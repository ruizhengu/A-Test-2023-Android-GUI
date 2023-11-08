import time

import openpyxl
import requests


class Crawler:
    def __init__(self):
        self.token = "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"
        self.file_name = "adoption.xlsx"
        self.file = openpyxl.load_workbook(self.file_name)
        self.sheet = self.file["repositories"]

        self.keyword_position = {
            "Espresso": 2,
            "UI Automator": 3,
            "Appium": 4
        }

    def search_code(self, keyword):
        for row in range(2, self.sheet.max_row + 1):
            cell = self.sheet.cell(row=row, column=1)
            owner = cell.value.split("/")[0]
            repo = cell.value.split("/")[1]
            response = requests.get(f"https://api.github.com/search/code?q={keyword}+repo:{owner}/{repo}",
                                    headers={"Authorization": f"token {self.token}"})
            data = response.json()
            if data["total_count"] > 1:
                self.sheet.cell(row=row, column=self.keyword_position[keyword]).value = 1
            else:
                self.sheet.cell(row=row, column=self.keyword_position[keyword]).value = 0
            print(f"repo: {cell.value} progress: {row - 1} / {self.sheet.max_row - 1} ")
            print(data)
            self.file.save(self.file_name)
            time.sleep(6)

    def search_test(self, keyword, repo):
        owner = repo.split("/")[0]
        repo = repo.split("/")[1]
        response = requests.get(f"https://api.github.com/search/code?q={keyword}+repo:{owner}/{repo}",
                                headers={"Authorization": f"token {self.token}"})
        data = response.json()
        print(data)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.search_code("Appium")
    # crawler.search_test("Appium", "BarryBryant/rally-genius-android")
