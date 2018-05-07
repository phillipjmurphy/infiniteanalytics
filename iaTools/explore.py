def search_for_col(data_frame, pattern):
    return  data_frame.columns[data_frame.columns.str.contains(pattern)]
 