import time

import github

from git_token import GITHUB_TOKEN
from github import Github
from utils import *


class Search:
    def __init__(self):
        self.g = Github(GITHUB_TOKEN)

    # def search_repo(self, name: list):
    #     name.append("in:name")
    #     query = " ".join(name)
    #     result = self.g.search_repositories(query)
    #     print(result.totalCount)

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
                # repo.append(1)
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


if __name__ == '__main__':
    search = Search()
    search.repos_exist()
