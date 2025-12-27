#!/usr/bin/env python3
import sys

paymentmethod_key = None
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

    if paymentmethod_key == key:
        current_total += value
    else:
        if paymentmethod_key is not None:
            print(f"{paymentmethod_key}\t{current_total}")

        paymentmethod_key = key
        current_total = value


if paymentmethod_key is not None:
    print(f"{paymentmethod_key}\t{current_total}")
