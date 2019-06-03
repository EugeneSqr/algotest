#!/usr/bin/python3
import argparse
from random import randint

DEFAULT_SEQ_LENGTH = 10
DEFAULT_SEQ_START = 0
DEFAULT_SEQ_END = 100


def print_sequence(start, end, length):
    res = ""
    for i in range(length):
        res += "%s " % randint(start, end)
    print(res)


def parse_range(range_pattern):
    rng = range_pattern.split(",")
    if len(rng) == 1:
        raise AssertionError("range pattern invalid")
    return (parse_int(rng[0], DEFAULT_SEQ_START),
            parse_int(rng[1], DEFAULT_SEQ_END))


def parse_int(number, fallback):
    try:
        return int(number)
    except ValueError:
        return fallback


parser = argparse.ArgumentParser("outputs a sequence of random integers")
parser.add_argument(
    "length",
    nargs="?",
    default=DEFAULT_SEQ_LENGTH,
    type=int,
    help="number of elements in the result sequence. "
         "Default is %s" % DEFAULT_SEQ_LENGTH)
parser.add_argument(
    "range",
    nargs="?",
    default=",",
    type=str,
    help="range pattern (e.g. -4,20 or ,0 or 0,). "
         "Default is %s,%s" % (DEFAULT_SEQ_START, DEFAULT_SEQ_END))
args = parser.parse_args()

print_sequence(
    *parse_range(args.range),
    parse_int(args.length, DEFAULT_SEQ_LENGTH))
