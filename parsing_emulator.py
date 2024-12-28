"""
parsing with using emulator
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import undetected_chromedriver as ucd

import time

import asyncio


class Parser:
    def __init__(self):
        self.website: str = 'https://www.ozon.ru/'
        self.main()

    async def load_info(self, product: str = ''):
        self.parser = ucd.Chrome()
        self.parser.get(self.website)

        await asyncio.sleep(2)

        print(self.parser)

    async def input_category(self):
        input = self.parser.find_element(By.NAME, 'text')
        input.clear()
        input.send_keys(self.name_product_pars)
        await asyncio.sleep(2)
        input.send_keys(Keys.ENTER)
        print("Нажатие ENTER")
        await asyncio.sleep(5)

    def main(self):
        print("Введите категорию товаров:")
        self.name_product_pars: str = input()
        asyncio.run(self.load_info(self.name_product_pars))
        asyncio.run(self.input_category())
        print("Ожидание?")


if __name__ == "__main__":
        info = Parser()

