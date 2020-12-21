import pandas as pd
import numpy as np
import re
from datetime import *

############################################################
# DataFrame and Dictionaries
# Get the data
df = pd.read_csv('')
# if needed, get additional data like dictionaries and there list of values.
dict_column = pd.read_csv('')['']
###########################################################
def data_setup():
    answer = input('Have you setup a DataFrame and Dictionaries for work?(Y/N) ')
    if answer != 'Y':
      raise Exception("Please setup DataFrame and Dictionaries. Then, try again..")
###########################################################
def preliminary_settings():
    global table_name, table_list,column_list, row_index_list, original_value_list, dq_test_type_list, runtime_list
    table_name = input('What is your table name? ')
    table_list = []
    column_list = []
    row_index_list = []
    original_value_list = []
    dq_test_type_list = []
    runtime_list = []
############################################################
def null_test(df):
    for column in df.columns:
        for index, value in enumerate(df[column],start=1):
            if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))== 0) or (len(re.sub('^\s*$','',str(value)))== 0) or (pd.isnull(value)):
                table_list.append(table_name),
                column_list.append(column),
                original_value_list.append(value),
                row_index_list.append(index),
                dq_test_type_list.append('null_test'),
                runtime_list.append(str(datetime.now()))
################################################################
def alphanumeric_test(df):
    column2check = input(f'''Please select columns to check for alphanumeric only: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    
    for column in df[column2check]:
        for index, value in enumerate(df[column],start=1):
            if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                    if len(re.sub('^[a-zA-Z0-9]*$','',str(value)))> 0:
                        table_list.append(table_name),
                        column_list.append(column),
                        original_value_list.append(value),
                        row_index_list.append(index),
                        dq_test_type_list.append('alphanumeric_test'),
                        runtime_list.append(str(datetime.now()))
################################################################
def name_test(df):
    column2check = input(f'''Please select columns to check for names(A-z and א-ת) only: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    
    for column in df[column2check]:
        for index, value in enumerate(df[column],start=1):
            if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                    if len(re.sub('^[a-zA-Zא-ת\s]*$','',str(value)))> 0:
                        table_list.append(table_name),
                        column_list.append(column),
                        original_value_list.append(value),
                        row_index_list.append(index),
                        dq_test_type_list.append('name_test'),
                        runtime_list.append(str(datetime.now()))
################################################################
def digit_test(df):
    column2check = input(f'''Please select columns to check for digit only: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    
    for column in df[column2check]:
        for index, value in enumerate(df[column],start=1):
            if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                    if len(re.sub('^[0-9]*$','',str(value)))> 0:
                        table_list.append(table_name),
                        column_list.append(column),
                        original_value_list.append(value),
                        row_index_list.append(index),
                        dq_test_type_list.append('digit_test'),
                        runtime_list.append(str(datetime.now()))
################################################################
def date_test(df):
    date_columns = input(f'''Please select date columns: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    for column in df[date_columns]:
        for index, value in enumerate(df[column],start=1):
            try:
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                    if (pd.to_datetime(value) > date.today()) or (pd.to_datetime(value) < pd.to_datetime('1900-01-01')):
                        table_list.append(table_name),
                        column_list.append(column),
                        original_value_list.append(value),
                        row_index_list.append(index),
                        dq_test_type_list.append('date_test'),
                        runtime_list.append(str(datetime.now()))
            except:
                table_list.append(table_name),
                column_list.append(column),
                original_value_list.append(value),
                row_index_list.append(index),
                dq_test_type_list.append('date_test'),
                runtime_list.append(str(datetime.now()))
#########################################################
def phone_test(df):
    column2check = input(f'''Please select columns to check for israeli phone format: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    
    for column in df[column2check]:
        for index, value in enumerate(df[column],start=1):
            if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                    value = str(value).replace('-','')
                    value = value.zfill(10)
                    if len(re.sub('^\+?(972|0)(\-)?0?(([23489]{1}\d{7})|[5]{1}\d{8})$','',str(value)))> 0:
                        table_list.append(table_name),
                        column_list.append(column),
                        original_value_list.append(value),
                        row_index_list.append(index),
                        dq_test_type_list.append('phone_test'),
                        runtime_list.append(str(datetime.now()))
#########################################################
def dict_test(df,dict_column):
    column2check = input(f'''Please select columns to check against list: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    
    for column in df[column2check]:
        for index, value in enumerate(df[column],start=1):
            if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                    if str(value) not in [str(item) for item in dict_column]:
                        table_list.append(table_name),
                        column_list.append(column),
                        original_value_list.append(value),
                        row_index_list.append(index),
                        dq_test_type_list.append('dict_test'),
                        runtime_list.append(str(datetime.now()))
#########################################################
def duplicate_test(df):
    column2check = input(f'''Please select columns to set as unique id of row to find duplicate rows: {(', '.join(df.columns))}.
your choices are(column1,column2)... ''').split(',')
    
    for value in df.index[df.duplicated(subset=column2check, keep=False)]:
        table_list.append(table_name),
        column_list.append(column2check),
        original_value_list.append(list(df.loc[value,column2check])),
        row_index_list.append(value),
        dq_test_type_list.append('duplicate_test'),
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
alphanumeric_test(df)
name_test(df)
digit_test(df)
date_test(df)
phone_test(df)
dict_test(df,dict_column)
duplicate_test(df)
error_log_generator()
