import pandas as pd
import numpy as np

def get_z(series):
    return (series - series.mean()) / np.std(series)
    
df = pd.read_csv('C:/Users/moon/Documents/final_p/after_submit/구 모음/result_df.csv')

gu_list = ['강남구','강동구','강서구','강북구','관악구','광진구','구로구','금천구','노원구','동대문구','도봉구','동작구',\
           '마포구','서대문구','성동구','성북구','서초구','송파구','영등포구','용산구','양천구','은평구','종로구','중구','중랑구']

sheet_list = df.columns
sheet_list = sheet_list.drop('Unnamed: 0')

df_norm = df.copy()

# 모든 데이터를 표준화한다.
for sheet in sheet_list:
    df_norm.loc[:,sheet] = get_z(df_norm[sheet])

# 평균으로부터 2시그마를 벗어나는 데이터에 대해서 2시그마 내의 최대/최소값으로 대체함.
for sheet_num in sheet_list:
    df_norm[sheet_num][df_norm[sheet_num] > 1.96] = df_norm['19'][df_norm['19'] < 1.96].max()
    df_norm[sheet_num][df_norm[sheet_num] < -1.96] = df_norm['19'][df_norm['19'] > -1.96].min()

df_norm['sum'] = df_norm.sum(axis=1)
df_norm['mean'] = df_norm.mean(axis=1)

df_norm.to_csv('C:/Users/moon/Documents/final_p/after_submit/구 모음/건강지표_sum&mean.csv', index=False, encoding='utf-8-sig')