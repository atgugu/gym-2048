"""Smooth reward values by lambda"""

from __future__ import print_function

import argparse

import training_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', default='data.csv', help="Set the output file name")
    parser.add_argument('--llambda', default=0.9, help="Decay value for rewards")
    parser.add_argument('input', help="Specify the input file name")
    args = parser.parse_args()

    data = training_data.training_data()
    data.import_csv(args.input)
    data.smooth_rewards(args.llambda)
    data.export_csv(args.output)
