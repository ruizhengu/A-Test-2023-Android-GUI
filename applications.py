import json
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By

app_file = "app.json"


class Application:
    def __init__(self, permission):
        self.driver = webdriver.Chrome()
        self.permission = permission
        self.category = [
            "connectivity",
            "development",
            "games",
            "graphics",
            "internet",
            "money",
            "multimedia",
            "navigation",
            "phone-sms",
            "reading",
            "science-education",
            "security",
            "sports-health",
            "system",
            "theming",
            "time",
            "writing"
        ]

    def switch_page(self):
        for cat in self.category:
            self.driver.get(f"https://f-droid.org/en/categories/{cat}/")
            time.sleep(2)
            pagination = self.driver.find_element(By.CLASS_NAME, "browse-navigation")
            pages = pagination.find_elements(By.CLASS_NAME, "nav")
            page_number = len(pages) - 3
            self.all_apps()
            for i in range(page_number):
                self.driver.get(f"https://f-droid.org/en/categories/{cat}/{i + 2}/")
                time.sleep(1)
                self.all_apps()
                time.sleep(1)

    def all_apps(self):
        apps = self.driver.find_element(By.ID, "package-list").find_elements(By.XPATH,
                                                                             "//*[contains(@class, 'package-header')]")
        app_href = [a.get_property("href") for a in apps]
        for href in app_href:
            self.driver.get(href)
            time.sleep(1)
            self.app_permission()
            time.sleep(1)

    def app_permission(self):
        try:
            app_name = self.driver.find_element(By.CLASS_NAME, "package-name").text
        except selenium.common.exceptions.NoSuchElementException:
            self.driver.refresh()
            time.sleep(1)
            app_name = self.driver.find_element(By.CLASS_NAME, "package-name").text
        try:
            latest_version = self.driver.find_element(By.ID, "latest")
            permission_element = latest_version.find_element(By.CLASS_NAME, "package-version-permissions-list")
            permission_items = permission_element.find_elements(By.CLASS_NAME, "permission")
            for item in permission_items:
                if self.permission in item.text:
                    self.append_application(app_name)
                    break
        except selenium.common.exceptions.NoSuchElementException:
            print(app_name)

    def append_application(self, application):
        result = {
            "application": application,
            "permission": self.permission
        }
        with open(app_file, "r") as file:
            feeds = json.load(file)
            feeds.append(result)
        with open(app_file, "w") as file:
            json.dump(feeds, file)

    def close(self):
        self.driver.close()


def get_apps():
    app_calendar_file = "app_calendar.json"
    with open(app_file, "r") as file:
        feeds = json.load(file)
    unique = []
    for app in feeds:
        if app not in unique:
            unique.append(app)
    with open(app_calendar_file, "w") as f:
        json.dump(unique, f, indent=4)


if __name__ == '__main__':
    # with open(app_file, "w") as f:
    #     json.dump([], f)
    #
    # app = Application("calendar")
    # app.switch_page()
    # time.sleep(2)
    # app.close()
    get_apps()
