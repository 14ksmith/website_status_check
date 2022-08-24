import json
import asyncio
from aiohttp import ClientSession, ClientResponseError
from notifications.email import send_email
from time import perf_counter


class ReadSettings:
    def __init__(self):
        """Get the settings from the settings.json."""

        with open("settings/settings.json") as settings:
            website_status_settings = json.load(settings)

        # get the hours between website status checks
        self.seconds_between_status_checks = website_status_settings.get(
            "seconds_between_checks"
        )
        # get the websites to be checked
        self.websites_to_check = website_status_settings.get(
            "websites_to_check"
        ).values()

        # Get the email server
        self.email_server = website_status_settings.get("email_server")


def send_website_down_email(websites_down, email_server):
    """Send an email notification with websites down from websites_down list (ignore 'None')."""

    email_body = f"The following websites are currently down:\n\n"
    down_websites = False

    for website in websites_down:
        if website != None:
            email_body += f"{website}\n"
            down_websites = True

    if down_websites:
        send_email(email_body=email_body, server=email_server)


async def request_url(session: ClientSession, url):
    """Send request for the given url. Raise the status of the request."""

    try:

        response = await session.request("GET", url=url)
        response.raise_for_status()
        print(f"{url} is working right now :)")

    except ClientResponseError as error:

        if error.status == 301:
            print(url, "Permanent Redirect", error.status)

        elif error.status == 302:
            print(url, "Temporary Redirect", error.status)

        elif error.status == 403:
            print(url, "Website Forbidden", error.status)
            return url

        elif error.status == 404:
            print(url, "Website Not Found", error.status)

        elif error.status == 410:
            print(url, "Website Gone", error.status)

        elif error.status == 500:
            print(url, "Internal Server Error, Website Down", error.status)
            return url

        elif error.status == 503:
            print(url, "Service Unavailable, Website Down", error.status)
            return url

        else:
            print(url, "unhandled error code", error.status)


async def request_all_urls(session: ClientSession, urls):
    """Request all urls in settings and return websites that are down."""
    output = await asyncio.gather(
        *[request_url(session=session, url=url) for url in urls]
    )
    return output


async def get_websites_status():
    """For each url provided, get the status of the request."""

    settings = ReadSettings()

    while True:

        # add a list of coroutines to complete
        async with ClientSession() as session:

            t1 = perf_counter()

            websites_down = await request_all_urls(
                session=session, urls=settings.websites_to_check
            )
            t2 = perf_counter()
            print(f"total time: {t2 - t1}")

        send_website_down_email(
            websites_down=websites_down, email_server=settings.email_server
        )

        # Sleep the program for the designated time between requests
        await asyncio.sleep(settings.seconds_between_status_checks)
