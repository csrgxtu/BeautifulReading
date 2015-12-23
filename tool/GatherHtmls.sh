#!/bin/bash
# Author: Archer Reilly
# File: GatherHtmls.sh
# Date: 23/Dec/2015
# Desc: move all subdirectories's html file into a signle directory
#
# Produced By BR
if [ $# -ne 3 ]; then
  echo "Usage: GatherHtmls Source Destination"
fi
