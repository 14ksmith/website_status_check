from settings.open_settings import open_settings
from url_request.url_request import get_websites_status
import asyncio
from time import perf_counter


if __name__ == "__main__":

    settings = open_settings()
    # Second return value from open_settings is the dict of websites. set urls to the values.
    urls = settings[1].values()

    t1_start = perf_counter()

    # ----------------------------- Async --------------------------------#
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_websites_status(urls=urls))
    # --------------------------------------------------------------------#

    # ----------------------------- Not Async ----------------------------#
    # get_websites_status(urls=urls)
    # --------------------------------------------------------------------#

    t1_stop = perf_counter()

    print(f"Elapsed time: {t1_stop - t1_start} seconds.")
