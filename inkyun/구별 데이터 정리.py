import pandas as pd
import re

# 시트 번호 - 항목

# 19-성인 남성 흡연율
# 23-현재 흡연자의 금연시도율
# 28-현재 비흡연자의 직장실내 간접흡연 노출율
# 50-월간음주율
# 70-격렬한 신체활동 실천율
# 52-고위험음주율
# 73-걷기 실천율
# 80-5일 이상 앛미식사 실천율
# 83-영양표시 독해율
# 89-비만유병율
# 96-어제 점심식사 후 칫솔질 실천율

dj_19 = pd.read_excel('C:/Users/moon/Documents/final_p/after_submit/2019 지역사회 건강통계_서울 동작구.xlsx', sheet_name='19', header=3, usecols=['Unnamed: 0','N','%(표준오차)'])[4:7].reset_index(drop=True)

#12.3(4.5)에서 12.3만 분리하는법

dj_19['표준오차'] = dj_19['%(표준오차)'].str.findall('[\d.\d]+(?=\()')

dj_19['%(표준오차)'].str.findall('[\d.\d]+(?=\()')

dj_19['%(표준오차)'].str.split(expand=True)[0].str.findall('[\d.\d]+(?=\()')
dj_19['%(표준오차)'].str.extract('[\d.\d]+(?=\()')


dj_19['%(표준오차)'].filter(regex='+)

sample = '12.3(4.5)'
