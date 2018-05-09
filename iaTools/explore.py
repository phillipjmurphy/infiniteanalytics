from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def search_for_col(data_frame, pattern):
    return  data_frame.columns[data_frame.columns.str.contains(pattern)]

def data_frame_date_hist(col):
    value_count = col.value_counts()
    fig, ax = plt.subplots(figsize=(20,10))
    plt.bar(value_count.index,value_count.values)
    month_loc = mdates.MonthLocator(bymonth=np.arange(1,13), interval=1)
    date_format = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_locator(month_loc)
    ax.xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45)

def test_code():
    pass

def get_percent_null(col):
    # the df isn't global.
    if df[col].hasnans:
        return 100 * df[col].isnull().value_counts().loc[True] / df[col].shape[0]
    else:
        return 0.00

def get_has_nans(col):
    return df[col].hasnans
def get_is_unique(col):
    return df[col].is_unique

def another_test():
    df_meta = pd.DataFrame(df.columns)
    df_meta['pct_null'] = df_meta['COL_NAME'].apply(get_percent_null)
    df_meta['hasnans'] =  df_meta['COL_NAME'].apply(get_has_nans)
    df_meta['is_unique'] =  df_meta['COL_NAME'].apply(get_is_unique)