import pathlib
import os
import argparse
from dataclasses import dataclass

@dataclass
class Submarine:

    aim: int = 0
    horizontal: int = 0
    depth: int = 0

    def add_horizontal(self, change: int):
        self.horizontal += change
        if self.aim != 0:
            self.depth += change * self.aim

    def add_aim(self, change: int):
        self.aim += change

    def subtract_aim(self, change: int):
        self.aim -= change

    def final_answer(self):
        return self.depth * self.horizontal

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
    parser.add_argument("course",
                        metavar="<course_commands_file>",
                        type=is_file,
                        help="Path to course.txt file")
    args = parser.parse_args()

    sub = Submarine()

    with open(args.course, "r", encoding="utf-8") as commands:
        for command in commands:
            match command.split():
                case ["forward", number]:
                    sub.add_horizontal(int(number))
                case ["down", number]:
                    sub.add_aim(int(number))
                case ["up", number]:
                    sub.subtract_aim(int(number))


    print(f"Final result: {sub.final_answer()}")