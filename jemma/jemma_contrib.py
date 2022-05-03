"""
"""
import os
import sys 
import csv 
import pandas as pd 

metric_headers = {
    "SLOC": "source_lines_of_code",
    "NMRT": "num_returns",
    "MXIN": "max_indent",
    "NMLT": "num_literals",
    "CMPX": "cyclomatic_complexity",
    "NUID": "num_unique_identifiers",
    "NMOP": "num_operators",
    "NAME": "method_name",
    "NMTK": "num_tokens",
    "NTID": "num_identifiers",
    "NMPR": "num_parameters",
    "TLOC": "total_lines_of_code",
}


def add_metrics(metric, metric_values, method_ids):
    """
    Concatenate new property values to local csv

    Parameters:
    * metric        : str - property code
    * metric_values : list(str) or list(int) - list of property values
    * method_ids    : list(str) - list of unique method ids

    Returns:
    * null
    """

    mi = sys.path[0] + "/jemma_datasets/properties/Jemma_Properties_" + metric + ".csv"
    df = pd.read_csv(mi, header=0)

    metric_header = metric_headers.get(metric, "NOT_FOUND") # for CMPX it's cyclomatic_complexity
    dc = pd.DataFrame(zip(method_ids, metric_values), columns=["method_id", metric_header])

    dn = pd.concat([df, dc], ignore_index=True)
    dn.to_csv(mi[:-4] + ".contrib.csv", index=False)