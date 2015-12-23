#!/bin/bash
# Author: Archer Reilly
# File: GatherHtmls.sh
# Date: 23/Dec/2015
# Desc: move all subdirectories's html file into a signle directory
#
# Produced By BR

# check command line parameters first
if [ $# -ne 2 ]; then
  echo "Usage: GatherHtmls Source Destination"
  exit 1
fi

Source=$1
Destination=$2

# recursively loop though the Source directory
for path in $Source/*; do
  printf $path
  printf "\n"
done
