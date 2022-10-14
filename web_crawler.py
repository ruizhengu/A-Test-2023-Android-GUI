import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Crawler:
    def __init__(self, repo):
        self.driver = webdriver.Chrome()
        self.driver.get(f"https://github.com/{repo}")
        self.driver.set_page_load_timeout(10)

    # get in the app folder
    def get_in_app(self):
        time.sleep(2)
        self.ele_click("app")

    # get in the src folder
    def get_in_src(self):
        self.ele_click("src")

    # get in the folder began with androidTest
    def get_in_android_test(self):
        self.ele_contain_click("androidTest")

    # click element by title
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

    # click element contains title
    def ele_contain_click(self, title_contain):
        ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        files = ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")
        for file in files:
            if title_contain in file.text:
                file.click()
                break
        time.sleep(2)

    # check if androidTest folder exists
    def if_android_test(self):
        ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        files = ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")
        for file in files:
            if file.text != ".\u200a." and file.text != "ExampleInstrumentedTest.java" and file.text != "":
                return True
        return False

    # get in test folders if any
    def get_folders(self):
        ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        folders = [folder.text for folder in ele_files.find_elements(By.XPATH,
                                                                     "//*[contains(@aria-label, 'Directory')]/../following-sibling::div/span/*[contains(@class, 'js-navigation-open')]")]
        return folders

    # open all test files ends with .java or .kt
    def open_test(self):
        folders = self.get_folders()
        if len(folders) != 0:
            for folder in folders:
                if len(self.driver.find_elements(By.XPATH, f"//*[text()='{folder}']")) != 0:
                    self.driver.find_element(By.XPATH, f"//*[text()='{folder}']").click()
                else:
                    self.driver.find_element(By.XPATH,
                                             f"//*[text()='{folder.split('/')[-1]}']/*[text()='{'/'.join(folder.split('/')[:-1]) + '/'}']").click()
                time.sleep(2)
                self.open_test()
                self.back()
        else:
            ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
            file_names = [file.text for file in
                          ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")]
            for file in file_names:
                if file != ".\u200a." and "ExampleInstrumentedTest" not in file and file != "" and file.endswith(
                        (".java", ".kt")):
                    self.driver.find_element(By.XPATH, f"//*[text()='{file}']").click()
                    self.check_test()

    # check the content of the test
    def check_test(self):
        # print("check test")
        time.sleep(2)
        self.back()

    def back(self):
        self.driver.back()
        time.sleep(2)

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    repo = "FoVlaX/test_architecture"
    crawler = Crawler(repo)
    crawler.get_in_app()
    crawler.get_in_src()
    crawler.get_in_android_test()
    if crawler.if_android_test():
        crawler.open_test()
    time.sleep(5)
    crawler.close()
