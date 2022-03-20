#!/usr/bin/env python3

# IMPORTANT! for any changes here the docker image (docker-registry.ebrains.eu/tc/cwl-workflows/psd_workflow_visualization) has to be updated

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# function that plots the PSDs for selected channels of a signal together
def visualization(input_file, channels, output_file):
    fig, ax = plt.subplots(figsize=(12,6))
    labs = []
    df = pd.read_json(input_file)
    print(df.loc[df['ch']==0]['pxx'].values[0][0])
    for ch in channels:
        ax.plot(df.loc[df['ch']==ch]['f'].values[0], np.log(df.loc[df['ch']==ch]['pxx'].values[0]), label='ch '+ str(ch))
    ax.set_xscale('log')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('log (pxx)')
    ax.legend()
    plt.show()
    plt.savefig(output_file)

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='file containing psd analysis results')
parser.add_argument('--output_file', default='out.png', help='file where output plot should be written')
parser.add_argument('--channels', nargs="+", type=int, metavar='ch', help='selected signal channels')
args = parser.parse_args()

# PSD visualization
visualization(args.input_file, args.channels, args.output_file)
