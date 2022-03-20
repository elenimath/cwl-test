#!/usr/bin/env cwltool

cwlVersion: v1.0
class: Workflow

inputs:
  input_file: File
  channels: int[]
  psd_output_file_name: string
  output_file_name: string

outputs:
  intermediate_output:
    type: File
    outputSource: analysis/output_file
  final_output:
    type: File
    outputSource: visualization/plot

steps:
  analysis:
    run: step1/analysis_tool.cwl
    in:
      input_file: input_file
      output_file_name: psd_output_file_name
      channels: channels
    out: [output_file]

  visualization:
    run: step2/visualization_tool.cwl
    in:
      input_file: analysis/output_file
      output_file_name: output_file_name
      channels: channels
    out: [plot]
