import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Crawler:
    def __init__(self, repo):
        self.driver = webdriver.Chrome()
        self.driver.get(f"https://github.com/{repo}")
        self.driver.set_page_load_timeout(10)

    def get_in_app(self):
        # ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        # files = ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")
        # dicts = {}
        # for file in files:
        #     dicts[file.text] = file
        # if "app" in dicts:
        #     dicts["app"].click()
        self.ele_click("app")

    def get_in_src(self):
        self.ele_click("src")

    def get_in_android_test(self):
        self.ele_contain_click("androidTest")

    def ele_click(self, title):
        ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        files = ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")
        dicts = {}
        for file in files:
            dicts[file.text] = file
        if title in dicts:
            dicts[title].click()
        else:
            "element not found"
        time.sleep(2)

    def ele_contain_click(self, title_contain):
        ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        files = ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")
        for file in files:
            if title_contain in file.text:
                file.click()
                break
        time.sleep(2)

    def if_android_test(self):
        ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        files = ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")
        for file in files:
            if file.text != ".\u200a." and file.text != "ExampleInstrumentedTest.java" and file.text != "":
                return True
        return False

    def get_in_folder(self):
        ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        folders = ele_files.find_elements(By.XPATH, "//*[contains(@aria-label, 'Directory')]")
        print(len(folders))
        # files = ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    repo = "Nizar127/MedicInfo"
    crawler = Crawler(repo)
    crawler.get_in_app()
    crawler.get_in_src()
    crawler.get_in_android_test()
    crawler.get_in_folder()
    print(crawler.if_android_test())
    time.sleep(5)
    crawler.close()
