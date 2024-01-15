import pandas as pd

def get_data(PATH):
    df = pd.read_parquet(PATH)
    df.reset_index(inplace=True)
    #df = df.groupby(['borough_pickup_location','business','date','hour_of_day'])[['rides_quantity']].sum()
    #df.reset_index(inplace=True)
    df['date'] = df['date'].astype(str)
    print(df.dtypes)
    return df