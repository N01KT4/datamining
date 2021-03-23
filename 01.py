import numpy as np
import pandas as pd

def PreProcess(namestr):
    data = pd.read_csv(namestr+"_Raw_data.csv")
    # 去除首列的序号（linpack无序号）
    # 去除尾列的场景
    if not namestr=="linpack": data = data.iloc[:, 1:-1]
    print("Has any null: ",(data.isnull()).any().any())
    data.dropna(how="any")
    # print(namestr+" reserved:")
    # print(data)
    
    data = (data - data.mean()) / data.std()
    print(data)
    data = data[data > -3]
    data = data[data < 3]
    data = data.dropna(how="all")
    print(data)
    

PreProcess("fio")
'''
PreProcess("linpack")
PreProcess("mlc")
PreProcess("tpc")
'''