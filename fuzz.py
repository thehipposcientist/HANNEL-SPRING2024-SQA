import os
import datetime
import subprocess
import random

from mining.git.repo.miner import makeChunks, getPythonCount, cloneRepo
from mining.mining import getPythonFileCount, days_between

def fuzz_functions():
    # Fuzz days_between function
    random_date1 = datetime.datetime.now()
    random_date2 = random_date1 + datetime.timedelta(days=random.randint(-365, 365))
    result = days_between(random_date1, random_date2)
    print(f"Fuzzing days_between with inputs: {random_date1}, {random_date2}. Result: {result}")

    # Fuzz getPythonFileCount function
    path = os.getcwd()  # Assuming the current directory
    result = getPythonFileCount(path)
    print(f"Fuzzing getPythonFileCount with path: {path}. Result: {result}")

    # Fuzz makeChunks function
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    chunk_size = random.randint(1, len(sample_list))
    result = list(makeChunks(sample_list, chunk_size))
    print(f"Fuzzing makeChunks with list: {sample_list}, chunk size: {chunk_size}. Result: {result}")

    # Fuzz getPythonCount function
    result = getPythonCount(path)
    print(f"Fuzzing getPythonCount with path: {path}. Result: {result}")

    # Fuzz cloneRepo function
    repo_name = "https://github.com/example/example_repo.git"  # Example repo URL
    target_dir = "cloned_repo"  # Example target directory
    cloneRepo(repo_name, target_dir)
    print(f"Fuzzing cloneRepo with repo name: {repo_name}, target directory: {target_dir}.")

if __name__ == "__main__":
    fuzz_functions()