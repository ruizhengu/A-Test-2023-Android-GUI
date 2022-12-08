import os
import re
import shutil
from os import listdir, path
from distutils.dir_util import copy_tree
import subprocess
import pandas as pd


class Mutation:
    def __init__(self):
        self.app_path = "../../../Experiment/ShiftCal"
        self.app_src_path = path.join(self.app_path, "app", "src")
        self.app_src_main_path = path.join(self.app_path, "app", "src", "main")
        self.mutant_path = "Mutant_ShiftCal"
        self.mutants = [m for m in listdir(self.mutant_path) if "log" not in m]
        self.test_script = "sh runJacoco.sh"
        self.mutant_log = "Mutant_ShiftCal/app-debug.apk-mutants.log"
        self.mutants_dict = self.get_mutant_info()
        self.result_file = "mutation.xlsx"
        self.result_sheet_name = "ShiftCal"
        self.result_header = [
            "Mutant",
            "Operator",
            "Kill",
            "Error"
        ]

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
        if os.path.exists(self.app_src_main_path):
            shutil.rmtree(self.app_src_main_path)
        mutant_main_path = path.join(self.mutant_path, mutant_main)
        destination = os.path.join(self.app_src_path, os.path.basename(mutant_main_path))
        copy_tree(mutant_main_path, destination)
        os.rename(destination, self.app_src_main_path)

    def kill_mutants(self):
        result = []
        for mutant in self.mutants:
            print(mutant)
            result_tmp = [mutant, self.mutants_dict[mutant.replace("app-debug.apk-mutant", "Mutant ")]]
            self.replace_app_main(mutant)
            process = subprocess.Popen(self.test_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, err = process.communicate()
            if "BUILD SUCCESSFUL" in output.decode("utf-8"):
                result_tmp.append("killed")
                result_tmp.append("None")
            else:
                result_tmp.append("not killed")
                result_tmp.append(err.decode('utf-8'))
            result.append(result_tmp)
            self.write_result(result)

    def write_result(self, result):
        df = pd.DataFrame(result, columns=self.result_header)
        df.to_excel(self.result_file, sheet_name=self.result_sheet_name, index=False)

    # @staticmethod
    # def get_error_type(err):
    #     if "FAILURE: Build failed with an exception." in err:
    #         return "Build failed with an exception"
    #     else:
    #         return err


if __name__ == '__main__':
    mutation = Mutation()
    mutation.kill_mutants()
