#!/usr/bin/python
from __future__ import print_function
import os
import argparse

class DiskWalk(object):
    def __init__(self,path):
        self.path = os.path.expanduser(path)

    def enumerate_paths(self):

        """Returns the path to all the files in a directory as a
        list"""

        path_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                fullpath = os.path.join(dirpath,file)
                path_collection.append(fullpath)

        return path_collection

    def enumerate_paths_with_ext(self,ext):

        """Returns the path to all the files that match extension in a
        directory as a list"""

        ext = ext.lower()
        if not ext.startswith('.'):
            ext = '.' + ext
        path_collection = []
        paths = self.enumerate_paths()
        for path in paths:
            (root,ext_) = os.path.splitext(path)
            if ext == ext_.lower():
                path_collection.append(path)
        return path_collection

    def enumerate_files(self):

        """Returns all the files in a directory as a list"""

        file_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                file_collection.append(file)

        return file_collection

    def enumerate_dir(self):

        """Returns all the directories in a directory as a list"""

        dir_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dir in dirnames:
                dir_collection.append(dir)

        return dir_collection

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Directory where tracking files are located")
    parser.add_argument("-d", "--dirs", dest='dirs', default=False, action="store_true", help="enumerate directories")
    parser.add_argument("-p", "--paths", dest='paths', default=False, action="store_true", help="enumerate paths")
    parser.add_argument("-f", "--files", dest='files', default=False, action="store_true", help="enumerate files")
    parser.add_argument("-e", "--ext", dest='ext', default="", help="enumerate paths with ext")
    args = parser.parse_args()
    working_dir = args.directory

    print("Working Directory: {0}".format(working_dir))
    dw = DiskWalk(working_dir)
    if args.paths:
        print("\nRecursive listing of all paths:")
        for path in dw.enumerate_paths():
            print(path)
    if args.files:
        print("\nRecursive listing of all files:")
        for file in dw.enumerate_files():
            print(file)
    if args.dirs:
        print("\nRecursive listing of all directories:")
        for dir in dw.enumerate_dir():
            print(dir)
    if args.ext != "":
        for path in dw.enumerate_paths_with_ext(args.ext):
            print(path)
