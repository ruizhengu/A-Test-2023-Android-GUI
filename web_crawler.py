import json
import os
import time
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import *

json_file = "api_result.json"


class Crawler:
    def __init__(self, repo):
        self.repo = repo
        self.driver = webdriver.Chrome()
        self.driver.get(f"https://github.com/{self.repo}")
        self.driver.set_page_load_timeout(10)
        self.require_manual_check = False
        self.espresso_used = False
        self.uiautomator_used = False
        self.espresso_apis = []
        self.uiautomator_apis = []

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
            self.require_manual_check = True
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
                if "/" not in folder:
                    self.driver.find_element(By.XPATH, f"//*[text()='{folder}' and not(span)]").click()
                else:
                    self.driver.find_element(By.XPATH,
                                             f"//*[text()='{folder.split('/')[-1]}']/*[text()='{'/'.join(folder.split('/')[:-1]) + '/'}']").click()
                time.sleep(2)
                self.open_test()
                self.back()
        # else:
        ele_files = self.driver.find_element(By.XPATH, "//*[contains(@class, 'Details-content')]")
        file_names = [file.text for file in
                      ele_files.find_elements(By.XPATH, "//*[contains(@class, 'js-navigation-open')]")]
        for file in file_names:
            if file != ".\u200a." and "ExampleInstrumentedTest" not in file and file != "" and file.endswith(
                    (".java", ".kt")):
                self.driver.find_element(By.XPATH, f"//*[text()='{file}']").click()
                time.sleep(2)
                self.get_code_with_keywords()

    # check if the code actually implemented the tools' apis
    def get_code_with_keywords(self):
        espresso_api = []
        uiautomator_api = []
        all_code = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'blob-code-inner')]")
        for code in all_code:
            if "import" in code.text:
                imports = code.text.split(" ")[-1]
                api = imports.split(".")[-1]
                if ";" in api:
                    api = api[:-1]
                if "espresso" in code.text:
                    espresso_api.append(api)
                if "uiautomator" in code.text:
                    uiautomator_api.append(api)
            else:
                for api in espresso_api:
                    if api in code.text:
                        self.espresso_used = True
                        self.espresso_apis.append(api)
                for api in uiautomator_api:
                    if api in code.text:
                        self.uiautomator_used = True
                        self.uiautomator_apis.append(api)
        time.sleep(2)
        self.back()

    def get_result(self):
        result = {
            "repository": self.repo,
            "require manual check": self.require_manual_check,
            "espresso used": self.espresso_used,
            "uiautomator used": self.uiautomator_used,
            "espresso apis": Counter(self.espresso_apis),
            "uiautomator apis": Counter(self.uiautomator_apis)
        }
        with open(json_file, "r") as file:
            feeds = json.load(file)
            feeds.append(result)
        with open(json_file, "w") as file:
            json.dump(feeds, file)

    def back(self):
        self.driver.back()
        time.sleep(2)

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    repos = get_target_repos()
    with open(json_file, "w") as f:
        json.dump([], f)

    for repo in repos:
        print(repo)
        crawler = Crawler(repo)
        crawler.get_in_app()
        crawler.get_in_src()
        if not crawler.require_manual_check:
            crawler.get_in_android_test()
            if crawler.if_android_test():
                crawler.open_test()
                crawler.get_result()
        time.sleep(2)
        crawler.close()

    # repo = "DroidsOnRoids/Toast-App"
    # crawler = Crawler(repo)
    # crawler.get_in_app()
    # crawler.get_in_src()
    # crawler.get_in_android_test()
    # if crawler.if_android_test():
    #     crawler.open_test()
    #     crawler.get_result()
    # time.sleep(5)
    # crawler.close()
