from os import listdir, path
import xml.etree.ElementTree as Et


class Operator:
    def __init__(self):
        self.resource = '../../../Experiment/ShiftCal/app/src/main/res/layout/'
        self.layouts = [lo for lo in listdir(self.resource)]
        Et.register_namespace('android', 'http://schemas.android.com/apk/res/android')
        Et.register_namespace('app', 'http://schemas.android.com/apk/res-auto')
        Et.register_namespace('tools', 'http://schemas.android.com/tools')

    def parse_components(self):
        for xml in self.layouts:
            layout = Layout(path.join(self.resource, xml))
            deletion = layout.get_deletion()
            if len(deletion) != 0:
                print(xml)


class Layout:
    def __init__(self, xml):
        self.path = xml
        self.button_deletion = False
        self.edit_text_deletion = False
        self.tree = Et.parse(path.join(self.path))
        self.root = self.tree.getroot()

    def get_deletion(self):
        deletion = []
        self.tree_walk(self.root)
        if self.button_deletion:
            deletion.append("Button")
            self.tree.write(self.path)
        if self.edit_text_deletion:
            deletion.append("EditText")
            self.tree.write(self.path)
        return deletion

    def tree_walk(self, root):
        if "Button" in root.tag:
            self.button_deletion = True
            root.set('{http://schemas.android.com/apk/res/android}visibility', 'gone')
        if root.tag == "EditText":
            self.edit_text_deletion = True
            root.set('{http://schemas.android.com/apk/res/android}visibility', 'gone')
        for child in root:
            self.tree_walk(child)

    def generate_mutant(self):
        pass


if __name__ == '__main__':
    operator = Operator()
    operator.parse_components()
