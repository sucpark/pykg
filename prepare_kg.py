import os
import json
import pickle
import argparse
from pathlib import Path
from pandas import read_csv
from utils import preprocess_df, split_df

parser = argparse.ArgumentParser(description='Prepare development knowledge base')
parser.add_argument('--data_dir', type='str', help='Directory containing raw data')
parser.add_argument('--save_dir', type='str', help='Directory to save the data')
parser.add_argument('--data', type='str', help='Dataset name')
parser.add_argument('--validation', type=bool, default=True, help='Determine to create validation set')

if __name__ == '__main__':
    args = parser.parse_args()
    data_dir = Path(args.data_dir)
    save_dir = Path(args.data_dir)

    if args.data == '10000recipe_sample1000.txt':
        data = read_csv(data_dir / args.data, sep='\t', names=['head', 'relation', 'tail'])
        data = preprocess_df(data)
        train, valid, test = split_df(share=0.8, validation=args.validation)
        train.to_csv(save_dir, 'train.txt', sep='\t')
        test.to_csv(save_dir, 'test.txt', sep='\t')
        if valid is not None:
            valid.to_csv(save_dir, 'valid.txt', sep='\t')
