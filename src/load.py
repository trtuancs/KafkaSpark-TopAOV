import pandas as pd
from sqlalchemy import create_engine

def load_data(data):
    engine = create_engine('postgresql://admin:adminpass@127.0.0.1:32773/postgres')
    data = data.replace('"', '')
    data_list = data[1:-1].split(', ')
    item = [x.split(': ') for x in data_list]
    col = [x[0] for x in item]
    value = [[x[1]] for x in item]
    value[1][0] = int(value[1][0])
    data_dict = dict(zip(col, value))
    df = pd.DataFrame(data_dict)
    df = df.set_index('id')
    df.to_sql('invoice_no', con=engine, if_exists='append')
