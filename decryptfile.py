#!/usr/bin/python3.6
# _*_ coding: utf-8 _*_
"""
SYNOPSIS
    To test the use of module argparse

DESCRIPTION

    Decrypt a file using openssl

EXAMPLES

    decryptfile.py <input file> <output encrypted file>

EXIT STATUS

    No exit status

AUTHOR

    Phil Kershaw <pkershaw0@gmail.com>

"""
#
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Encrypt a file')
parser.add_argument('input_file', type=str, help='Name of file to decrypt')
parser.add_argument('output_file', type=str, help='Name of decrypted file')
args = parser.parse_args()

if __name__ == '__main__':
    subprocess.run(["openssl", "aes-256-cbc", "-d", "-salt", "-pbkdf2", "-in", args.input_file, "-out", args.output_file])
