import argparse
from pathlib import Path
from pandas import read_csv
from os import makedirs
from os.path import exists
from utils import preprocess_df, split_df

parser = argparse.ArgumentParser(description='Prepare development knowledge base')
parser.add_argument('--data_dir', default='raw_data', type=str, help='Directory containing raw data')
parser.add_argument('--save_dir', default='dataset', type=str, help='Directory to save the data')
parser.add_argument('--dataset', type=str, help='Dataset name')
parser.add_argument('--validation', type=bool, default=True, help='Determine to create validation set')

if __name__ == '__main__':
    args = parser.parse_args()
    data_dir = Path(args.data_dir)
    save_dir = Path(args.save_dir)

    if args.dataset == '10000recipe_sample1000.txt':
        save_dir = save_dir / '10000Recipe_sample1000'
        data_prefix = '10000recipe_1000_'
        data = read_csv(data_dir / args.dataset, sep='\t', names=['head', 'relation', 'tail'])
        data = preprocess_df(data)
        train, valid, test = split_df(df=data, share=0.8, validation=args.validation)

    if not exists(save_dir):
        makedirs(save_dir, exist_ok=True)

    train.to_csv(save_dir / (data_prefix + 'train.txt'), sep='\t', index=False, header=False)
    test.to_csv(save_dir / (data_prefix + 'test.txt'), sep='\t', index=False, header=False)
    if valid is not None:
        valid.to_csv(save_dir / (data_prefix + 'valid.txt'), sep='\t', index=False, header=False)
