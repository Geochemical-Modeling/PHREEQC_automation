"""
    generate_inputs.py
    ~~~~~~~~~~~~~~~~~~
    generate inputs for simple_job1
    
    output:
        -- 140 input files
        -- one csv file with modification information

"""

import csv
import itertools
import os
import re
import sys


def find_section(sections: list, search_str: str) -> int:
    """find section position by search string"""

    for index, element in enumerate(sections):
        if element.startswith(search_str):
            return index
    # not found, just return None+_
    return None


def replace_solution(basefile: str, header: str, solution_file: str) -> str:
    """replace solution in template file with new s
    olution"""

    sections = read_sections(basefile)
    print(f"Total sections: {len(sections)}")
    inx = find_section(sections, header)
    print(f"{header} is found at {inx}")
    with open(solution_file, "r", encoding="utf-8") as file:
        solution_replace = file.read()
    sections[inx] = solution_replace
    newbasefile = basefile.split(".")[0] + "_" + header.replace(" ", "_") + ".pqi"
    with open(newbasefile, "w", encoding="utf-8") as file:
        newtext = os.linesep.join(sections)
        file.write(newtext)
        file.write(os.linesep)

    # check the sections of new base file
    sections = read_sections(newbasefile)
    print(f"Total sections in new basefile: {len(sections)}")

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

def modify_rate_line_for_mineral(content, mineral, multiplier):
    """
    Modify the rate line within a mineral block in the content by applying a multiplier
    to the (1-SR("mineral name")) part of its rate equation.
    """
    # Pattern to find the rate line that ends with (1-SR("mineral"))
    rate_line_pattern = re.compile(rf'(rate = .*?\(1-SR\("{mineral}"\)\))')
    # Search and replace the rate line with the modified one including the multiplier
    def replace_rate_line(match):
        # Extract the original rate line from the match
        original_rate_line = match.group(1)
        # Append the multiplier to the (1-SR("mineral")) part
        modified_rate_line = f"{original_rate_line}*{multiplier}"
        return modified_rate_line

    # Replace the rate line in the content using the pattern and replacement function
    modified_content = rate_line_pattern.sub(replace_rate_line, content)
    return modified_content



def workflow(basefile):
    # Define parameters and multipliers
    para_names = ["temp", "shifts", "time_step"]
    para_temp = list(range(5, 40, 5))
    para_shifts = list(range(100, 550, 50))
    minerals = ["MikeSorghum", "Quartz", "Plagioclase", "Apatite", "Diopside_Mn", "Diopside", "Olivine", "Alkali-feldspar", "Montmorillonite", "Ilmenite", "Glass"]
    multipliers = [0.01, 0.1, 1, 10, 100]
    base_files = [basefile, replace_solution(basefile, "SOLUTION 0", "SOLUTION_0.txt")]  # Assuming replace_solution returns a filename

    # Calculate the total number of simulations
    total_simulations = len(para_temp) * len(para_shifts) * len(minerals) * len(multipliers) * len(base_files)
    print(f"Total simulations to be generated: {total_simulations}")


    jobs_folder = "jobs"
    os.makedirs(jobs_folder, exist_ok=True)

    summary = []
    count = 1

    for basefile_path in base_files:
        with open(basefile_path, "r", encoding="utf-8") as file:
            base_content = file.read()

        # Generate all combinations of parameters
        para_combines = itertools.product(para_temp, para_shifts, minerals, multipliers)
        for temp, shifts, mineral, multiplier in para_combines:
            time_step = 157824904.4 / shifts
            modified_content = modify_rate_line_for_mineral(base_content, mineral, multiplier)
            para_values = [str(temp), str(shifts), "{:.3f}".format(time_step)]

            # Replace parameters in the modified content
            for name, value in zip(para_names, para_values):
                modified_content = re.sub(rf"{name}\s+(\d+(?:\.\d+)?)", f"{name}  {value}", modified_content)

            # Save the modified content to a new file
            jobname = f"job{str(count).zfill(3)}_{mineral}_{multiplier}.pqi"
            filepath = os.path.join(jobs_folder, jobname)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(modified_content)
            summary.append([jobname, basefile_path] + para_values + [mineral, str(multiplier)])
            count += 1

    # Write summary to CSV
    with open("job_summary.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["input_file", "base_file", "temp", "shifts", "time_step", "mineral", "multiplier"])
        writer.writerows(summary)


def main():
    basefile = "Beerling_Clean_V3.pqi"
    workflow(basefile=basefile)


if __name__ == "__main__":
    main()
