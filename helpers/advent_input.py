import argparse


class AdventInput:
    """ Class to import advent of code
        input files so they are easier
        to work with
    """

    def __init__(self, input_path) -> None:
        self.input_path = input_path
        self.fp = open(self.input_path, "r")

    def next_line(self):
        yield self.fp.readline()

    def all_lines(self):
        return self.fp.read().splitlines()

    def reset_input(self):
        self.fp.close()
        self.fp = open(self.input_path, "r")


class Parser:

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="Advent of code text file input"
        )
        self.parser.add_argument("input_file",
                                 type=str,
                                 help="Path to advent of code input")

    def get_args(self):
        return self.parser.parse_args()