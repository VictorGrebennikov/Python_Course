import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


def one_hot_func(data_frame):
    # get the values of the column headers
    headers_data = (data_frame.columns.values)

    # get all the unique data values in the columns
    col_data = list(set([item for items in data.values for item in items]))

    # creat new column headers
    new_headers = [j + "_" + i for i in col_data for j in headers_data]

    # prepar new data for the columns
    data_fill = [lst] * len(new_headers)

    # creat new "one_hot" DataFrame
    new_lst = zip(*data_fill)
    new_data = pd.DataFrame(new_lst, columns=new_headers)

    for count, i in enumerate(new_headers):
        new_data.loc[new_data[i] != col_data[count], i] = 0
        new_data.loc[new_data[i] != 0, i] = 1

    # sorting columns "one_hot" DataFrame
    one_hot_sorted = new_data.reindex(sorted(new_data.columns), axis=1)

    return one_hot_sorted


# compare the results
dummie_data = pd.get_dummies(data)
print(dummie_data.compare(one_hot_func(data), keep_shape=True, keep_equal=True))
