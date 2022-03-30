"""
jemma_utils

author: @anjandash
license: MIT
"""

import pandas as pd 


projects_csv = "./data/Giganticode_50PLUS_DB_projects_CENTOS.csv"
classes_csv  = "./data/Giganticode_50PLUS_DB_classes_CENTOS.csv"
methods_csv  = "./data/Giganticode_50PLUS_DB_methods_CENTOS.csv"

metrics = { 
    "CMPX": "./data/Giganticode_50PLUS_DB_metrics_CMPX_CENTOS.csv",
    "SLOC": "./data/Giganticode_50PLUS_DB_metrics_SLOC_CENTOS.csv",
    "MXIN": "./data/Giganticode_50PLUS_DB_metrics_MXIN_CENTOS.csv",
}

representations = {
    "TEXT": "./data/Giganticode_50PLUS_DB_representations_TEXT_CENTOS.csv",
    "TOKN": "./data/Giganticode_50PLUS_DB_representations_TOKN_CENTOS.csv",
    "C2VC": "./data/Giganticode_50PLUS_DB_representations_C2VC_CENTOS.csv",
    "C2SQ": "./data/Giganticode_50PLUS_DB_representations_C2SQ_CENTOS.csv",
}



# *************** #
#  get functions  #
# *************** #


# *************** #
#    projects     #
# *************** #


def get_project_id(project_name):
    """
    Returns the project_id of the project.

    Parameters:
    * project_name : str - name of the project

    Returns:
    * Returns a str uuid of the corresponding project (project_id)
    * Returns None if no project_id was found
    * Returns None if multiple projects were found with the same name
    """

    df = pd.read_csv(projects_csv, header=0)
    df = df[df["project_name"] == project_name.strip()]

    if df.shape[0] == 1:
        return df.iloc[0]["project_id"]
    return None


def get_project_id_by_path(project_path):
    """
    """

    df = pd.read_csv(projects_csv, header=0)
    df = df[df["project_path"] == project_path.strip()]

    if df.shape[0] == 1:
        return df.iloc[0]["project_id"]
    return None


def get_project_name(project_id):
    """
    """

    df = pd.read_csv(projects_csv, header=0)
    df = df[df["project_id"] == project_id.strip()]

    if df.shape[0] == 1:
        return df.iloc[0]["project_name"]
    return None


def get_project_path(project_id):
    """
    """

    df = pd.read_csv(projects_csv, header=0)
    df = df[df["project_id"] == project_id.strip()]

    if df.shape[0] == 1:
        return df.iloc[0]["project_path"]
    return None


# *************** #
#     classes     #
# *************** #


def get_class_id(project_id, class_name):
    """
    """
    
    df = pd.read_csv(classes_csv, header=0)
    df = df[(df['project_id'] == project_id.strip()) & (df['class_name'] == class_name.strip())]

    if df.shape[0] == 1:
        return df.iloc[0]['class_id']
    return None


def get_class_id_by_path(class_path):
    """
    """

    df = pd.read_csv(classes_csv, header=0)
    df = df[df["class_path"] == class_path.strip()]

    if df.shape[0] == 1:
        return df.iloc[0]['class_id']
    return None


def get_class_name(class_id):
    """
    """

    df = pd.read_csv(classes_csv, header=0)
    df = df[df["class_id"] == class_id.strip()]

    if df.shape[0] == 1:
        return df.iloc[0]['class_name']
    return None


def get_class_path(class_id):
    """
    """

    df = pd.read_csv(classes_csv, header=0)
    df = df[df["class_id"] == class_id.strip()]

    if df.shape[0] == 1:
        return df.iloc[0]['class_path']
    return None


# *************** #
#     methods     #
# *************** #


def get_method_id(class_id, method_name):
    """
    """

    df = pd.read_csv(methods_csv, header=0)
    df = df[(df['class_id'] == class_id.strip()) & (df['method_name'] == method_name.strip())]

    if df.shape[0] == 1:
        return df.iloc[0]['method_id']
    return None


# *************** #
#      utils      #
# *************** #


def get_properties(property, methods):
    """
    Get property values of a list of methods 

    Parameters:
    * property : (str) - property code
    * methods : list[str] - list of unique methods ids

    Returns:
    """

    # read the csv of the property
    # merge the property csv with the list of methods passed and return it
    pass

def get_representations(representation="C2VC", methods=method_ids):
    """
    Get representation values of a list of methods

    Parameters:
    * representation : (str) - representation code
    * methods : list[str] - list of unique methods ids
    """
    pass 

def get_callees(method_id):
    """
    """
    pass
