import json
import asyncio
from aiohttp import ClientSession, ClientResponseError
from notifications.email import send_email
from time import sleep


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
    """If there are websites down (in the websites_down list) send an email notification."""

    if websites_down:

        email_body = f"The following websites are currently down:\n\n"

        for website in websites_down:
            email_body += f"{website}\n"

        send_email(email_body=email_body, server=email_server)


async def request_url(session: ClientSession, url):
    """Send request for the given url. Raise the status of the request."""

    response = await session.request("GET", url=url)

    response.raise_for_status()


async def get_websites_status():
    """For each url provided, get the status of the request."""

    settings = ReadSettings()

    while True:

        # add a list of coroutines to complete
        async with ClientSession() as session:

            websites_down = []

            tasks = []

            for url in settings.websites_to_check:
                print(url)

                try:
                    tasks.append(request_url(session=session, url=url))
                    print("This website is working right now :)")

                except ClientResponseError as e:
                    print(e)
                    websites_down.append(url)
                    print("This website is currently down.")

            # execute all the tasks and wait for them to complete
            asyncio.wait(tasks)

        send_website_down_email(
            websites_down=websites_down, email_server=settings.email_server
        )

        # Sleep the program for the designated time between requests
        sleep(settings.seconds_between_status_checks)
