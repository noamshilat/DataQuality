from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

class FuzzyLookup:
    
    def __init__(self,df,df_column_name,lookup_list,imagination_ratio=80):
        self.df = df
        self.df_column_name = df_column_name
        self.lookup_list = lookup_list
        self.imagination_ratio = imagination_ratio
        
    def run_matching(self):
        self.df[self.df_column_name+'_matched'] = None
        for index, value in enumerate(self.df[self.df_column_name]):
            if process.extractOne(str(value),self.lookup_list)[1] > self.imagination_ratio:
                self.df.loc[index, self.df_column_name+'_matched'] = process.extractOne(str(value),self.lookup_list)[0]
            else:
                self.df.loc[index, self.df_column_name+'_matched'] = 'No similar values were found'
        return self.df
