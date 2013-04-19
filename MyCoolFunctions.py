#!/usr/bin/env python

#======= IMPORTS ==============================================================
import os
import shutil
import numpy as np
#==============================================================================

#======= MAKE DIRS ============================================================
def KW_mkdirs(dir):
    """
    A very simple little function that replicates mkdir -p in bash
    Basically if the directory exists then it doesn't run the mkdirs command
    Easy peasy!
    """
    if not os.path.isdir(dir):
        os.makedirs(dir)
#==============================================================================

#======= REMOVE DIRS ============================================================
def KW_rmforce(dir_or_file):
    """
    A very simple little function that replicates rm -fr in bash
    Basically if the directory or file doesn't exist it doesn't try to
    remove them!
    """
    if os.path.isdir(dir_or_file):
        shutil.rmtree(dir_or_file)
    if os.path.isfile(dir_or_file):
        os.remove(dir_or_file)
#==============================================================================

#======= ROUND TO N SIG FIGS ==================================================
def KW_round(data, n):
    """
    This function takes a numpy array and rounds such that the smallest
        value has n significant figures
    """
    minimum = data.min()
    counter = 0
    if minimum == 0:
        counter = 0
    elif minimum > 10:
        while np.log10(minimum) >= 1:
            counter += 1
            minimum /= 10
        data = data / ( 10 ** counter )
        data = np.round(data, n-1)
        data = data * ( 10 ** counter )
    elif minimum < 1:
        while minimum ** 10 < 1:
            counter += 1
            minimum *= 10
        data = data * ( 10 ** counter )
        data = np.round(data, n-1)
        data = data / ( 10 ** counter )
    
    return data
#==============================================================================

#======= REMOVE DIRS ============================================================
def KW_paste(file1, file2, outfile):
    """
    A very simple little function that replicates paste in bash.
    It just puts together two files line by line, separated by a tab.
    It can deal with files of different length (without importing
    itertools...which isn't necessarily better, just a bit simpler).
    """
    with open(file1, 'r') as f1:
        f1_lines=f1.readlines()
    with open(file2, 'r') as f2:
        f2_lines=f2.readlines()
    common = min(len(f1_lines), len(f2_lines))

    with open(outfile, 'w') as f:
        for line1, line2 in zip(f1_lines[:common], f2_lines[:common]):
            f.write(line1.strip('\n') + '\t' + line2)
        if len(f1_lines) > len(f2_lines):
            for line1 in f1_lines[common:]:
                f.write(line1)
        elif len(f1_lines) < len(f2_lines):
            for line2 in f2_lines[common:]:
                f.write('\t' + line2)

#==============================================================================

