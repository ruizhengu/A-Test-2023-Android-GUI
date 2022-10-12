import json
import pandas as pd

from utils import data_file

f = open("repos.json")
data = json.load(f)

gui_repos = []

for repo in data:
    attr = data[repo]

    if attr["gui_test_ratio"] != 0:
        gui_repos.append(repo)

gui_data = pd.DataFrame(gui_repos, columns=["repository"])
gui_data.to_excel(data_file, sheet_name="repositories")
