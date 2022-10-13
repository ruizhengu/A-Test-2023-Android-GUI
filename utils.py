import json
import pandas as pd
import math

data_path = "gui_repos.xlsx"
sheet_repositories = "repositories"
sheet_exist = "exist"
sheet_espresso = "espresso"
sheet_uiautomator = "uiautomator"
sheet_both = "both"
search_keywords = {
    "espresso": ["espresso"],
    "uiautomator": ["uiautomator"],
    "both": ["espresso, uiautomator"]
}


def repo_filter():
    f = open("repos.json")
    data = json.load(f)
    gui_repos = []

    for repo in data:
        attr = data[repo]
        if attr["num_androidTests"] != 0:
            gui_repos.append(repo)

    gui_data = pd.DataFrame(gui_repos, columns=["repository"])
    with pd.ExcelWriter(data_path) as writer:
        gui_data.to_excel(writer, sheet_name=sheet_repositories, index=False)


# repo_filter()

# get currently valid repositories as the targets
def get_target_repos():
    repos = pd.read_excel(data_path, sheet_name=sheet_exist)
    repo_num = repos.shape[0]
    target_repos = []
    for i in range(repo_num):
        repo = repos.iloc[i]
        if repo["count"] != 0:
            if type(repo["new"]) != str and math.isnan(repo["new"]):
                target_repos.append(repo["repository"])
            else:
                target_repos.append(repo["new"])
    return target_repos


# get_target_repos()

def get_test_count(tools):
    repos = pd.read_excel(data_path, sheet_name=tools)
    repo_num = repos.shape[0]
    test_repos = []
    for i in range(repo_num):
        repo = repos.iloc[i]
        if repo["espresso, uiautomator"] > 1:
            test_repos.append(repo["repository"])
    print(len(test_repos))


get_test_count("both")
