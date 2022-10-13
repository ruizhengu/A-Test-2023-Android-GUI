import json
import pandas as pd

data_path = "gui_repos.xlsx"
# data_writer = pd.ExcelWriter(data_path)
sheet_repositories = "repositories"
sheet_exist = "exist"


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
