import time

import github.GithubException

from git_token import GITHUB_TOKEN
from github import Github
from write_csv import Writer

g = Github(GITHUB_TOKEN)

# search keywords
keywords = ["androidx.test.uiautomator", "androidx.test.espresso"]
# search in build.gradle
languages = ["language:" + language for language in ["Gradle"]]
keywords.extend(languages)
query = " ".join(keywords)
print(query)

writer = Writer()
results = g.search_code(query)

counter = 0
for result in results:
    counter += 1
    if counter % 30 == 0:
        time.sleep(60)
    writer.write_row(result.repository.full_name, result.path, result.repository.stargazers_count)
    print(result.repository.stargazers_count)
