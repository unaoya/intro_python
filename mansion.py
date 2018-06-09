import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# アパート価格のデータ
df = pd.read_csv("Mansion1.csv")

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)

print(df.describe())

# 質的変数の要約
print(df.dtypes)
print(df.dtypes[df.dtypes == object])
print(df.dtypes[df.dtypes == object].index)

for i in df.dtypes[df.dtypes == object].index:
    print(df[i].value_counts())

# ソート
print(df.sort_values(by='家賃'))

# DataFrame.queryを用いて、条件に合うデータを取り出す（遅い？）
# 南向き、築5年以内
new = df.query("方角=='南' and 築年数 <= 5")
print(new)

# GroupBy
print(df.groupby('近さ'))
print(df.groupby('近さ')['間取り'].value_counts())

# 近さA/Bを数値0/1に変換する
dummy_df = pd.get_dummies(df['近さ'])
print(dummy_df.head())

df_new = pd.concat([df, dummy_df], axis=1)
print(df_new.head())

df_rm = df_new.drop('B', axis=1)
print(df_rm.head())

# 変数間の相関、クロス集計
print(df.corr())
print(pd.crosstab(df['近さ'], df['方角']))
print(pd.pivot_table(df, index='近さ', columns='間取り'))

# 家賃のヒストグラム
sns.distplot(df['家賃'], kde=False)
plt.show()

# 家賃と大きさの散布図
sns.jointplot('家賃', '大きさ', data=df)
plt.show()

sns.pairplot(df)
plt.show()

# 箱ひげ図
sns.boxplot('近さ', '家賃', data=df)
plt.show()

# 近さごとに色分けしてヒストグラム、散布図
sns.pairplot(df, hue='近さ')
plt.show()

# 複数のグラフを並べる
g = sns.FacetGrid(df, col='近さ')
g.map(plt.hist, '家賃')
plt.show()

g = sns.FacetGrid(df, col='方角', hue='近さ', col_wrap=4)
g.map(plt.scatter, '大きさ', '家賃')
plt.show()

# 近さによって家賃の分布がどう変わるかを調べる
# t検定
print(stats.ttest_ind(df[df['近さ'] == 'A']['家賃'], df[df['近さ'] == 'B']['家賃']))

# 大きさと家賃の関係
# 線形回帰
print(stats.linregress(df['大きさ'], df['家賃']))
sns.lmplot('大きさ', '家賃', data=df)
plt.show()