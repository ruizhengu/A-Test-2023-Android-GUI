from git_token import GITHUB_TOKEN
from github import Github


class Search:
    def __init__(self):
        self.g = Github(GITHUB_TOKEN)

    def search_repo(self, name: list):
        name.append("in:name")
        query = " ".join(name)
        result = self.g.search_repositories(query)
        print(result.totalCount)


if __name__ == '__main__':
    search = Search()
    names = ["0xpr03/VocableTrainer-Android"]
    search.search_repo(names)
