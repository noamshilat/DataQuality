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
    
    def alphanumeric_test(self,alphanumeric_column2check):
        for column in self.df[alphanumeric_column2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if len(re.sub('^[a-zA-Z0-9]*$','',value))> 0:
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
                        if len(re.sub('^[a-zA-Zא-ת\s]*$','',value))> 0:
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
                        if len(re.sub('^[0-9]*$','',value))> 0:
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
                    self.dq_test_type_list.append('date_test'),
                    self.runtime_list.append(str(datetime.now()))
                    
    def phone_test(self,phone_column2check):
        for column in self.df[phone_column2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if len(re.sub('^\+?(972|0)(\-)?0?(([23489]{1}\d{7})|[5]{1}\d{8})$','',value.replace('-','').zfill(10)))> 0:
                            self.table_list.append(self.table_name),
                            self.column_list.append(column),
                            self.original_value_list.append(value),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('phone_test'),
                            self.runtime_list.append(str(datetime.now()))
                            
    def dict_test(self,dict_column2check,list_column):
        for column in self.df[dict_column2check]:
            for index, value in enumerate(self.df[column]):
                if (len(re.sub('[!@#$%^&*(),.?":{}|<>]','',str(value)))> 0) and (len(re.sub('^\s*$','',str(value)))> 0) and (pd.isnull(value) is False):
                        if value not in [str(item) for item in list_column]:
                            self.table_list.append(self.table_name),
                            self.column_list.append(column),
                            self.original_value_list.append(value),
                            self.row_index_list.append(index),
                            self.dq_test_type_list.append('dict_test'),
                            self.runtime_list.append(str(datetime.now()))
                            
    def context_test(self,context_column2check,context_column2check_value,context_column2check_against,context_list2check):
        for index, value in enumerate(self.df[context_column2check]):
            if self.df.loc[index, ''.join(context_column2check)] == str(context_column2check_value):
                if self.df.loc[index,''.join(context_column2check_against)] not in [str(item) for item in context_list2check]:
                    self.table_list.append(self.table_name),
                    self.column_list.append(''.join(context_column2check_against)),
                    self.original_value_list.append(self.df.loc[index,''.join(context_column2check_against)]),
                    self.row_index_list.append(index),
                    self.dq_test_type_list.append('context_test'),
                    self.runtime_list.append(str(datetime.now()))
                    
    def duplicate_test(self,duplicate_column2check):
        for value in self.df.index[self.df.duplicated(subset=duplicate_column2check, keep=False)]:
            self.table_list.append(self.table_name),
            self.column_list.append(', '.join([str(item) for item in duplicate_column2check])),
            self.original_value_list.append(', '.join([item for item in self.df.loc[value,duplicate_column2check]])),
            self.row_index_list.append(value),
            self.dq_test_type_list.append('duplicate_test'),
            self.runtime_list.append(str(datetime.now()))
            
    def error_log_generator(self):
        error_log = pd.DataFrame(list(zip(self.table_list, self.column_list, self.row_index_list, self.original_value_list, 
                                     self.dq_test_type_list, self.runtime_list)), 
           columns =['Table', 'Column', 'Row_index', 'Original_value', 'DQ_test_type', 'Runtime'])
        return error_log.drop_duplicates(subset=['Column','Row_index']).reset_index()
