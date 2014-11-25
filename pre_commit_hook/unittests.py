from __future__ import print_function
import argparse
import os

from fabric.api import local


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--run-cmd')
    args = parser.parse_args(argv)
    result = local(args.run_cmd)
    return result.return_code

if __name__ == '__main__':
    exit(main())
