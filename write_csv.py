import csv


class Writer:
    def __init__(self):
        self._csv_path = "repositories.csv"
        self._field_name = ["repository", "path", "stars"]

    def write_row(self, repository, path, stars):
        content = {
            "repository": repository,
            "path": path,
            "stars": str(stars)
        }
        with open(self._csv_path, "a") as f:
            row = csv.DictWriter(f, fieldnames=self._field_name)
            row.writerow(content)
        f.close()
