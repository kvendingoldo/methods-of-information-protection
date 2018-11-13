import codecs
import os
import re

# Signature file
source = raw_input('Enter the name of signature file: ')

with codecs.open(source, 'r', 'utf-8') as f:
    signature = f.read()

# Source file
source_path = raw_input('Enter the name of source file: ')

with codecs.open(source_path, 'r') as f:
    directory = f.read()

# Logic
files = [directory + '\\' + file_name for file_name in os.listdir(directory)]

result_list = []
for path in files:
    if os.path.isfile(path):
        with open(path) as f:
            if re.search(signature, f.read()):
                result_list += [path]

# Writting
result_file = raw_input('Enter the name of result file: ')

with codecs.open(result_file, 'w') as f:
    for result in result_list:
        f.write(result + '\n')