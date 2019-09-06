import argparse

__author__ = "yth2012"

parser = argparse.ArgumentParser(description="parser test", usage="for fun")

parser.add_argument("-n", dest="numof", type=int, help="number of input", default=5)
parser.add_argument("values", type=int, nargs='*')  ### nargs number of arg to be cosumed  '?':0 or 1  '*': all
parser.add_argument("-v", action="count")
excgrp = parser.add_mutually_exclusive_group()
excgrp.add_argument("-t", action="store_true")
excgrp.add_argument("-f", action="store_true")
excgrp.add_argument("-w", action="store_false")

args = parser.parse_args()
if args.v:
    print("v level: {}".format(args.v))

if len(args.values) > args.numof:
    print("too many values")

if args.t:
    print("t")
elif args.f:
    print("f")
elif args.w:
    print("w")





