import os
import datetime
import subprocess
import random
import csv

# Direct import of specific functions
import imp
makeChunks = imp.load_source("makeChunks", "miner/git.repo.miner.py")
getPythonCount = imp.load_source("getPythonCount", "miner/git.repo.miner.py")
cloneRepo = imp.load_source("cloneRepo", "miner/git.repo.miner.py")

from mining.mining import getPythonFileCount, days_between

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

    # Fuzz makeChunks function
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    chunk_size = random.randint(1, len(sample_list))
    try:
        result = list(makeChunks(sample_list, chunk_size))
        print(f"Fuzzing makeChunks with list: {sample_list}, chunk size: {chunk_size}. Result: {result}")
    except Exception as e:
        print(f"Bug found in makeChunks function: {e}")
        write_bug_to_csv('makeChunks', str(e))

    # Fuzz getPythonCount function
    try:
        result = getPythonCount(path)
        print(f"Fuzzing getPythonCount with path: {path}. Result: {result}")
    except Exception as e:
        print(f"Bug found in getPythonCount function: {e}")
        write_bug_to_csv('getPythonCount', str(e))

    # Fuzz cloneRepo function
    repo_name = "https://github.com/example/example_repo.git"  # Example repo URL
    target_dir = "cloned_repo"  # Example target directory
    try:
        cloneRepo(repo_name, target_dir)
        print(f"Fuzzing cloneRepo with repo name: {repo_name}, target directory: {target_dir}.")
    except Exception as e:
        print(f"Bug found in cloneRepo function: {e}")
        write_bug_to_csv('cloneRepo', str(e))

if __name__ == "__main__":
    fuzz_functions()
