import os
import os.path as osp

print(os.getcwd())

text_file_path = osp.join("/var/lib/volume_dst/test.txt")

with open(text_file_path, 'a') as f:
    f.write("new_string\n")