"""
    batch_run.py
    -- run jobs with multiprocessing

    the job configuration file
    test.cfg
    ----------------
    [jobs]
    jobname: "a name for the job"
    jobrundir: "the output location to the job"
    database: "database file"
    inputs: "the folder with the list of input file"
    
    [phreeqc]
    phreeqcexe: "path to phreeqcexe"
    ----------------
    The folder structure:
    jobrundir/
        .logfile
        -- job1
        -- job2
        ...
"""

import os
import sys
import argparse
import configparser
import shutil

def cfg_to_dict(cfgfile):
    """load cfg file to dictionary"""

    config_object = configparser.ConfigParser()
    try:
        with open(cfgfile, "r") as file:
            config_object.read_file(file)
    except FileNotFoundError:
        print(f"{cfgfile} is not found!")
        sys.exit()
    output_dict = {s:dict(config_object.items(s)) for s in config_object.sections()}
    return output_dict

def prepare_jobs(jobcfg_dict):
    """setup job folders and copy files"""

    jobfolder = jobcfg_dict["jobs"]["jobrundir"]
    if os.path.exists(jobfolder):
        shutil.rmtree(jobfolder)
        print(f"clean run, {jobfolder} is deleted")
    
    os.makedirs(jobfolder, exist_ok = True)
    print(f"setup run folder: {jobfolder}")

    # get the list of input file
    input_dir = jobcfg_dict['jobs']['inputs']
    input_pqi = [x for x in os.listdir(input_dir) if ".pqi" in x ]
    print(input_pqi)

    # copy files over
    for entry in input_pqi:
        input_name = entry.split(".")[0]
        subfolder = os.path.join(jobfolder,input_name)
        if os.path.exists(subfolder):
            print(subfolder)
            shutil.rmtree(subfolder)
        else:    
            os.makedirs(subfolder, exist_ok = True)
        # copy file
        # input.qpi, phreeqcexe, database
        files_to_copy =[os.path.join(input_dir, entry), jobcfg_dict['phreeqc']['phreeqcexe'],jobcfg_dict['jobs']['database']]
        for file in files_to_copy:
            print(file)
            shutil.copy(file, subfolder)
        

def run_jobs(jobcfg, dryrun):
    """run jobs with a configuration file"""
    print("configuration file: ",jobcfg)
    print("dryrun ? ", dryrun)

    jobcfg_dict = cfg_to_dict(jobcfg)
    print(jobcfg_dict)
    prepare_jobs(jobcfg_dict)    

def main():
    parser = argparse.ArgumentParser(description="Run jobs in batch.")
    parser.add_argument(dest="job_cfg", type=str, help="job configuration")
    parser.add_argument("-d","--dryrun",action="store_true",help="test with a dryrun")
    args = parser.parse_args()
    run_jobs(args.job_cfg, args.dryrun)

if __name__ == "__main__":
    main()