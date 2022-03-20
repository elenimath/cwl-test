#!/usr/bin/env cwltool

cwlVersion: v1.0
class: CommandLineTool
baseCommand: visualization.py
hints:
  DockerRequirement:
    dockerPull: docker-registry.ebrains.eu/tc/cwl-workflows/psd_workflow_visualization
inputs:
  input_file:
    type: File
    inputBinding:
      position: 1
  output_file_name:
    type: string
    inputBinding:
      prefix: --output_file
      position: 2
  channels:
    type: int[]
    inputBinding:
      prefix: --channels
      position: 3
outputs:
  plot:
    type: File
    outputBinding:
      glob: $(inputs.output_file_name)
