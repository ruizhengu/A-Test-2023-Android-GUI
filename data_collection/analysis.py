import json
import re


def framework_result_analysis():
    f = open("api_result.json")
    data = json.load(f)
    repo_no_manual = 0
    repo_need_manual = 0
    repo_has_espresso = 0
    repo_has_uiautomator = 0
    repo_has_both = 0
    for repo in data:
        if repo["require manual check"]:
            repo_need_manual += 1
        if not repo["require manual check"]:
            repo_no_manual += 1
        if repo["espresso used"]:
            repo_has_espresso += 1
        if repo["uiautomator used"]:
            repo_has_uiautomator += 1
        if repo["uiautomator used"] and repo["espresso used"]:
            # print(repo["repository"])
            repo_has_both += 1
    print("repo need manual", repo_need_manual)
    print("repo no manual", repo_no_manual)
    print("repo has espresso", repo_has_espresso)
    print("repo has uiautomator", repo_has_uiautomator)
    print("repo has both", repo_has_both)


def app_suite_analysis():
    suite = "/home/ruizhen/Projects/PycharmProjects/autcom/baseline/ShiftCal/Baseline.java"
    # with open(suite, "r") as f:
    #     lines = f.readlines()
    # for line in lines:
    #     if ""
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
                # print(line.strip())
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
