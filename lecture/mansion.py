import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('Mansion1.csv')

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)

print(df.describe())

print(df.dtypes[df.dtypes == object])
print(df.dtypes[df.dtypes == object].index)

for i in df.dtypes[df.dtypes == object].index:
    print(df[i].value_counts())

# print(df.sort_values(by='家賃', ascending=False))

new = df.query("方角 == '南' and 築年数 <= 5")
print(new)

print(df.groupby('近さ')['間取り'].value_counts())
print(df.groupby('近さ').describe()['大きさ'])

dummy_df = pd.get_dummies(df['近さ'])
print(dummy_df)

print(pd.get_dummies(df['間取り']))

print(df.corr())
print(pd.crosstab(df['近さ'], df['方角']))

sns.distplot(df['家賃'])
plt.show()

sns.jointplot('家賃', '大きさ', data=df)
plt.show()

sns.pairplot(df)
plt.show()

sns.boxplot('近さ', '家賃', data=df)
plt.show()

sns.pairplot(df, hue='近さ')
plt.show()

g = sns.FacetGrid(df, col='近さ')
g.map(plt.hist, '家賃')
plt.show()

g = sns.FacetGrid(df, col='方角', hue='近さ',
                  col_wrap=4)
g.map(plt.scatter, '大きさ', '家賃')
plt.show()

print(stats.ttest_ind(df[df['近さ']=='A']['家賃'],
                      df[df['近さ']=='B']['家賃']))

print(stats.linregress(df['大きさ'], df['家賃']))
sns.lmplot('大きさ', '家賃', data=df)
plt.show()