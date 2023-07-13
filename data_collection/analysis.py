import json
import re
import pandas as pd


def framework_result_analysis():
    f = open("data_collection/api_result.json")
    data = json.load(f)
    repo_no_manual = 0
    repo_has_espresso = 0
    repo_has_uiautomator = 0
    repo_has_both = 0
    no_manual_repos = []
    for repo in data:
        if not repo["require manual check"]:
            repo_no_manual += 1
            no_manual_repos.append(repo)
        if repo["espresso used"]:
            repo_has_espresso += 1
        if repo["uiautomator used"]:
            repo_has_uiautomator += 1
        if repo["uiautomator used"] and repo["espresso used"]:
            # print(repo["repository"])
            repo_has_both += 1
    print("repo no manual", repo_no_manual)
    print("repo has espresso", repo_has_espresso)
    print("repo has uiautomator", repo_has_uiautomator)
    print("repo has both", repo_has_both)
    get_manual_check_repos(get_repo_names(no_manual_repos))


def get_repo_names(repo_details):
    repo_names = []
    for item in repo_details:
        repo_names.append(item["repository"])
    return repo_names


def get_manual_check_repos(manual_repos):
    data = pd.read_excel("data_collection/gui_repos.xlsx", "exist")
    for index, repo in data.iterrows():
        if repo["repository"] not in manual_repos and repo["new"] not in manual_repos and repo["count"] == 1:
            print(repo["repository"])


def app_suite_analysis():
    suite = "/home/ruizhen/Projects/PycharmProjects/autcom/baseline/ShiftCal/Baseline.java"
    file = open(suite, "r")
    lines = file.readlines()
    pattern = ".*\\/\\/ [0-9]{1,2}. (.*)."
    total_lines = 0
    unique_lines = set()
    for line in lines:
        if "//" in line:
            match = re.match(pattern, line).group(1)
            print(match)
            unique_lines.add(match)
            total_lines += 1
    print(total_lines)
    print(len(unique_lines))


def loc_cal():
    suite = "/home/ruizhen/Projects/PycharmProjects/autcom/baseline/DroidShows/Baseline.java"
    file = open(suite, "r")
    lines = file.readlines()
    total_lines = 0
    unique_lines = set()
    for line in lines:
        if "device." in line or "onView" in line or "pressBack" in line:
            if "assert" not in line and "import" not in line:
                unique_lines.add(line.strip())
                total_lines += 1
    print(total_lines)
    print(len(unique_lines))
    uiautomator_exclusive = 0
    for unique in unique_lines:
        if "device" in unique:
            uiautomator_exclusive += 1
            print(unique)

    print(uiautomator_exclusive)


if __name__ == '__main__':
    framework_result_analysis()
