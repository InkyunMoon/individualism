import pandas as pd
import re
import numpy as np

# 시트 번호 - 항목
# 19-성인 남성 흡연율
# 23-현재 흡연자의 금연시도율
# 28-현재 비흡연자의 직장실내 간접흡연 노출율
# 50-월간음주율
# 70-격렬한 신체활동 실천율
# 52-고위험음주율
# 73-걷기 실천율
# 80-5일 이상 아침식사 실천율
# 83-영양표시 독해율
# 89-비만유병율
# 96-어제 점심식사 후 칫솔질 실천율

gu_list = ['강남구','강동구','강서구','강북구','관악구','광진구','구로구','금천구','노원구','동대문구','도봉구','동작구',\
           '마포구','서대문구','성동구','성북구','서초구','송파구','영등포구','용산구','양천구','은평구','종로구','중구','중랑구']
sheet_list = [19, 23, 28, 50, 52, 70, 73, 80, '83, 84', 89, 96]
nine_eleven = [19,23,28,50,52,70,73,'83, 84']#
# twelve_fourteen = [80, 96]
eighty = [80]#
ninety_six = [96]
thirteen_fifteen = [89]
reverse_list = [70,73,80,'83, 84',96] # '걷기 실천율' 같이 높을수록 긍정적인 지표는 -처리를 해서 높을수록 안좋게 만들어준다. 예) 1-걷기 실천율 -> 걷기 비실천율

path = 'C:\\Users\\moon\\Documents\\final_p\\after_submit\\구 모음\\excel\\'

def get_df(df): # '%(표준오차)' 컬럼에서 %만 분리
    ratio = df.iloc[:,2].map(lambda x : x.split('(')[0])
    df['ratio'] = ratio.map(lambda x : float(x) if x != '-' else 0)
    df.iloc[:,1] = df.iloc[:,1].astype('float64')
    
def get_mean(df):
    get_df(df)
    return sum(df.iloc[:,1]*(df.iloc[:,3]*0.01))/sum(df.iloc[:,1])

# '구'당 11개의 지표를 각각 가중평균한다.
result_df = pd.DataFrame({'sheet_no':sheet_list})
result_df = result_df.set_index('sheet_no')
for gu in gu_list:
    print('*****'+gu+' 진행 중...*****')
    feature_list = []
    
    for sheet in sheet_list:    
        print(str(sheet)+'번 시트 진행 중...')

        if sheet in nine_eleven:
            df = pd.read_excel(path + gu + '.xlsx', sheet_name=str(sheet), header=0, usecols=[0,1,2])[7:10].reset_index(drop=True)
            feature_list.append(get_mean(df))
        elif sheet in eighty:
            df = pd.read_excel(path + gu + '.xlsx', sheet_name="80", header=0, usecols=[0,1,2])[10:13].reset_index(drop=True)
            feature_list.append(get_mean(df))
        elif sheet in ninety_six:
            df = pd.read_excel(path + gu + '.xlsx', sheet_name="96", header=0, usecols=[0,4,5])[10:13].reset_index(drop=True)
            feature_list.append(get_mean(df))
        elif sheet in thirteen_fifteen:
            df = pd.read_excel(path + gu + '.xlsx', sheet_name="89", header=0, usecols=[0,1,6])[11:14].reset_index(drop=True)
            feature_list.append(get_mean(df))
    
    # 높을수록 긍정인 지표를 부정지표로 바꿔준다.
    feature_list[5] = 1 - feature_list[5]
    feature_list[6] = 1 - feature_list[6]
    feature_list[7] = 1 - feature_list[7]
    feature_list[8] = 1 - feature_list[8]
    feature_list[10] = 1 - feature_list[10]
        
    result_df[gu] = feature_list
print('모든 작업을 완료했습니다.')


# result_df.to_csv('C:\\Users\\moon\\Documents\\final_p\\after_submit\\구 모음\\result_df.csv', index=False, encoding='utf-8-sig')
# result_df.T.to_csv('C:\\Users\\moon\\Documents\\final_p\\after_submit\\구 모음\\result_df_T.csv', index=True, encoding='utf-8-sig')

df = result_df.T
df
data = np.array(df)
