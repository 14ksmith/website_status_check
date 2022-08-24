from url_request.url_monitor import get_websites_status
import asyncio


if __name__ == "__main__":

    # Create async event loop and run 'get_websites_status' until complete
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_websites_status())
