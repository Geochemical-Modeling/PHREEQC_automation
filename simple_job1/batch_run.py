"""
    batch_run.py
    -- run jobs with multiprocessing
"""

import  argparse

def run_jobs(jobcfg, dryrun):
    """run jobs with a configuration file"""
    print("configuration file: ",jobcfg)
    print("dryrun ? ", dryrun)

def main():
    parser = argparse.ArgumentParser(description="Run jobs in batch.")
    parser.add_argument(dest="job_cfg", type=str, help="job configuration")
    parser.add_argument("-d","--dryrun",action="store_true",help="test with a dryrun")
    args = parser.parse_args()
    run_jobs(args.job_cfg, args.dryrun)

if __name__ == "__main__":
    main()