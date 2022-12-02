import json
import re


def framework_result_analysis():
    f = open("api_result.json")
    data = json.load(f)
    repo_no_manual = 0
    repo_has_espresso = 0
    repo_has_uiautomator = 0
    repo_has_both = 0
    for repo in data:
        if not repo["require manual check"]:
            repo_no_manual += 1
        if repo["espresso used"]:
            repo_has_espresso += 1
        if repo["uiautomator used"]:
            repo_has_uiautomator += 1
        if repo["uiautomator used"] and repo["espresso used"]:
            print(repo["repository"])
            repo_has_both += 1
    print("repo no manual", repo_no_manual)
    print("repo has espresso", repo_has_espresso)
    print("repo has uiautomator", repo_has_uiautomator)
    print("repo has both", repo_has_both)


def app_suite_analysis():
    suite = "/home/ruizhen/AndroidStudioProjects/DroidShows/app/src/androidTest/java/nl/asymmetrics/droidshows/TestSuite.java"
    file = open(suite, "r")
    lines = file.readlines()
    pattern = ".*\\/\\/ [0-9]{1,2}. (.*)."
    total_lines = 0
    unique_lines = set()
    for line in lines:
        if "//" in line:
            match = re.match(pattern, line).group(1)
            unique_lines.add(match)
            total_lines += 1
    print(total_lines)
    print(len(unique_lines))


if __name__ == '__main__':
    app_suite_analysis()
