import hashlib
from tkinter import Tk, filedialog
import os.path
import ntpath


def get_File_MD5(filepath):
    f = open(filepath, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    _hash_ = md5obj.hexdigest()
    f.close()
    return str(_hash_).upper()


root = Tk()
root.withdraw()
file_path = filedialog.askopenfilenames(filetypes=[('text files', '.txt')])
md5_dictionary = {}
same = {}
test = {}
for each in file_path:
    basename = os.path.basename(each)
    file_md5 = get_File_MD5(each)
    print(basename, "的MD5值是", file_md5)
    for i in md5_dictionary.keys():
        if i == file_md5:
            same[md5_dictionary[i]] = basename
    md5_dictionary[file_md5] = basename
if same != test:
    for key, value in same.items():
        print(key, "与", value, "是一样的！")
