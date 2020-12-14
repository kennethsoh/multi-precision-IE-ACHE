#!/usr/bin/python3
import os
import sys

#filename = str(input("C File name with extension: "))
#filestriped = filename[:-2]

#os.system(f"g++ {filename} -o {filestriped} -ltfhe-spqlios-fma")

print("Compiling process, alice, cloud and verif files")
os.system(f"g++ process.c -o process -ltfhe-spqlios-fma")
os.system(f"g++ keygen.c -o keygen -ltfhe-spqlios-fma")
os.system(f"g++ alice.c -o alice -ltfhe-spqlios-fma")
os.system(f"g++ cloud.c -o cloud -ltfhe-spqlios-fma")
os.system(f"g++ verif.c -o verif -ltfhe-spqlios-fma")
