import os
import glob
import sys

arg1 = input("Enter name of the folder with the photos in that you wish to rename:\n ")
arg2 = input("Enter name prefix for photos in the folder (e.g. HONGKONG2000) \n: ")
counter = 0

for filename in os.listdir(arg1):
    print(filename)
    extension = os.path.splitext(filename)[1]
    new_name_with_ext = arg2 + "-" + str(counter) + extension
    print(new_name_with_ext)
    os.rename(os.path.join(arg1,filename),os.path.join(arg1, new_name_with_ext))
    counter += 1
    print('----------------')

print("Finished. Press any key to exit.")
input()