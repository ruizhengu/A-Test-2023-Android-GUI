from os import listdir, path
import xml.etree.ElementTree as ET


class Operator:
    def __init__(self):
        self.resource = '../../../Experiment/ShiftCal/app/src/main/res/layout/'
        self.layouts = [l for l in listdir(self.resource)]

    def get_components(self):
        for xml in self.layouts:
            layout = Layout(path.join(self.resource, xml))
            deletion = layout.get_deletion()
            if len(deletion) != 0:
                print(xml)
                print(deletion)

    def button_widget_deletion(self):
        pass


class Layout:
    def __init__(self, xml):
        self.path = xml
        self.button_deletion = False
        self.edit_text_deletion = False
        self.tree = ET.parse(path.join(self.path))
        self.root = self.tree.getroot()

    def get_deletion(self):
        deletion = []
        self.tree_walk(self.root)
        if self.button_deletion:
            deletion.append("Button")
        if self.edit_text_deletion:
            deletion.append("EditText")
        return deletion

    def tree_walk(self, root):
        if root.tag == "Button":
            self.button_deletion = True
        if root.tag == "EditText":
            self.edit_text_deletion = True
        for child in root:
            self.tree_walk(child)


if __name__ == '__main__':
    operator = Operator()
    operator.get_components()
