#!/usr/bin/env python3
import sys

prodcategory_key = None
current_total = 0.0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    key, value = line.split('\t')

    try:
        value = float(value)
    except ValueError:
        continue

    if prodcategory_key == key:
        current_total += value
    else:
        if prodcategory_key is not None:
            print(f"{prodcategory_key}\t{current_total}")

        prodcategory_key = key
        current_total = value


if prodcategory_key is not None:
    print(f"{prodcategory_key}\t{current_total}")
