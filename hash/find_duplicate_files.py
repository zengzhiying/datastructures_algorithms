#!/usr/bin/env python3
# coding=utf-8
import os
import hashlib

SRC_PREFIX = 8192
SCAN_PATH = 'abc'

def md5(src: bytes) -> bytes:
    m = hashlib.md5()
    m.update(src)
    return m.digest()

def get_file_hash(path):
    with open(path, 'rb') as f:
        src = f.read(SRC_PREFIX)
    return md5(src)

if __name__ == '__main__':
    scan_files = os.listdir(SCAN_PATH)
    print(f"number of files: {len(scan_files)}")

    hash_by_path = {}

    for filename in scan_files:
        file_path = os.path.join(SCAN_PATH, filename)
        if not os.path.isfile(file_path):
            continue
        value = get_file_hash(file_path)
        if value in hash_by_path:
            print(f"duplicated file: {hash_by_path[value]} -> {file_path}")
            hash_by_path[value].append(file_path)
            continue
        hash_by_path[value] = [file_path]

