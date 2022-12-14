import os
from os import listdir, path
import xml.etree.ElementTree as Et
from distutils.dir_util import copy_tree


class Operator:
    def __init__(self):
        self.resource = '../../../Experiment/ShiftCal/app/src/main/res/layout/'
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
        self.origin_main = "../../../Experiment/ShiftCal/app/src/main"
        self.mutants_path = "Mutant_ShiftCal"

    def tree_walk(self, root):
        if "Button" in root.tag or "EditText" in root.tag:
            root.set('{http://schemas.android.com/apk/res/android}visibility', 'gone')
            print(os.path.basename(self.xml))
            self.generate_mutant()
            root.attrib.pop('{http://schemas.android.com/apk/res/android}visibility')
        for child in root:
            self.tree_walk(child)

    def generate_mutant(self):
        mutant_directory = self.get_mutant_directory()
        os.mkdir(mutant_directory)
        copy_tree(self.origin_main, mutant_directory)
        self.tree.write(os.path.join(mutant_directory, "res", "layout", self.xml))

    def get_mutant_directory(self):
        mutants = [m for m in os.listdir(self.mutants_path) if "mutant" in m]
        return os.path.join(self.mutants_path, f"mutant_{len(mutants) + 1}")


if __name__ == '__main__':
    operator = Operator()
    operator.parse_components()
