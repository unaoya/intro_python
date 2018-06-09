# Pandas入門
Pandasではデータを表の形式でまとめた`DataFrame`を扱う。

https://pandas.pydata.org

あるクラスで行った試験の結果をまとめた`DataFrame`を以下のように定義しよう。
```python
import pandas as pd

x = pd.DataFrame({'Name':['A', 'B', 'C'],
                  '英語':[80, 75, 60],
                  '数学':[50, 60, 80],
                  '国語':[50, 60, 75]})
print(x)

```
リストと同じように`[]`で特定の要素を取り出すことができる。
```python
print(x['Name'])
print(x['数学'])
```

この表を少し加工していく。
まずは行の名前を書き換える。
`index`attributeに行の名前が入っている。
```python
x.index = x['Name']
print(x)
```

特定の行を削除するときには`drop`methodを使う。
```python
x = x.drop('Name', axis=1)
print(x)
```

## ix, loc, ilocの使い方
特定の位置にある要素を取り出す方法がいくつかあるので、それを紹介する。

```python
print(x.ix[2,1])
print(x.ix[2,'数学'])
print(x.ix['C','数学'])
print(x.ix[2,:])
print(x.ix['C',:])
print(x.ix[:,1])
print(x.ix[:,'数学'])
```

```python
print(x.loc[:,['数学', '英語']])
print(x.loc[['A', 'B'], ['数学', '英語']])
```

```python
print(x.iloc[1:2,1:3])
```

特定の条件を満たす要素を取り出す。
```python
print(x > 70)
print(x[x > 70])
```

```python
print(x['英語'])
print(x['英語'][x['英語'] > 70])
```

## データフレームの結合
二つのデータフレームを結合するには`concat`を使う。

先ほどのデータにDさん、Eさんの結果を追加して新しいデータフレームを作ろう。
```python
y = pd.DataFrame({'Name': ['D', 'E'],
                  '英語': [70, 55],
                  '国語': [80, 80],
                  '数学': [60, 60]})
y.index = y['Name']
y = y.drop('Name', axis=1)
```
```python
z = pd.concat([x, y])
print(z)
```

さらに、理科と社会の点数も追加して新しいデータフレームを作ろう。
```python
w = pd.DataFrame({'理科': [80, 70, 85, 60, 70],
                  '社会': [50, 60, 55, 75, 70]})
z_total = pd.concat([z,w], axis=1)
print(z_total)

w.index = z.index # 全部書き換えのみ
z_total = pd.concat([z,w], axis=1)
print(z_total)
```

## apply
各列や各行に同じ操作を行うときにはapplyを使う。

```python
print(z_total.apply(sum))
print(z_total.apply(sum, axis=1))
```

合計点を表す列を新たに追加しよう。

```python
z_sum = pd.concat([z_total, z_total.apply(sum, axis=1)], axis=1)
print(z_sum)

z_sum = z_sum.rename(columns={0: '合計'}) # 列名を一つだけ変更
print(z_sum)
```

要素の大きさに従ってソートできる。
```python
print(z_sum.sort_values(['合計'], ascending=False))
```

データフレームの要約は以下のようにできる。

```python
print(z_sum.info())
print(z_sum.describe())
print(z_sum.corr())
print(z_sum.cov())
```


### 練習問題
各教科の試験で、点数が50点以下のものは再試験を行うことになった。
誰のどの教科が再試験に該当するか、表示せよ。

また英語の点数が70点以上の者のうち、合計点がもっとも高い生徒を海外留学させることになった。
どの生徒が該当するか表示せよ。