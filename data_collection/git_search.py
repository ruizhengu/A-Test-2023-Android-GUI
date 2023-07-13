import time

import github

from git_token import GITHUB_TOKEN
from github import Github
from data_collection.utils import *


class Search:
    def __init__(self):
        self.g = Github(GITHUB_TOKEN)

    # get repos from excel
    @staticmethod
    def get_repos():
        repo_filter()
        repo_data = pd.read_excel(data_path, sheet_name=sheet_repositories)
        data_list = repo_data.values.tolist()
        return data_list

    # dose the repo with the name exists
    def repos_exist(self):
        repos = self.get_repos()
        for repo in repos:
            try:
                query = f"repo:{repo[0]}"
                result = self.g.search_repositories(query)
                repo.append(result.totalCount)
            except github.GithubException as e:
                if e.data["message"] == "Validation Failed":
                    repo.append(0)
                else:
                    print(repo)
                    print(e.data["message"])
                    time.sleep(60)
                continue
        exist_data = pd.DataFrame(repos, columns=["repository", "count"])
        with pd.ExcelWriter(data_path, mode="a") as writer:
            exist_data.to_excel(writer, sheet_name=sheet_exist, index=False)

    # searching code by keywords in repos
    def search_in_repo(self, keywords: list, sheet: str):
        target_repos = get_target_repos()
        data = []
        for repo in target_repos:
            for attempt in range(10):
                try:
                    query = f"{' '.join(keywords)} repo:{repo}"
                    result = self.g.search_code(query)
                    data.append([repo, result.totalCount])
                    # data.append([repo, 1])
                except github.GithubException as e:
                    print(e)
                    time.sleep(60)
                else:
                    break
            else:
                continue
        code_data = pd.DataFrame(data, columns=["repository", " ".join(keywords)])
        with pd.ExcelWriter(data_path, mode="a", if_sheet_exists="replace") as writer:
            code_data.to_excel(writer, sheet_name=sheet, index=False)


if __name__ == '__main__':
    search = Search()
    search.search_in_repo(search_keywords["both"], sheet_both)
