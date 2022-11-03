import json

if __name__ == '__main__':
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
