#!/usr/bin/python3.6
# _*_ coding: utf-8 _*_
"""
SYNOPSIS
    To test the use of module argparse

DESCRIPTION

    Encrypt a file using openssl and give the option to delete the original

EXAMPLES

    encryptfile.py <input file> <output encrypted file> <-d optional delete input file flag>

EXIT STATUS

    No exit status

AUTHOR

    Phil Kershaw <pkershaw0@gmail.com>

"""
#
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Encrypt a file')
parser.add_argument('input_file', type=str, help='Name of file to encrypt')
parser.add_argument('output_file', type=str, help='Name of encrypted file')
parser.add_argument('-d', '--delete', action='store_true', help='use this flag if you want to delete original file')
args = parser.parse_args()

if __name__ == '__main__':
    subprocess.run(["openssl", "aes-256-cbc", "-salt", "-pbkdf2", "-in", args.input_file, "-out", args.output_file])
    if args.delete:
        subprocess.run(["rm", args.input_file])
    else:
        print('Original file not deleted!')
