"""
parsing with using emulator
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import undetected_chromedriver as ucd

import asyncio


class Parser:
    def __init__(self, name):
        """
        Inizialization WenUrl - website
        start function main
        """
        self.website: str = 'https://www.ozon.ru/'
        self.name_product_pars: str = name

        self.main()


    def main(self):
        """
        Input search
        start syncio with load_info, input_category
        :return:
        """
        print("Введите категорию товаров:")

        asyncio.run(self.load_info(self.name_product_pars))
        asyncio.run(self.input_category())


    async def load_info(self, product: str = ''):
        """
        inizialization browser(in our script - Chrome browser)
        open ozon in browser and sleep 1 second for antibot
        :param product:
        :return:
        """
        self.parser = ucd.Chrome()
        self.parser.get(self.website)

        await asyncio.sleep(1)



    async def input_category(self):
        """
        find in Html "text"
        input our category(from keyboard)
        pressed ENTER and sleep 1 second for antibot
        start function pars_all()
        :return:
        """
        self.input = self.parser.find_element(By.NAME, 'text')
        self.input.clear()
        self.input.send_keys(self.name_product_pars)
        print(f"Название {self.name_product_pars}")

        await asyncio.sleep(1)

        self.input.send_keys(Keys.ENTER)
        print("Нажатие ENTER")

        await asyncio.sleep(2)

        self.pars_all()



    def pars_all(self):
        """
        function for start pars_url, pars_cost
        :return:
        """
        self.pars_url()
        self.pars_cost()



    def pars_url(self):
        """
        find urls in Ozon
        :return:
        """
        try:
            self.links = self.parser.find_elements(By.CLASS_NAME, 'tile-clickable-element')
            print(f'{self.links} это был links')

            self.products = list(set(f'{link.get_attribute("href")}' for link in self.links))
            print(f'{self.products} это все продукты с длинной {len(self.products)}')

        except:
            print("[ERROR] dont find elemets of url")



    def pars_cost(self):
        """
        find cost of our products in Ozon
        :return:
        """
        print("pars cost")
        '''
        This block for future
        '''
        # try:
        #     self.cost = self.parser.find_element(By.CLASS_NAME, 'c3023-a1 tsHeadline500Medium c3023-b1 c3023-a6')
        #     print(f'cost {self.cost}')
        #     self.prod_cost = list(set(f'{costa.get_attribute("href")}' for costa in self.cost))
        # except Exception as er:
        #     print(f"[ERROR] dont find elemets of cost with error: {er}")


