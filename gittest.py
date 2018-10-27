# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:gittest.py
@time:2018/10/20 21:10
"""
import os
import pandas as pd
import numpy as np


def cutname(list):
    major = []
    cla = []
    name = []

    for i in range(len(list)):

        j = 0
        k = j

        while j < len(list[i]) and list[i][j] != '-':
            j += 1
        major.append(list[i][k:j])

        j += 1
        k = j
        while j < len(list[i]) and list[i][j] != '-':
            j += 1
        cla.append(list[i][k:j])

        j += 1
        k = j
        while j < len(list[i]) and list[i][j] != '.':
            j += 1
        name.append(list[i][k:j])

    return major, cla, name


if __name__ == "__main__":
    listtxt = os.listdir("c:\\Users\\yxr\\Desktop\\GitTest\\实战班")

    major, cla, name = cutname(listtxt)

    data_arry = []
    data_arry.append(major)
    data_arry.append(cla)
    data_arry.append(name)

    np_data = np.array(data_arry)
    np_data = np_data.T
    np.array(np_data)

    print(np_data)

    save = pd.DataFrame(np_data, columns=['专业', '班级', '姓名'])
    save.to_csv('./gittest.csv', index=True)
