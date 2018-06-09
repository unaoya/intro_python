# Seaborn入門
pythonでグラフなどを作図するライブラリとしてよく使われるものに`matplotlib`がある。

https://matplotlib.org

今回は`matplotlib`をより扱いやすくした`seaborn`ライブラリを用いて、
データの可視化をしてみる。

https://seaborn.pydata.org

また`scipy`を用いて簡単な統計分析も行ってみよう。
https://www.scipy.org

まずは必要なライブラリのインストール
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
```

## データを読み込む。
今回は配布したアパート価格のデータを用いる。

```python
df = pd.read_csv("Mansion1.csv")

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)

print(df.describe())
```

## 質的変数の要約
質的変数を要約しよう。
```python
print(df.dtypes)
print(df.dtypes[df.dtypes == object])
print(df.dtypes[df.dtypes == object].index)

for i in df.dtypes[df.dtypes == object].index:
    print(df[i].value_counts())
```

## ソート
```python
print(df.sort_values(by='家賃'))
```

## データの抽出
`DataFrame.query`を用いて、条件に合うデータを取り出す。

例えば南向き、築5年以内のデータを取り出そう。
```python
new = df.query("方角=='南' and 築年数 <= 5")
print(new)
```

## グルーピング
`groupby`を用いて、データをグルーピングできる。

```python
print(df.groupby('近さ'))
print(df.groupby('近さ')['間取り'].value_counts())
```

## ダミー変数
`get_dummies`を用いて、ダミー変数を作ることができる。

ここでは近さA/Bを数値0/1に変換しよう。
```python
dummy_df = pd.get_dummies(df['近さ'])
print(dummy_df.head())
```

新しい列として追加する。
```python
df_new = pd.concat([df, dummy_df], axis=1)
print(df_new.head())

df_rm = df_new.drop('B', axis=1)
print(df_rm.head())
```

## 変数間の関係
相関係数の計算、クロス集計表など
```python
print(df.corr())
print(pd.crosstab(df['近さ'], df['方角']))
print(pd.pivot_table(df, index='近さ', columns='間取り'))
```

# データの可視化
以下では`seaborn`を用いて、簡単なデータの可視化を行っていく。

## ヒストグラム
家賃のヒストグラムを描いてみる。
`distplot`メソッドを使う。
```python
sns.distplot(df['家賃'], kde=False)
plt.show()
```

## 散布図
家賃と大きさの散布図を描いてみる。
`jointplot`メソッドを使う。

```python
sns.jointplot('家賃', '大きさ', data=df)
plt.show()
```

全変数の関係を一気に図示する場合には`pairplot`を用いることもできる。
```python
sns.pairplot(df)
plt.show()
```

## 箱ひげ図
箱ひげ図を描くには`boxplot`メソッドを用いる。

```python
sns.boxplot('近さ', '家賃', data=df)
plt.show()
```

## 質的変数で色分け
近さごとに色分けしてヒストグラムや散布図を描いてみよう。
引数`hue`を指定してやればよい。

```python
sns.pairplot(df, hue='近さ')
plt.show()
```

## 複数のグラフを並べる
複数のグラフを並べるには`FacetGrid`を用いる。
`col`でどの変数に応じてグラフを描き分けるかを指定できる。

```python
g = sns.FacetGrid(df, col='近さ')
g.map(plt.hist, '家賃')
plt.show()
```

`col_wrap`を指定すると、配置を指定できる。
```python
g = sns.FacetGrid(df, col='方角', hue='近さ', col_wrap=4)
g.map(plt.scatter, '大きさ', '家賃')
plt.show()
```

# scipy.statsによる簡単な分析
## t検定
近さによって家賃の分布がどう変わるかを調べよう。

```python
print(stats.ttest_ind(df[df['近さ'] == 'A']['家賃'], df[df['近さ'] == 'B']['家賃']))
```

## 線形回帰
大きさと家賃の関係を線形回帰分析しよう。

```python
print(stats.linregress(df['大きさ'], df['家賃']))
sns.lmplot('大きさ', '家賃', data=df)
plt.show()
```
