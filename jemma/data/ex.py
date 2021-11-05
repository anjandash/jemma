import csv, os, sys 
import pandas as pd
csv.field_size_limit(sys.maxsize)

# STAGE I
# with open('/Users/anjandash/Desktop/maccode/projects_work/jemma/jemma/data/Giganticode_50PLUS_DB_projects.csv', 'r') as rd, \
#     open('/Users/anjandash/Desktop/maccode/projects_work/jemma/jemma/data/Giganticode_50PLUS_DB_projects_CENTOS.csv', 'w+') as wr:
#     csv_reader = csv.reader(rd)
#     csv_header = next(csv_reader)

#     csv_writer = csv.writer(wr)
#     csv_writer.writerow(["project_id", "project_name", "project_path"])

#     for i,row in enumerate(csv_reader):
#         csv_writer.writerow(row)

#         if i == 99:
#             break


# STAGE II
# projects_df = pd.read_csv("/Users/anjandash/Desktop/maccode/projects_work/jemma/jemma/data/Giganticode_50PLUS_DB_projects_CENTOS.csv", header=0)
# projects_tr = projects_df["project_id"].tolist()

# with open('/Users/anjandash/Desktop/maccode/projects_work/jemma/jemma/data/Giganticode_50PLUS_DB_classes.csv', 'r') as rd, \
#     open('/Users/anjandash/Desktop/maccode/projects_work/jemma/jemma/data/Giganticode_50PLUS_DB_classes_CENTOS.csv', 'w+') as wr:
#     csv_reader = csv.reader(rd)
#     csv_header = next(csv_reader)

#     csv_writer = csv.writer(wr)
#     csv_writer.writerow(["project_id", "class_id", "class_name", "class_path"])

#     for i,row in enumerate(csv_reader):
#         if row[csv_header.index('projectId')] in projects_tr:
#             csv_writer.writerow(row[1:])

# STAGE III
# projects_df = pd.read_csv("/Users/anjandash/Desktop/maccode/projects_work/jemma/jemma/data/Giganticode_50PLUS_DB_projects_CENTOS.csv", header=0)
# projects_tr = projects_df["project_id"].tolist()

# with open('/Volumes/KCORP-4TB/50KCDatabases/Giganticode_50PLUS_DB_methods_pid_cid_mid_mpath_mname_stln_enln_mtokens_mtext.csv', 'r') as rd, \
#     open('/Users/anjandash/Desktop/maccode/projects_work/jemma/jemma/data/Giganticode_50PLUS_DB_methods_CENTOS.csv', 'w+') as wr:
#     csv_reader = csv.reader(rd)
#     csv_header = next(csv_reader)

#     csv_writer = csv.writer(wr)
#     csv_writer.writerow(["project_id", "class_id", "method_id", "method_path", "method_name", "start_line", "end_line"])

#     #projects_set = set()
#     for i,row in enumerate(csv_reader):
#         if row[csv_header.index('projectId')] in projects_tr:
#             csv_writer.writerow(row[:-2])
#             #projects_set.add(csv_header.index('projectId'))


df = pd.read_csv("/Users/anjandash/Desktop/maccode/projects_work/jemma/jemma/data/Giganticode_50PLUS_DB_methods_CENTOS.csv",header=0)
x = df["project_id"].unique()

print(len(x))