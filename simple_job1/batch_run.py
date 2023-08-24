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
    copyexe: True
    ----------------
    The folder structure:
    jobrundir/jobname
        .logfile
        -- job1
        -- job2
        ...
"""

import os
import sys
import argparse
import configparser

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

def run_jobs(jobcfg, dryrun, cleanrun):
    """run jobs with a configuration file"""
    print("configuration file: ",jobcfg)
    print("dryrun ? ", dryrun)
    print("clean run ?", cleanrun)

    jobcfg_dict = cfg_to_dict(jobcfg)
    print(jobcfg_dict)
    


def main():
    parser = argparse.ArgumentParser(description="Run jobs in batch.")
    parser.add_argument(dest="job_cfg", type=str, help="job configuration")
    parser.add_argument("-d","--dryrun",action="store_true",help="test with a dryrun")
    parser.add_argument("-c","--cleanrun",action="store_true",help="start over, clean run")
    args = parser.parse_args()
    run_jobs(args.job_cfg, args.dryrun, args.cleanrun)

if __name__ == "__main__":
    main()