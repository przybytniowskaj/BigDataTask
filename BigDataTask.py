import pandas as pd

def join(path1, path2, column_name, type)
    try:
        file1 = open(path1)
        file2 = open(path2)
    except IOError:
        print("File not accessible")
        return
    data1 = pd.read_csv(path1)
    data2 = pd.read_csv(path2)
    if column_name not in data1 or column_name not in data2:
        print("Column_name does not exist in DataFrame"
              return
    data1 = pd.read_csv(path1)
    data2 = pd.read_csv(path2)
    if pd.isna(type):
        type = "inner"
    try:
        merged = data1.join(data2, on = column_name, how = type)
    except IOError:
        print("Incorrect type")
        return
    merged.to_csv("./merged.csv")
    return