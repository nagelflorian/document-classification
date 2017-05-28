#!/bin/sh
python src/training.py \
  --bottleneck_dir="training/bottlenecks" \
  --model_dir="model/inception" \
  --summaries_dir="training/summaries" \
  --output_graph="model/retrained_graph.pb" \
  --output_labels="model/retrained_labels.txt" \
  --image_dir="training/images"
