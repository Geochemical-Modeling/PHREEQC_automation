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
import logging
from multiprocessing import Pool, cpu_count
import subprocess
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

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

def set_logger(apath):
    """set the job log at a path"""

    logfile = os.path.join(apath, "run.log")
    file_handler = logging.FileHandler(logfile)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

def prepare_jobs(jobcfg_dict):
    """setup job folders and copy files"""

    jobs_to_run = []
    jobfolder = jobcfg_dict["jobs"]["jobrundir"]
    if os.path.exists(jobfolder):
        shutil.rmtree(jobfolder)
        print(f"clean run, {jobfolder} is deleted")
    
    os.makedirs(jobfolder, exist_ok = True)
    print(f"setup run folder: {jobfolder}")

    set_logger(jobfolder)
    logger.info(f'log for {jobcfg_dict["jobs"]["jobname"]}')

    # get the list of input file
    input_dir = jobcfg_dict['jobs']['inputs']
    input_pqi = [x for x in os.listdir(input_dir) if ".pqi" in x ]
    print("total number of jobs: ", len(input_pqi))

    # copy files over
    for entry in input_pqi:
        input_name = entry.split(".")[0]
        subfolder = os.path.join(jobfolder,input_name)
        if os.path.exists(subfolder):
            shutil.rmtree(subfolder)
        else:    
            os.makedirs(subfolder, exist_ok = True)
        # copy file
        # input.qpi, phreeqcexe, database
        files_to_copy =[os.path.join(input_dir, entry), jobcfg_dict['phreeqc']['phreeqcexe'],jobcfg_dict['jobs']['database']]
        for file in files_to_copy:
            shutil.copy(file, subfolder)
        database= os.path.basename(jobcfg_dict['jobs']['database'])
        output = f"{input_name}.pqo"
        screenlog = f"{input_name}.log"
        # record jobs to run
        jobs_to_run.append({"folder":subfolder, "input":entry,"output":output,"database":database,"log":screenlog})

    logger.info('setup is done')    
    
    return jobs_to_run

def dryrun_task(ajob):
    """dry run a job"""

    os.chdir(ajob['folder'])
    output = subprocess.check_output(f"dir", shell=True).decode()
    time.sleep(5)
    return output

def dryrun_jobs(jobs):
    """dry run jobs"""

    pool_size = int(cpu_count()/2)
    logger.info("dry run start.")
    with Pool(pool_size) as pool:
        results = set(pool.map(dryrun_task,jobs))
    print(results)
    logger.info("dry run end.")

def phreeqc_task(ajob):
    """execute a phreeqc job"""

    os.chdir(ajob['folder'])
    exe_n = './phreeqc.exe'
    input_n = ajob['input']
    output_n = ajob['output']
    database_n = ajob['database']
    log_n = ajob['log']
    cmd = f'{exe_n} {input_n} {output_n} {database_n} {log_n}'
    exit_code = subprocess.call(cmd)
    return exit_code


def run_phreeqc_jobs(jobs):
    """run the real job"""
    pool_size = int(cpu_count()/2)
    logger.info("run start.")
    with Pool(pool_size) as pool:
        results = set(pool.map(phreeqc_task,jobs))
    print(results)
    logger.info("run end.")


def run_jobs(jobcfg, dryrun):
    """run jobs with a configuration file"""
    print("configuration file: ",jobcfg)
    print("dryrun ? ", dryrun)

    jobcfg_dict = cfg_to_dict(jobcfg)
    print(jobcfg_dict)
    jobs_list = prepare_jobs(jobcfg_dict)    
    print(jobs_list)

    if dryrun:
        dryrun_jobs(jobs_list)
    else:
        run_phreeqc_jobs(jobs_list)

def main():
    parser = argparse.ArgumentParser(description="Run jobs in batch.")
    parser.add_argument(dest="job_cfg", type=str, help="job configuration")
    parser.add_argument("-d","--dryrun",action="store_true",help="test with a dryrun")
    args = parser.parse_args()
    run_jobs(args.job_cfg, args.dryrun)

if __name__ == "__main__":
    main()