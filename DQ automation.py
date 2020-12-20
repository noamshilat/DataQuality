import pandas as pd
import numpy as np
import re
from datetime import *
############################################################
# DataFrame and Dictionaries
# Get the data
df = pd.read_excel(path)
# if needed, get additional data like dictionary df's and there columns
dict_column = pd.read_excel(path)[column_name]
###########################################################
def data_setup():
    answer = input('Have you setup a DataFrame and Dictionaries for work?(Y/N) ')
    if answer != 'Y':
      raise Exception("Please setup DataFrame and Dictionaries.")
###########################################################
def preliminary_settings():
    global table_name, table_list,column_list, row_index_list, original_value_list, dq_test_type_list, runtime_list
    table_name = input('What is yout table name? ')
    index_column = input(f'''Please select a column to set as an index (unique ID of the record in the table): {(', '.join(df.columns))}.
    your choice is... ''')
    df.set_index(index_column,inplace=True)
    table_list = []
    column_list = []
    row_index_list = []
    original_value_list = []
    dq_test_type_list = []
    runtime_list = []
############################################################
def null_test(df):
    for column in df.columns:
        for index, row in df.iterrows():
            if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(row[column])))== 0) or (len(re.sub('^\s*$','',str(row[column])))== 0) or (pd.isnull(row[column])):
                table_list.append(table_name),
                column_list.append(column),
                original_value_list.append(df.loc[index,column]),
                row_index_list.append(index),
                dq_test_type_list.append('null_test'),
                runtime_list.append(str(datetime.now()))
################################################################
def date_test(df):
    date_columns = input(f'''Please select date columns: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    for column in df[date_columns]:
        for index, row in df.iterrows():
            try:
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(row[column])))> 0) and (len(re.sub('^\s*$','',str(row[column])))> 0) and (pd.isnull(row[column]) is False):
                    if (pd.to_datetime(row[column]) > date.today()) or (pd.to_datetime(row[column]) < pd.to_datetime('1900-01-01')):
                        table_list.append(table_name),
                        column_list.append(column),
                        original_value_list.append(df.loc[index,column]),
                        row_index_list.append(index),
                        dq_test_type_list.append('date_test'),
                        runtime_list.append(str(datetime.now()))
            except:
                table_list.append(table_name),
                column_list.append(column),
                original_value_list.append(df.loc[index,column]),
                row_index_list.append(index),
                dq_test_type_list.append('date_test'),
                runtime_list.append(str(datetime.now()))
#########################################################
def dict_test(df,dict_column):
    column2check = input(f'''Please select columns to check against list: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    
    for column in df[column2check]:
        for index, row in df.iterrows():
            if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(row[column])))> 0) and (len(re.sub('^\s*$','',str(row[column])))> 0) and (pd.isnull(row[column]) is False):
                    if str(row[column]) not in [str(item) for item in dict_column]:
                        table_list.append(table_name),
                        column_list.append(column),
                        original_value_list.append(df.loc[index,column]),
                        row_index_list.append(index),
                        dq_test_type_list.append('dict_test'),
                        runtime_list.append(str(datetime.now()))
#########################################################
def error_log_generator():
    error_log = pd.DataFrame(list(zip(table_list, column_list, row_index_list, original_value_list, 
                                 dq_test_type_list, runtime_list)), 
       columns =['Table', 'Column', 'Row_index', 'Original_value', 'DQ_test_type', 'Runtime'])
    return error_log
#########################################################
data_setup()
preliminary_settings()
null_test(df)
date_test(df)
dict_test(df,dict_column)
error_log_generator()
