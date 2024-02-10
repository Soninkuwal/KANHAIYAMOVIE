# Credit @KANHADeveloper.

# Please Don't remove credit.

# Born to make history @KANHADeveloper !

# Thank you KANHADeveloper for helping us in this Journey

# 🥰  Thank you for giving me credit @KANHADeveloper  🥰

# for any error please contact me -> telegram@KANHADeveloper or insta @KANHADeveloper 

# rip paid developers 🤣 - >> No need to buy paid source code while @KANHADeveloper is here 😍😍
import asyncio
import logging
import aiohttp
import traceback
from info import *


async def ping_server():
    sleep_time = PING_INTERVAL
    while True:
        await asyncio.sleep(sleep_time)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(URL) as resp:
                    logging.info("Pinged server with response: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Couldn't connect to the site URL..!")
        except Exception:
            traceback.print_exc()
