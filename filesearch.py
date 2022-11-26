#pip install fuzzywuzzy
#pip install python-Levenshtein

import os
from fuzzywuzzy import fuzz

root_dir = input("Enter the root directory for your search: ")
file_type = input("Enter the file endings to look for (Separate by spaces) (Empty = All): ")
fuzzy_search = input ("Enter a fuzzy search query (Empty = None): ")

file_types = file_type.split(" ")

for root, dirs, files in os.walk(root_dir):
    for name in files:
        if name.endswith(tuple(ft for ft in file_types)) or file_types[0] == "":
            if fuzz.token_sort_ratio(fuzzy_search.lower(), name.lower()) > 50 or fuzzy_search == "":
                print(root + os.sep + name)