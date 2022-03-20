# PSD (Power Spectral Density) Calculation Workflow

This is a CWL workflow consisting of 2 steps (tools).

#### Step 1: analysis_tool.cwl (analysis.py)
calculates the PSD (Power Spectral Density) of all the selected channels of a signal

input:
- input file containing a .smr file found in Knowledge Graph (location link in Object Storage at CSCS)
- output file preferred name
- output file (plot) preferred name
- selected channels

output:
- produced plot


#### Step 2: visualization_tool.cwl (visualization.py)

plots the PSDs for selected channels of a signal together

input:
- input file containing the PSDs
- output file (plot) preferred name
- selected channels

output:
- produced plot
