import pandas as pd 
import numpy as np
import copy

class Preprocessor():
    def __init__(self, configs):
        
        self.configs = configs

        self.train_label = self._load_data(self.configs.filepath['train_label'])
        self.public_alert_date = self._load_data(self.configs.filepath['public_alert_date'])
        self.predicted_alert_key = self._load_data(self.configs.filepath['predicted_alert_key'])
        self.train_x_alert_date = self._load_data(self.configs.filepath['train_x_alert_date'])
        self.cust_info = self._load_data(self.configs.filepath['cust_info'])
        self.ccba = self._load_data(self.configs.filepath['ccba'])
        self.cdtx = self._load_data(self.configs.filepath['cdtx'])
        self.dp = self._load_data(self.configs.filepath['dp'])
        self.remit = self._load_data(self.configs.filepath['remit'])
        
        self.train_key, self.public_key = self._train_public_list()
        self.dataset = self._process(self.configs)
        self.public_dataset = self._filter_and_merge(self.public_key)
        self.train_dataset = self._filter_and_merge(self.train_key, self.train_label)
        
    def _filter_and_merge(self, index_list, label=None):
        
        dataset = pd.DataFrame(data={'alert_key':index_list})
        dataset = dataset.merge(self.dataset, how='left', on='alert_key')
        if label is not None:
            dataset = dataset.merge(label, how='left', on='alert_key')
        return dataset
        
    def _load_data(self, filepath):
        
        data = pd.read_csv(filepath)
        return data
    
    def _train_public_list(self):
        
        train_list = list(self.train_label['alert_key'])
        public_list = list(self.predicted_alert_key['alert_key'])
        return train_list, public_list
    
    def _process(self, configs):
        
        dataset = self.cust_info.copy()
        dataset = self._filling_missing_value(dataset, configs.cust_info_columns_type)
        dataset = self._dealing_with_outlier(dataset, configs.cust_info_columns_type)
        dataset = self._add_count(dataset)
        return dataset
        
        
    def _filling_missing_value(self, dataset, columns_type):
        
        for column in columns_type.keys():
            
            if dataset[column].isna().any():
                
                if columns_type[column] == 'cateogry':
                    # fillin with mode
                    dataset[column].fillna(dataset[column].mode()[0], inplace=True)
                
                elif columns_type[column] == 'numeric':
                    # filling with median
                    dataset[column].fillna(dataset[column].median()[0], inplace=True)
        return dataset
        
    
    def _dealing_with_outlier(self, dataset, columns_type, remove_type ='box_plot'):
        
        if remove_type =='box_plot':
            dataset = self._box_plot(dataset, columns_type)
        return dataset
    
    
    def _box_plot(self, dataset, column_type, remove = True):
        
        for column in column_type.keys():
            
            if column_type[column] == 'numeric':
                Q1 = np.percentile(dataset[column], 25, method = 'midpoint')
                Q3 = np.percentile(dataset[column], 75, method = 'midpoint')
                IQR = Q3 - Q1

                upper = dataset[column] >= (Q3+1.5*IQR)
                lower = dataset[column] <= (Q1-1.5*IQR)

                dataset.loc[upper, column] = Q3+1.5*IQR
                dataset.loc[lower, column] = Q3-1.5*IQR
                
                return dataset
    
    def _get_count_dict(self, dataset):
        
        id_dict = {}
        for id in dataset.cust_id:
            if id not in id_dict:
                id_dict[id] = 1
            else:
                id_dict[id] += 1
        return id_dict
            
    
    def _add_count(self, dataset):
        
        id_dict = self._get_count_dict(self.cust_info)
        dataset['cust_info_count'] = dataset.cust_id.apply(lambda x: id_dict[x] if x in id_dict.keys() else 0)
        
        id_dict = self._get_count_dict(self.ccba)
        dataset['ccba_count'] = dataset.cust_id.apply(lambda x: id_dict[x] if x in id_dict.keys() else 0)
        
        id_dict = self._get_count_dict(self.cdtx)
        dataset['cdtx_count'] = dataset.cust_id.apply(lambda x: id_dict[x] if x in id_dict.keys() else 0)
        
        id_dict = self._get_count_dict(self.dp)
        dataset['dp_count'] = dataset.cust_id.apply(lambda x: id_dict[x] if x in id_dict.keys() else 0)
        
        id_dict = self._get_count_dict(self.remit)
        dataset['remit_count'] = dataset.cust_id.apply(lambda x: id_dict[x] if x in id_dict.keys() else 0)
        return dataset
        
        
        
        
            
        
        
        
        
        
        
            