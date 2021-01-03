# Documentation

    # Methods
        
        # df_show - Shows original data frame.
        # df_save2excel - Saves original data frame to current directory(with index) as excel file.
        # null_test - Checks for empty/null/meaningless values in all the data frame.
        # null_specific_test - Checks for empty/null/meaningless values in specific columns.
        # leadtrail_whitespace_test - Checks for leading/trailing whitespaces in values in specific columns.
        # alphanumeric_test - Checks for alphanumeric values in specific columns.
        # name_test - Checks for name values in specific columns.
        # digit_test - Checks for digit values in specific columns.
        # date_test - Checks for date format in specific columns and if the date before '1900-01-01' and after today's date.
        # date_order_test - Checks the order of date columns in specific row in the data frame.
        # phone_test - Israeli phone validation for specific columns.
        # dict_test - Checks column value against list of values
        # context_test - Checkes the value of specific column when other column equal to specific values.
        # duplicate_test - Checks duplicate rows in data frame based on user definition. 
        # error_log_generator - Generates error log based on pevious tests.
        # error_log_show - Shows error log after generation.
        # error_log_save2excel - Saves error log to current directory as excel file.
        # fully_quality_df_show - Shows data frame who passed all the tests, based on pevious tests.
        # fully_quality_df_save2excel - Saves data frame to current directory as excel file.
    
    
    # Notice
        
        # All inputs should be in a list structure, except for the context_column2check_value argument in the context_test method that should be in a string structure.
        # After initial setup of a data set and table name any test can be used. Do not forget,
            # after running tests run the error_log_generator method to generate an error report.
            
import pandas as pd
import numpy as np
import re
from datetime import *
import os
from sqlalchemy import create_engine
import hvplot.pandas


class DataQuality:
    
    def __init__(self,table_name,df):
        self.table_name = table_name
        self.table_list = []
        self.column_list = []
        self.row_index_list = []
        self.original_value_list = []
        self.dq_test_type_list = []
        self.runtime_list = []
        self.df = df
        self.cwd = os.getcwd()
        
    def df_show(self):
        return self.df
    
    def df_save2excel(self):
        self.df.to_excel(self.table_name+'_'+datetime.today().strftime('%d_%m_%Y')+'.xlsx')
        print(f'File saved to {self.cwd} successfully!')
    
    def null_test(self):
        for column in self.df.columns:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))== 0) or (len(re.sub('^\s*$','',str(value)))== 0) or (pd.isnull(value)):
                    self.table_list.append(self.table_name),
                    self.column_list.append(column),
                    self.original_value_list.append(value),
                    self.row_index_list.append(index),
                    self.dq_test_type_list.append('null_test'),
                    self.runtime_list.append(str(datetime.now()))
                    
    def null_specific_test(self,null_columns2check):
        for column in self.df[null_columns2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))== 0) or (len(re.sub('^\s*$','',str(value)))== 0) or (pd.isnull(value)):
                    self.table_list.append(self.table_name),
                    self.column_list.append(column),
                    self.original_value_list.append(value),
                    self.row_index_list.append(index),
                    self.dq_test_type_list.append('null_test'),
                    self.runtime_list.append(str(datetime.now()))
                    
    def leadtrail_whitespace_test(self,leadtrail_whitespace_columns2check):
        for column in self.df[leadtrail_whitespace_columns2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                    if len([len(item) for item in (re.findall('(^\s*|\s*$)',str(value))) if len(item) > 0]) > 0:
                        self.table_list.append(self.table_name),
                        self.column_list.append(column),
                        self.original_value_list.append(value),
                        self.row_index_list.append(index),
                        self.dq_test_type_list.append('leadtrail_whitespace_test'),
                        self.runtime_list.append(str(datetime.now()))                
    
    def alphanumeric_test(self,alphanumeric_column2check):
        for column in self.df[alphanumeric_column2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if len(re.sub('^[a-zA-Z0-9]*$','',str(value)))> 0:
                            self.table_list.append(self.table_name),
                            self.column_list.append(column),
                            self.original_value_list.append(value),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('alphanumeric_test'),
                            self.runtime_list.append(str(datetime.now()))
    
    def name_test(self,name_column2check):
        for column in self.df[name_column2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if len(re.sub('^[a-zA-Zא-ת\s]*$','',str(value)))> 0:
                            self.table_list.append(self.table_name),
                            self.column_list.append(column),
                            self.original_value_list.append(value),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('name_test'),
                            self.runtime_list.append(str(datetime.now()))
    
    def digit_test(self,digit_column2check):
        for column in self.df[digit_column2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if len(re.sub('^[0-9]*$','',str(value).replace('.','',1)))> 0:
                            self.table_list.append(self.table_name),
                            self.column_list.append(column),
                            self.original_value_list.append(value),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('digit_test'),
                            self.runtime_list.append(str(datetime.now()))
    
    def date_test(self,date_columns):
        for column in self.df[date_columns]:
            for index, value in enumerate(self.df[column]):
                try:
                    if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if (pd.to_datetime(value) > date.today()) or (pd.to_datetime(value) < pd.to_datetime('1900-01-01')):
                            self.table_list.append(self.table_name),
                            self.column_list.append(column),
                            self.original_value_list.append(value),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('date_test'),
                            self.runtime_list.append(str(datetime.now()))
                except:
                    self.table_list.append(self.table_name),
                    self.column_list.append(column),
                    self.original_value_list.append(value),
                    self.row_index_list.append(index),
                    self.dq_test_type_list.append('date format error'),
                    self.runtime_list.append(str(datetime.now()))
                    
    def date_order_test(self,first_date_column,second_date_column):
            for index in self.df.index:
                try:
                    if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if pd.to_datetime(self.df[''.join(first_date_column)][index]) > pd.to_datetime(self.df[''.join(second_date_column)][index]):
                            self.table_list.append(self.table_name),
                            self.column_list.append(''.join(first_date_column)+', '+''.join(second_date_column)),
                            self.original_value_list.append(self.df[''.join(first_date_column)][index]+', '+self.df[''.join(second_date_column)][index]),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('date_order_test'),
                            self.runtime_list.append(str(datetime.now()))
                except:
                    pass    
                    
    def phone_test(self,phone_column2check):
        for column in self.df[phone_column2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if len(re.sub('^(0|972|)(?:[23489]|5[0-689]|7[234679])(\d{7})$','',str(value).replace('-','')))> 0:
                            self.table_list.append(self.table_name),
                            self.column_list.append(column),
                            self.original_value_list.append(value),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('phone_test'),
                            self.runtime_list.append(str(datetime.now()))
                            
    def dict_test(self,dict_column2check,list_column):
            for index, value in enumerate(self.df[''.join(dict_column2check)]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if value not in [item for item in list_column]:
                            self.table_list.append(self.table_name),
                            self.column_list.append(''.join(dict_column2check)),
                            self.original_value_list.append(value),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('dict_test'),
                            self.runtime_list.append(str(datetime.now()))
                            
    def context_test(self,context_column2check,context_column2check_value,context_column2check_against,context_list2check):
        for index, value in enumerate(self.df[''.join(context_column2check)]):
            try:
                if self.df.loc[index, ''.join(context_column2check)] == context_column2check_value:
                    if self.df.loc[index,''.join(context_column2check_against)] not in [item for item in context_list2check]:
                        self.table_list.append(self.table_name),
                        self.column_list.append(''.join(context_column2check_against)),
                        self.original_value_list.append(self.df.loc[index,''.join(context_column2check_against)]),
                        self.row_index_list.append(index),
                        self.dq_test_type_list.append('context_test'),
                        self.runtime_list.append(str(datetime.now()))
            except:
                pass
    
    def duplicate_test(self,duplicate_column2check):
        for value in self.df.index[self.df.duplicated(subset=duplicate_column2check, keep=False)]:
            try:
                for item in [item for item in self.df.loc[value,duplicate_column2check]]:
                    if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(item)))> 0) and (len(re.sub('^\s*$','',str(item)))> 0) and (pd.isnull(item) is False):
                        self.table_list.append(self.table_name),
                        self.column_list.append(', '.join([str(item) for item in duplicate_column2check])),
                        self.original_value_list.append(', '.join([str(item) for item in self.df.loc[value,duplicate_column2check]])),
                        self.row_index_list.append(value),
                        self.dq_test_type_list.append('duplicate_test'),
                        self.runtime_list.append(str(datetime.now()))
            except:
                pass
            
    def error_log_generator(self):
        self.error_log = pd.DataFrame(list(zip(self.table_list, self.column_list, self.row_index_list, self.original_value_list, 
                                     self.dq_test_type_list, self.runtime_list)), 
           columns =['Table', 'Columns', 'Row_index', 'Original_values', 'DQ_test_type', 'Runtime']).drop_duplicates(subset=['Columns','Row_index']).reset_index(drop=True).sort_values('Row_index')
        print('Error log created successfully!')
        
    def error_log_show(self):
        Columns_visual_df = self.error_log.Columns.value_counts()
        DQ_test_type_visual_df = self.error_log.DQ_test_type.value_counts()
        display(Columns_visual_df.hvplot.bar(y='Columns'))
        display(DQ_test_type_visual_df.hvplot.bar(y='DQ_test_type'))
        return self.error_log.drop_duplicates(subset=['Columns','Original_values','DQ_test_type'])
        #return self.error_log
    
    def error_log_save2excel(self):
        self.error_log.drop_duplicates(subset=['Columns','Original_values','DQ_test_type']).to_excel(self.table_name+'_ErrorLog_'+datetime.today().strftime('%d_%m_%Y')+'.xlsx',index=False)
        #self.error_log.to_excel(self.table_name+'_ErrorLog_'+datetime.today().strftime('%d_%m_%Y')+'.xlsx',index=False)
        print(f'File saved to {self.cwd} successfully!')
    
    def fully_quality_df_show(self):
        self.fully_quality_df = self.df.loc[~self.df.index.isin(set(self.error_log['Row_index']))]
        print(str(len(self.fully_quality_df)/len(self.df)*100)+'%'+' of the Data is fully quality!')
        return self.fully_quality_df
    
    def fully_quality_df_save2excel(self):
        self.fully_quality_df.to_excel(self.table_name+'_FullyQuality_'+datetime.today().strftime('%d_%m_%Y')+'.xlsx',index=False)
        print(f'File saved to {self.cwd} successfully!')
