filepath = {
    'train_label': 'data/train_y_answer.csv',
    'public_alert_date': 'data/public_x_alert_date.csv',
    'train_x_alert_date': 'data/train_x_alert_date.csv',
    'cust_info': 'data/public_train_x_custinfo_full_hashed.csv',
    'ccba': 'data/public_train_x_ccba_full_hashed.csv',
    'cdtx': 'data/public_train_x_cdtx0001_full_hashed.csv',
    'dp': 'data/public_train_x_dp_full_hashed.csv',
    'remit': 'data/public_train_x_remit1_full_hashed.csv',
    'predicted_alert_key': 'data/predicted_alert_key.csv'
}

data_list = ['cust_info', 'ccba', 'cdtx', 'dp', 'remit']

train_test_split = 0.2
random_state = 1114

cust_info_columns_type = {
    'risk_rank': 'cateogry',
    'occupation_code': 'cateogry',
    'AGE': 'category',
    'total_asset': 'numeric',
}

dp_columns_type = {
    'tx_amt': 'numeric',
    'exchg_rate': 'numeric',
    'tx_time': 'numeric', 
    'debit_credit': 'cateogry', 
    'tx_type': 'cateogry', 
    'info_asset_code': 'cateogry', 
    'fiscTxId': 'cateogry', 
    'cross_bank': 'cateogry', 
    'ATM': 'cateogry',
}

