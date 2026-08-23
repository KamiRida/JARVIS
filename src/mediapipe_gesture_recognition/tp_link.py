import asyncio
from kasa import Discover
from dotenv import load_dotenv
from dotenv import dotenv_values
import os

load_dotenv()
print(list(dotenv_values().keys()))
get = os.getenv
print(load_dotenv())
async def right_turn_off():
    dev = await Discover.discover_single(get("IP_Address_right"), username = get("TP_LINK_USERNAME"), password=get("TP_LINK_PASSWORD"))

    await dev.turn_off()
    await dev.update()
async def right_turn_on():
    dev = await Discover.discover_single(get("IP_Address_right"), username = get("TP_LINK_USERNAME"), password=get("TP_LINK_PASSWORD"))

    await dev.turn_on()
    await dev.update()

async def left_turn_off():
    dev = await Discover.discover_single(get("IP_Address_left"), username = get("TP_LINK_USERNAME"), password=get("TP_LINK_PASSWORD"))

    await dev.turn_off()
    await dev.update()

async def left_turn_on():
    dev = await Discover.discover_single(get("IP_Address_left"), username = get("TP_LINK_USERNAME"), password=get("TP_LINK_PASSWORD"))

    await dev.turn_on()
    await dev.update()

async def led1_turn_off():
    dev = await Discover.discover_single(get("IP_Address_LED1"), username = get("TP_LINK_USERNAME"), password=get("TP_LINK_PASSWORD"))

    await dev.turn_off()
    await dev.update()

async def led1_turn_on():
    dev = await Discover.discover_single(get("IP_Address_LED1"), username = get("TP_LINK_USERNAME"), password=get("TP_LINK_PASSWORD"))

    await dev.turn_on()
    await dev.update()

async def led2_turn_off():
    dev = await Discover.discover_single(get("IP_Address_LED2"), username = get("TP_LINK_USERNAME"), password=get("TP_LINK_PASSWORD"))

    await dev.turn_off()
    await dev.update()

async def led2_turn_on():
    dev = await Discover.discover_single(get("IP_Address_LED2"), username = get("TP_LINK_USERNAME"), password=get("TP_LINK_PASSWORD"))

    await dev.turn_on()
    await dev.update()

#asyncio.run(right_turn_off())