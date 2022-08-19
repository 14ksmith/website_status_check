import requests
from requests.exceptions import HTTPError
import asyncio
from aiohttp import ClientSession, ClientResponseError


# -------------------------------- Async ------------------------------------------#


async def request_url(session: ClientSession, url):
    """Send request for the given url. Raise the status of the request."""

    response = await session.request("GET", url=url)

    response.raise_for_status()


async def get_websites_status(urls):
    """For each url provided, get the status of the request."""

    # add a list of coroutines to complete
    async with ClientSession() as session:

        tasks = []

        for url in urls:
            print(url)

            try:
                tasks.append(request_url(session=session, url=url))
                print("This website is working right now :)")

            except ClientResponseError as e:
                print(e)
                print("This website is currently down.")

        # execute all the tasks and wait for them to complete
        asyncio.wait(tasks)


# --------------------------------------------------------------------------------#


# -------------------------- Not Async ------------------------------------------#

# def request_url(url):
#     """Send request for the given url. Raise the status of the request."""

#     response = requests.get(url=url)

#     response.raise_for_status()


# def get_websites_status(urls):
#     """For each url provided, get the status of the request."""

#     for url in urls:
#         print(url)

#         try:
#             request_url(url=url)
#             print("This website is working right now :)")

#         except HTTPError as e:
#             print(e)
#             print("This website is currently down.")
# --------------------------------------------------------------------------------#
