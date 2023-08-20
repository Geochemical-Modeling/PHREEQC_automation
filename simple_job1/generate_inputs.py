"""
    generate_inputs.py
    ~~~~~~~~~~~~~~~~~~
    generate inputs for simple_job1
    
    output:
        -- 140 input files
        -- one csv file with modification information

"""

import os
import re
import sys


def replace_solution():
    """replace solution in template file with new solution"""
    pass


def update_parameters():
    """update parameters in template file with new parameters"""
    pass


def split_on_empty_lines(s: str) -> list:

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

def read_sections(textfile: str) -> list:
    try:
        with open(textfile, "r", encoding="utf-8") as file:
            lines = file.read()
        # split file into different sections by the empty line
        sections = split_on_empty_lines(lines)
        return sections
    except FileNotFoundError:
        print(f"File not found: {textfile}")
        return None


def workflow(basefile):
    """generate inputs for simple_job1"""
    sections = read_sections(basefile)
    print(f'Total sections: {len(sections)}')


def main():
    basefile = "Beerling_Clean_V2.pqi"
    workflow(basefile=basefile)


if __name__ == "__main__":
    main()
