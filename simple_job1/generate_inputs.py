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
import itertools

def find_section(sections :list, search_str: str) -> int:
    """find section position by search string"""

    for index, element in enumerate(sections):
        if element.startswith(search_str):
            return index
    # not found, just return None
    return None

def replace_solution(basefile: str, header :str, solution_file: str) -> str:
    """replace solution in template file with new solution"""
    
    sections = read_sections(basefile)
    print(f'Total sections: {len(sections)}')
    inx = find_section(sections, header)
    print(f'{header} is found at {inx}')
    with open(solution_file,"r",  encoding="utf-8") as file:
        solution_replace = file.read()
    sections[inx] = solution_replace
    newbasefile = basefile.split(".")[0] + "_" + header.replace(" ", "_") + ".pqi"
    with open(newbasefile, "w",  encoding="utf-8") as file:
        newtext = os.linesep.join(sections)
        file.write(newtext)
        file.write(os.linesep)
    
    # check the sections of new base file
    sections = read_sections(newbasefile)
    print(f'Total sections in new basefile: {len(sections)}')

    return newbasefile


def update_parameters():
    """update parameters in template file with new parameters"""
    pass


def split_on_empty_lines(s: str) -> list:
    """split into sections by empty lines"""
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

def read_sections(textfile: str) -> list:
    """read file into sections"""
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

    # step 1: replace solution, and generate a new base file
    second_basefile = replace_solution(basefile, "SOLUTION 0","SOLUTION_0.txt")
    print(second_basefile)
    all_files = [basefile]
    all_files.append(second_basefile)

    # step 2: generate all combination of parameters
    # three parameters
    # temperature
    para_temp = list(range(5, 40, 5))
    para_shifts = list(range(100, 550, 50))
    # Shifts*Time_Step = 157824904.4 s
    # para_time_step
    print(para_temp)
    print(para_shifts)
    listOLists = [para_temp, para_shifts]
    para_combines = itertools.product(*listOLists)
    all_para = []
    for entry in para_combines:
        shifts = entry[1]
        time_step = 157824904.4/entry[1]
        all_para.append([entry[0],shifts,time_step])
    print(f'Number of para combinations: {len(all_para)}')

    # step 3: replace parameters in each base file

def main():
    basefile = "Beerling_Clean_V2.pqi"
    workflow(basefile=basefile)


if __name__ == "__main__":
    main()
