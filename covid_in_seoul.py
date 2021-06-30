import pandas as pd

# download data from Seoul Official Statistics Site
# for Korean, use encoding cp949
doc = pd.read_csv('../seoul_covid_19.csv', encoding='cp949', error_bad_lines=False)

# set index
doc = doc.set_index('자치구 기준일')

# delete unnecessary columns
del doc['수집일']
del doc['기타 전체']
del doc['기타 추가']
# drop unnecessary columns which contains '추가' in column name
doc = doc[doc.columns[pd.Series(doc.columns).str.endswith('전체')]]

# edit column name and index name
doc.columns = doc.columns.str.replace(' 전체', '')
doc.index = doc.index.str.slice(start=0, stop=10)

# drop NaN, sort, change data type
doc = doc.dropna()
doc = doc.sort_index(ascending=True)
doc = doc[doc.columns].astype('int64')

doc.info()

# exchange column and index
doc = doc.transpose()

# save
doc.to_csv('../seoul_covid_final.csv', encoding='utf-8-sig')

# use bar chart race
https://public.flourish.studio/visualisation/6593480/
