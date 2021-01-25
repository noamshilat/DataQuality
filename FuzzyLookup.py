# Documentation

    # Methods
        
        # run_matching - Run the test.
    
    
    # Notice
        
        # The main goal of this class is to implement FuzzyWuzzy on a data frame using column as main data and lookup list or column as data to compare with.
        # The class takes data frame, data frame column name, lookup list and imagination ratio (default is 80). 
        # The class run on the entire column values and search for matches in the lookup list. if there is a match - it generates a new value in columm_matched column.

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
