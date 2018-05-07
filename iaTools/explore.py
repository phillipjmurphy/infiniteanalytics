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