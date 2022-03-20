#!/usr/bin/env python3

# IMPORTANT! for any changes here the docker image (docker-registry.ebrains.eu/tc/cwl-workflows/psd_workflow_analysis) has to be updated

import argparse
import numpy as np
import pandas as pd
import scipy.io as sio
import scipy.signal
import neo

# function that computes the PSD (Power Spectral Density) for every selected channel in the signal
def analysis(input_file, channels, output_file):
    signal = read_smr(input_file)
    samp_freq = signal['Fs'][0]
    df_psd = pd.DataFrame(columns=['f', 'pxx', 'ch'])
    for i,ch in enumerate(channels):
        print('Performing analysis (' + str(i+1) + '/' + str(len(channels)) + ')')
        f, pxx = scipy.signal.welch(x=signal['value'][ch,:], fs=samp_freq, nperseg=2*samp_freq, nfft=10*samp_freq)
        df_psd = df_psd.append({'f': f, 'pxx':pxx, 'ch':ch}, ignore_index=True)
    df_psd.to_json(output_file)
    print('Analysis completed, results saved to', output_file)

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='file where the signal is stored')
parser.add_argument('--output_file', default='psd.json', help='file where the analysis results should be written')
parser.add_argument('--channels', nargs="+", type=int, metavar='ch', help='selected signal channels')
args = parser.parse_args()



def read_smr(filename):
    reader = neo.io.Spike2IO(filename=filename, try_signal_grouping=False)
    Raw_Data = reader.read(lazy=False)[0]
    samp_freq = float(Raw_Data.segments[0].analogsignals[0].sampling_rate)
    num_chs = len(Raw_Data.segments[0].analogsignals)
    channel_labels = [Raw_Data.segments[0].analogsignals[idx].array_annotations['channel_names'][0] for idx in range(num_chs)]
    samples_number = np.min([len(Raw_Data.segments[0].analogsignals[idx].magnitude) for idx in range(num_chs)])
    X = np.zeros((num_chs, samples_number), dtype=np.float32)
    for i in range(num_chs):
        X[i,:] = Raw_Data.segments[0].analogsignals[i].magnitude.T[0][:samples_number]
    signal = {'value': X, 'Fs': [samp_freq]}
    return signal

# perform analysis
analysis(args.input_file, args.channels, args.output_file)
