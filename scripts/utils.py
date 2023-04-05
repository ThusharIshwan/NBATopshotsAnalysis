from web3 import Web3
from threading import Thread
import re
import pandas as pd
from os import listdir


def make_file_safe(string):
    # replace any non-alphanumeric characters with underscores
    safe_string = re.sub(r'[^\w\s]', '_', string)
    # remove any whitespace and convert to lowercase
    safe_string = re.sub(r'\s+', '_', safe_string).lower()
    return safe_string


def to_hex(x):
    """ Return the text of hex string.  If empty return empty string"""
    if x == '' or x is None:
        return ''
    if isinstance(x,list):
        return [to_hex(xi) for xi in x]
    return Web3.toHex(x).lower()


def distribute_elements(lst, n):
    """
    Distributes the elements of the given list `lst` into `n` sublists.
    """
    sublists = [[] for _ in range(n)]
    for i, element in enumerate(lst):
        sublists[i % n].append(element)
    return sublists


def consolodate_data(event_identifier, in_folder="output", out_folder="consolodated_output"):
    tot_df = pd.DataFrame({})
    nobs_count = 0
    output_count = 1
    for x in [l for l in listdir(in_folder) if event_identifier in l]:
        df = pd.read_csv(f'{in_folder}/{x}')
        if len(df) > 0:
            if nobs_count == 0:
                tot_df = df
                nobs_count = len(df)
            elif nobs_count + len(df) > 1000000:
                tot_df.to_csv(f"{out_folder}/{event_identifier}_{output_count}.csv", index = False)
                output_count += 1
                tot_df = df
                nobs_count = len(df)
            else:
                tot_df = pd.concat([tot_df, df], ignore_index=True)
                nobs_count += len(df)
    print(f"{out_folder}/{event_identifier}_{output_count}.csv")
    tot_df.to_csv(f"{out_folder}/{event_identifier}_{output_count}.csv", index = False)


def group_consecutive_numbers(lst):
    groups = []
    current_group = []
    
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1] + 1:
            # Start a new group
            current_group = [lst[i]]
            groups.append(current_group)
        else:
            # Add to the current group
            current_group.append(lst[i])
    return groups