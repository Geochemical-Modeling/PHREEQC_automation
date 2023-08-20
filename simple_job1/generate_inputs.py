"""
    generate_inputs.py
    ~~~~~~~~~~~~~~~~~~
    generate inputs for simple_job1
    
    output:
        -- 140 input files
        -- one csv file with modification information

"""

def replace_solution():
    """replace solution in template file with new solution"""
    pass

def update_parameters():
    """update parameters in template file with new parameters"""
    pass

def read_sections (textfile: str) -> list:

    try:
        with open(textfile, "r",encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"File not found: {textfile}")
        return None

def workflow(basefile):
    """generate inputs for simple_job1"""
    sections = read_sections(basefile)
    print(sections)

def main():
    basefile = "Beerling_Clean_V2.pqi"
    workflow(basefile = basefile)

if __name__ == '__main__':
    main()


