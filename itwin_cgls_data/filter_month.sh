#!/bin/bash

# Define the source and target directories
src_dir="./2016"
target_dir="./2016_01"

# Create the target directory if it doesn't exist
mkdir -p "$target_dir"

# Loop over all .nc files in the source directory
for file in "$src_dir"/*.nc; do
    # If the filename contains "201601", move it to the target directory
    if [[ $(basename "$file") == *"201601"* ]]; then
        mv "$file" "$target_dir"
    fi
done