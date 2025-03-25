import os
import shutil
from glob import glob


source_file_dir = "./evaluation_ds/"
output_file_dir = "./HardOutput/"

folder_list = sorted(glob(os.path.join(source_file_dir, "Case_*")))
print(folder_list[80:])
for i in folder_list[80:]:
    shutil.copytree(i, output_file_dir + i.split("/")[-1])