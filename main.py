from url_request.url_monitor import get_websites_status
import asyncio
from time import perf_counter


if __name__ == "__main__":

    t1_start = perf_counter()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_websites_status())

    t1_stop = perf_counter()

    print(f"Elapsed time: {t1_stop - t1_start} seconds.")
