import os
import json
import pickle
import argparse
from pathlib import Path
from pandas import read_csv

parser = argparse.ArgumentParser(description='Prepare development knowledge base')
parser.add_argument('--data_dir', type='str', help='Directory containing raw data')
parser.add_argument('--save_dir', type='str', help='Directory to save the data')
parser.add_argument('--data', type='str', help='Dataset name')

if __name__ == '__main__':
    args = parser.parse_args()
    data_dir = Path(args.data_dir)
    save_dir = Path(args.data_dir)

    if args.data == '10000recipe_sample1000.txt':
        data = read_csv(data_dir / args.data)