import pandas as pd

x = pd.DataFrame({'Name':['A','B','C'],
                  '英語':[80, 75, 60],
                  '数学':[50, 60, 80],
                  '国語':[50, 60, 75]})
print(x)

print(x['Name'])
print(x['数学'])

x.index = x['Name']
print(x)

x = x.drop('Name', axis=1)
print(x)

print(x.ix[2,1])
print(x.ix['C','数学'])
print(x.ix[2,:])
print(x.ix[:,1])
print(x.ix['B',:])
print(x.ix[['A','B'],['英語','数学']])

print(x.loc[['A','B'],['英語','数学']])
print(x.iloc[[0,1],[0,1]])

print(x > 70)
print(x[x > 70])

print(x['英語'])
print(x['英語'][x['英語'] > 70])

y = pd.DataFrame({'Name':['D','E'],
                  '英語':[70,55],
                  '国語':[80,80],
                  '数学':[60,60]})
y.index = y['Name']
y = y.drop('Name', axis=1)

z = pd.concat([x, y])
print(z)

w = pd.DataFrame({'理科':[80, 70, 85, 60, 70],
                  '社会':[50, 60, 55, 75, 70]})
w.index = z.index
z_total = pd.concat([z,w], axis=1)
print(z_total)

print(z_total.apply(sum))
print(z_total.apply(sum, axis=1))

z_total['合計'] = z_total.apply(sum, axis=1)
print(z_total)

print(z_total.sort_values(['合計'], ascending=False))

print(z_total.info())
print(z_total.describe())

print(z_total.corr())

print(z_total <= 50)
print(z_total[z_total <= 50])

print(z_total[z_total['英語'] >= 70])
print(z_total[z_total['英語'] >= 70].sort_values(['合計'], ascending=False))

#z_sum = pd.concat([z_total, z_total.apply(sum, axis=1)], axis=1)
#print(z_sum)
#z_sum = z_sum.rename(columns={0: '合計'})
#print(z_sum)