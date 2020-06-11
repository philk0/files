#!/usr/bin/python3.6
# _*_ coding: utf-8 _*_
"""

SYNOPSIS
    
    Simple FizzBuzz Challenger

DESCRIPTION

    This script prints out a sequence of numbers from a provided range with the following instructions:
    - if the number is divisible by 3, then print out "fizz"
    - if the number is divisible by 5, then print out "buzz"
    - if the number is divisible 3 and 5, then print out "fizzbuzz"
    - else print out the number.
"""


import sys
import argparse


class CustomFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass


parser = argparse.ArgumentParser(description=sys.modules[__name__].__doc__, formatter_class=CustomFormatter)
parser.add_argument('lower', type=int, help='lower number for range')
parser.add_argument('upper', type=int, help='Upper number for range')
g = parser.add_argument_group('fizzbuzz settings')
g.add_argument('--fizz',
               metavar='value',
               default=3,
               type=int,
               help='Modulo value for fizz')
g.add_argument('--buzz',
               metavar='value',
               default=5,
               type=int,
               help='Modulo value for buzz')
args = parser.parse_args()


for n in range(int(sys.argv[1]), int(sys.argv[2])):
    if n % args.fizz == 0 and n % args.buzz == 0:
        print('FizzBuzz')
    elif n % args.fizz == 0:
        print('Fizz')
    elif n % args.buzz == 0:
        print('Buzz')
    else:
        print(n)
