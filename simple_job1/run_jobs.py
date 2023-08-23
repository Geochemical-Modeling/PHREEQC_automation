"""
    run_jobs.py
    -- run jobs with multiprocessing
"""

import  argparse

def main():
    parser = argparse.ArgumentParser(description="Run jobs in batch.")
    parser.add_argument(dest="job_cfg", type=str, help="job configuration")
    parser.add_argument("-d","--dryrun",action="store_true",help="test with a dryrun")
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()