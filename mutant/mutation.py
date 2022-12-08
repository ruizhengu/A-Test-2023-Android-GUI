import re
import shutil
from os import listdir, path
from distutils.dir_util import copy_tree
import subprocess


class Mutation:
    def __init__(self):
        self.app_path = "../../../Experiment/ShiftCal"
        self.app_main_path = path.join(self.app_path, "app", "src", "main")
        self.mutant_path = "Mutant_ShiftCal"
        self.mutants = [m for m in listdir(self.mutant_path) if "log" not in m]
        self.test_script = "sh runJacoco.sh"
        self.mutant_log = "Mutant_ShiftCal/app-debug.apk-mutants.log"
        self.mutants_dict = self.get_mutant_info()

    def get_mutant_info(self):
        mutants_dict = dict()
        with open(self.mutant_log, "r") as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            results = re.search(r".*(Mutant [0-9]*).*; (.*) in.*", line)
            mutants_dict[results.group(1)] = results.group(2)
        return mutants_dict

    def replace_app_main(self, mutant_main):
        shutil.rmtree(self.app_main_path)
        mutant_main_path = path.join(self.mutant_path, mutant_main)
        copy_tree(mutant_main_path, self.app_main_path)

    def kill_mutants(self):
        for mutant in self.mutants:
            print(f"mutant: {mutant}")
            print(self.mutants_dict[mutant.replace("app-debug.apk-mutant", "Mutant ")])
            self.replace_app_main(mutant)
            process = subprocess.Popen(self.test_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, err = process.communicate()
            if "BUILD SUCCESSFUL" in output.decode("utf-8"):
                print("mutant killed")
            else:
                print(f"output: {output.decode('utf-8')}")
                print(f"err: {err.decode('utf-8')}")
                print("mutant not killed")
            break

    def result(self):
        pass


if __name__ == '__main__':
    mutation = Mutation()
    mutation.kill_mutants()
