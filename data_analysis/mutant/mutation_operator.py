import os
from os import listdir, path
import xml.etree.ElementTree as Et
from distutils.dir_util import copy_tree
import pandas as pd

result = []


class Operator:
    def __init__(self):
        self.resource = '../../../Experiment/DroidShows/app/src/main/res/layout/'
        self.layouts = [lo for lo in listdir(self.resource)]
        Et.register_namespace('android', 'http://schemas.android.com/apk/res/android')
        Et.register_namespace('app', 'http://schemas.android.com/apk/res-auto')
        Et.register_namespace('tools', 'http://schemas.android.com/tools')

    def parse_components(self):
        for xml in self.layouts:
            tree = Et.parse(path.join(self.resource, xml))
            root = tree.getroot()
            layout = Layout(xml, tree)
            layout.tree_walk(root)


class Layout:
    def __init__(self, xml, tree):
        self.xml = xml
        self.tree = tree
        self.origin_main = "../../../Experiment/DroidShows/app/src/main"
        self.mutants_path = "Mutant_DroidShows"
        self.result_file = "mutation.xlsx"
        self.result_sheet_name = "DroidShows - BWD - TWD"
        self.result_header = [
            "Mutant",
            "Resource",
            "Tag",
            "Operator",
            "Valid"
        ]

    def tree_walk(self, root):
        if "Button" in root.tag or "EditText" in root.tag:
            root.set('{http://schemas.android.com/apk/res/android}visibility', 'gone')
            print(os.path.basename(self.xml))
            self.generate_mutant(root)
            root.attrib.pop('{http://schemas.android.com/apk/res/android}visibility')
        for child in root:
            self.tree_walk(child)

    def generate_mutant(self, root):
        mutant_directory = self.get_mutant_directory()
        self.mutation_logging(mutant_directory, self.xml, root)
        os.mkdir(mutant_directory)
        copy_tree(self.origin_main, mutant_directory)
        self.tree.write(os.path.join(mutant_directory, "res", "layout", self.xml))

    def get_mutant_directory(self):
        mutants = [m for m in os.listdir(self.mutants_path) if "log" not in m]
        return os.path.join(self.mutants_path, f"mutant_{len(mutants) + 1}")

    def mutation_logging(self, file, xml, root):
        result_tmp = [os.path.basename(file), xml]
        if "Button" in root.tag:
            result_tmp.append("Button widget deletion")
        else:
            result_tmp.append("EditText widget deletion")
        result_tmp.append(root.tag)
        result_tmp.append("TBD")
        result.append(result_tmp)
        df = pd.DataFrame(result, columns=self.result_header)
        df.to_excel(self.result_file, sheet_name=self.result_sheet_name, index=False)


if __name__ == '__main__':
    operator = Operator()
    operator.parse_components()
