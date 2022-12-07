import shutil
from os import listdir, path
from distutils.dir_util import copy_tree
import subprocess

android_path = "../../../Experiment/ShiftCal"
src_main_path = path.join(android_path, "app", "src", "main")
# shutil.rmtree(src_main_path)
mutant_path = "Mutant_ShiftCal"

mutants = [m for m in listdir(mutant_path) if "log" not in m]

t = path.join(mutant_path, mutants[0])
print(t)

copy_tree(t, src_main_path)

test_command = android_path + "/gradlew jacocoTestReportDebug"
print(test_command)

def test_command_result():
    process = subprocess.Popen(test_command, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process


with test_command_result():
    for line in test_command_result().stdout:
        print(line)
