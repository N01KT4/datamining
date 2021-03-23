import numpy as np
import pandas as pd

def PreProcess(namestr):
    data = pd.read_csv(namestr+"_Raw_data.csv")
    # 去除首列的序号（linpack无序号）
    if not namestr=="linpack": data = data.iloc[:, 1:]
    # 分离尾列的场景，方便后续纯数据处理
    species = data["species"]
    data = data.iloc[:, :-1]
    print("Has any null: ",(data.isnull()).any().any())
    # 经验证无缺失值
    # data.dropna(how="any")
    # print(namestr+" reserved:")
    # print(data)
    # NonGaussian = data["TasksTotal":"TasksSleeping"]
    # 3σ原则筛选正常数据
    normal = (data - data.mean()) / data.std()
    normal = (normal >-3) & (normal < 3)
    # 在原数据中保留正常数据
    data = data[normal == True]
    print(data)
    # data["TasksTotal":"TasksRuning"] = NonGaussian
    data = data.dropna(how="any")
    # 补回尾列场景
    data["species"] = namestr
    print(data)
    

PreProcess("fio")
'''
PreProcess("linpack")
PreProcess("mlc")
PreProcess("tpc")
'''