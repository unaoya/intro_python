import pandas as pd

x = pd.DataFrame({'Name':['A', 'B', 'C'],
                  '英語':[80, 75, 60],
                  '数学':[50, 60, 80],
                  '国語':[50, 60, 75]})
print(x)

x.index = x['Name']
print(x)

x = x.drop('Name', axis=1)
print(x)

# ix, loc, ilocの使い方
print(x.ix[2,1])
print(x.ix[2,'数学'])
print(x.ix['C','数学'])

print(x.ix[2,:])
print(x.ix['C',:])

print(x.ix[:,1])
print(x.ix[:,'数学'])

print(x.loc[:,['数学', '英語']])
print(x.loc[['A', 'B'], ['数学', '英語']])
#print(x.loc[1:2,1:3])

#print(x.iloc[:,['数学', '英語']])
#print(x.iloc[['A', 'B'], ['数学', '英語']])
print(x.iloc[1:2,1:3])

print(x > 70)
print(x[x > 70])

print(x['英語'])
print(x['英語'][x['英語'] > 70])

# mapやapply
print(x.apply(sum))
print(x.apply(sum, axis=1))

# concat
y = pd.DataFrame({'Name': ['D', 'E'],
                  '英語': [70, 55],
                  '国語': [80, 80],
                  '数学': [60, 60]})

y.index = y['Name']
y = y.drop('Name', axis=1)
z = pd.concat([x, y])
print(z)

w = pd.DataFrame({'理科': [80, 70, 85, 60, 70],
                  '社会': [50, 60, 55, 75, 70]})
z_total = pd.concat([z,w], axis=1)
print(z_total)

w.index = z.index # 全部書き換えのみ
z_total = pd.concat([z,w], axis=1)
print(z_total)

print(z_total.apply(sum, axis=1))

z_sum = pd.concat([z_total, z_total.apply(sum, axis=1)], axis=1)
print(z_sum)

z_sum = z_sum.rename(columns={0: '合計'}) # 列名を一つだけ変更
print(z_sum)

print(z_sum.info())
print(z_sum.describe())
print(z_sum.corr())
print(z_sum.cov())

print(z_sum.sort_values(['合計'], ascending=False))
