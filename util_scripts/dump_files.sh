#!/bin/bash

# for ChatGTP help purposes

output_file="output.txt"

# Recreate the output file
rm -f "$output_file"
touch "$output_file"

# Function to process a single file
process_file() {
  local file="$1"
  echo "*${file#./}*" >> "$output_file"
  cat "$file" >> "$output_file"
  echo -e "\n__________\n" >> "$output_file"
}

# Exclude unnecessary file extensions
exclude_exts=(-name '*.pyc' -o -name '*.pyo' -o -name '*.log')

# If no arguments are provided, find all files except those starting with a dot and excluded file extensions
if [ $# -eq 0 ]; then
  find . -type f -not -path '*/\.*' \( "${exclude_exts[@]}" -prune -o -print0 \) | while IFS= read -r -d '' file; do
    process_file "$file"
  done
else
  # Process specified files and directories
  for path in "$@"; do
    if [[ -d "$path" ]]; then
      find "$path" -type f -not -path '*/\.*' \( "${exclude_exts[@]}" -prune -o -print0 \) | while IFS= read -r -d '' file; do
        process_file "$file"
      done
    elif [[ -f "$path" && "${path##*/}" != .* && ! "${path##*.}" =~ ^(pyc|pyo|log)$ ]]; then
      process_file "$path"
    fi
  done
fi
