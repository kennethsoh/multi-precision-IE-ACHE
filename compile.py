#!/usr/bin/python3
import os
import sys

filename = str(input("C File name with extension: "))
filestriped = filename[:-2]

os.system(f"g++ {filename} -o {filestriped} -ltfhe-spqlios-fma")
