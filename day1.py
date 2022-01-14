#!/usr/bin/env python3
""" Day 1: Sonar Sweep

    Summary: Count the number of times a depth
        measurement increases from the previous
        measurement.

    Description: Given a list of depths, count the
        number of times a depth measurement increases.

        Only need to return the number of measurements
        that are larger than the previous.

    Author: Thisara Wijesundera
"""
from __future__ import annotations

import argparse
import os.path
import pathlib


def part1(measurements: 'Path') -> int:
    """Count the number of time a depth
    measurements increases from the previous
    measurement.

    Parameters
    ----------
    measurements : Path
        Path to file containing all
        measurements.

    Returns
    -------
    increases : int
        Count of time mesurement incereases from the
        previous measurement.
    """
    increases = 0

    with open(measurements, "r", encoding="utf-8") as measure:
        previous = 0

        for line in measure:
            if previous == 0:
                previous = int(line)
            if int(line) > previous:
                increases += 1
            previous = int(line)

    return increases


def part2(measurements: 'Path') -> int:
    increases = 0
    with open(measurements, "r", encoding="utf-8") as measure:
        all_measurements = list(map(int, measure.readlines()))
        previous_sum = 0

        for line_num in range(len(all_measurements) - 3):
            if previous_sum == 0:
                previous_sum = sum(all_measurements[line_num:line_num+4])
            if sum(all_measurements[line_num:line_num+4]) > previous_sum:
                increases += 1
            previous_sum = sum(all_measurements[line_num:line_num+4])

    return increases



def is_file(path: str):
    if not os.path.exists(path):
        argparse.ArgumentError(f"Unable to find file {path}")
    else:
        return pathlib.Path(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Given a list of measurements,
        return the number of times the deapth measurement increases"""
    )
    parser.add_argument("measurements",
                        metavar="<measurements_file>",
                        type=is_file,
                        help="Path to measurements.txt file")
    args = parser.parse_args()

    print(part1(args.measurements))
    print(part2(args.measurements))