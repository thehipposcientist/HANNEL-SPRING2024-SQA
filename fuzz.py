import os
import datetime
import subprocess
import random
import csv

from mining.mining import getPythonFileCount, days_between, cloneRepo, checkPythonFile

def write_bug_to_csv(func_name, bug_info):
    with open('fuzz_report.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([func_name, bug_info])

def fuzz_functions():
    # Fuzz days_between function
    random_date1 = datetime.datetime.now()
    random_date2 = random_date1 + datetime.timedelta(days=random.randint(-365, 365))
    try:
        result = days_between(random_date1, random_date2)
        print(f"Fuzzing days_between with inputs: {random_date1}, {random_date2}. Result: {result}")
    except Exception as e:
        print(f"Bug found in days_between function: {e}")
        write_bug_to_csv('days_between', str(e))

    # Fuzz getPythonFileCount function
    path = os.getcwd()  # Assuming the current directory
    try:
        result = getPythonFileCount(path)
        print(f"Fuzzing getPythonFileCount with path: {path}. Result: {result}")
    except Exception as e:
        print(f"Bug found in getPythonFileCount function: {e}")
        write_bug_to_csv('getPythonFileCount', str(e))

    # Fuzz cloneRepo function
    repo_name = "https://github.com/example/example_repo.git"  # Your repository URL
    target_dir = "repo_clone"  # Target directory to clone the repository
    try:
        cloneRepo(repo_name, target_dir)
        print(f"Cloning repository {repo_name} to {target_dir}...")
    except Exception as e:
        print(f"Bug found in cloneRepo function: {e}")
        write_bug_to_csv('cloneRepo', str(e))

    # Fuzz checkPythonFile function
    path2dir = "."  # Path to the directory to check Python files
    try:
        result = checkPythonFile(path2dir)
        print(f"Fuzzing checkPythonFile with path: {path2dir}. Result: {result}")
    except Exception as e:
        print(f"Bug found in checkPythonFile function: {e}")
        write_bug_to_csv('checkPythonFile', str(e))

def makeChunks(the_list, size_):
    for i in range(0, len(the_list), size_):
        yield the_list[i:i+size_]

if __name__ == "__main__":
    fuzz_functions()
