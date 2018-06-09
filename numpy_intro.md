# Numpy入門
数値を要素にもつ配列を高速に処理するためのライブラリ。
http://www.numpy.org

機械学習などでデータを扱う際によく用いられる。

## 配列の定義
`array`メソッドで配列を定義する。
```python
import numpy as np
a = np.array([0,1,2,3])
print(a)
print(a.ndim, a.shape, len(a))
```

2次元配列も定義できる。
```python
b=np.array([[0,1,2],[3,4,5]]) #2x3 array
print(b)
print(b.ndim, b.shape, len(b))
```

3次元配列も定義できる。
```python
d=np.array([[1,4],[2,5],[3,6]])
print(d)
print(d.ndim, d.shape, len(d))
```

色々と簡単に配列を定義できる。
```python
a=np.arange(10) #0から9まで
b=np.arange(1,9,2) #9は入らない
c=np.linspace(0,1,6) #1は入る
d=np.linspace(0,1,6,endpoint=False) #1は入らない
print(a,b,c,d)
```

## 様々な要素の指定方法
通常のリストと同じように、番号を適切に指定することで要素を取り出すことができる。
```python
a=np.arange(10)
print(a)
print(a[0])
print(a[2])
print(a[-1])
print(a[::-1])
print(a[2:9:3])
print(a[::-1])
print(a[2:9][::-1])
```

条件に合う要素のみを取り出す。
```python
print(a%3==0)
print(a[a%3==0])
a[a%3==0]=-1
print(a)
```

少し変わった要素の指定。
```python
idx=np.array([[3,4],[9,7]])
print(a[idx])
```


### 二次元配列の要素の指定
```python
a=np.array([[1,2],[3,4]])
print(a[0,1])
```

`np.newaxis`を使って配列に新しい次元を追加できる。
```python
print(np.arange(0,51,10)[:,np.newaxis])
```

```python
a=np.arange(6)+np.arange(0,51,10)[:,np.newaxis]
print(a)
print(a[0,3:5])
print(a[4:,4:])
print(a[:,2])
print(a[2::2,::2])
print(a[(0,1,2,3,4),(1,2,3,4,5)])
print(a[3:,[0,2,5]])
print(a[::-1,2:4])
mask=np.array([1,0,1,0,0,1],dtype=bool)
print(mask)
print(a[mask,2])
```

条件に該当するindexを返す
```python
x=np.arange(10)+2
print(x[x%2==0])
print(np.where(x%2==0))
```


## 速度比較
速さを比較してみよう
```python
N=100000000
s=0
from time import time
start = time()
np.arange(N).sum()
print(time()-start)
```

```python
s=0
from time import time
start = time()
for i in range(N):
    s=i+s
print(s)
print(time()-start)
```

## 乱数生成
標準的な確率分布に従った乱数を生成できる。

一様分布
```python
a=np.random.rand(4)
b=np.random.rand(3,4)
print(a,b)
```

正規分布
```python
x=np.random.normal(loc=0, scale=1, size=10)
print(x)
```

二項分布
```python
x=np.random.binomial(n=5, p=0.5, size=10)
print(x)
```
ポアソン分布
```python
x=np.random.poisson(lam=3, size=10)
print(x)
```


# 論理演算
数値だけでなくbool型の演算も行うことができるが、少し注意が必要。

```python
a=np.array([True,True,False,False])
b=np.array([True,False,True,False])
print(np.logical_or(a,b))
print(np.logical_and(a,b))
```


# 行列の演算
掛け算、逆行列、転置
```python
a = np.array([[1,2],[3,4]])
b = np.array([[1,0,],[0,-1]])
print(a)
```
行列の転置は`transpose`を用いる。
```python
print(a.transpose())
```

逆行列は`np.linalg.inv`を用いる。
```python
print(np.linalg.inv(a))
```

行列の掛け算は`np.dot`を用いる。
```python
print(a+b)
print(a*b)
print(np.dot(a,b))
```
