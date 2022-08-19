from settings.open_settings import open_settings
from url_request.url_request import request_url
from requests.exceptions import HTTPError


settings = open_settings()
# Second return value from open_settings is the dict of websites. set urls to the values.
urls = settings[1].values()

for url in urls:
    print(url)

    try:
        request_url(url=url)
        print("This website is working right now :)")

    except HTTPError as e:
        print(e)
        print("This website is currently down.")
