"""
This is script for parsing info
"""

import requests
import asyncio
from bs4 import BeautifulSoup


from to_json.rejson import json_dump


async def request_to():
    """
    standart request to ozon string
    :return:
    """
    url = "https://www.ozon.ru/product/komplekt-mysh-klaviatura-logitech-mk120-classic-desktop-920-002561-32549314/?campaignId=518"
    my_request = requests.get(url)
    print(my_request.text)
    to_class = BeautifulSoup(my_request.text, "html")
    print(to_class.prettify())

    name_file = 'test.json'
    await json_dump(name_file, my_request.text)

if __name__ == "__main__":
    asyncio.run(request_to())
