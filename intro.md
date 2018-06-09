# PyCharm

6 hours to linear regression with python

線形回帰を用いてデータ分析をすることを目標にして、
6時間でpythonによるデータ分析に必要な基礎を概観する。

scikit-learnなどのライブラリを使う時に、何をやっているの想像できるように
自作クラスで線形回帰分析を行う。

# Hello world!
まずはhello worldを通してPyCharmの基本操作を学ぶ。

hello worldと表示するプログラムを書こう。  

```python
print('hello world')
```

- プロジェクト作成
- ファイル作成
- コードを書く
- 実行

の手順を確認する。

# 基本的なデータ型

まず基本的なデータ型として数値、文字列、真理値を扱う。  
わからないことがあればドキュメントを見よう。

https://docs.python.jp/3/index.html
  
また`?print`とすればリファレンスを見ることができる。

## 文字列
適当な文字列を`x`という変数に代入し、それを表示するプログラムを書こう。

```python
x='abc'
print(x)
```

`x`は`str`クラスのオブジェクトである。

```python
print(type(x))
```

`x`に対して、いくつかの操作を行うことができる。
`x`の長さを取り出す関数。
```python
print(len(x))
```

`x`の何文字目かを取り出す。
```python
print(x[2])
print(x[1])
print(x[0])
print(x[3])
```

エラーメッセージをよく読もう。
綴りの間違い、大文字と小文字、コンマとピリオド、かっこの閉じ忘れ、などはよくあるミス。


`x`の先頭の文字を大文字にするメソッド。
```python
print(x.capitalize())
```
この`x.capitalize()`という`.`を使った書き方はpythonで非常によく出てくる。

### 練習問題
各自の苗字、名前をそれぞれ`myouji, namae`という`str`型のオブジェクトに代入せよ。

次にその二つの文字列を結合して、`fullname`という`str`型のオブジェクトに代入せよ。
ここで文字列の結合は`+`を使うことでできる。

最後に`myouji, namae, fullname`を表示せよ。

## 数値型
数値型のデータを扱う。
また、演算子`+, -, *, /, //, ¥%, **`をそれぞれ使ってみる。
```python
x=3
y=4.0
print(x+y)
print(type(x))
print(type(y))
```
数値を表す型は一つではない。

nをmで割ったあまりを計算する。
```python
n, m=100,7
print(n%m) 
```

nのm乗を計算する。
```python
n,m=2,3
print(n**m) 
```

変わった代入の仕方。
```python
y,z=2,3
print(y)
print(z)
```

## bool型
真偽を表すbool型についてみてみる。
値は`True, False`の二つ。
演算子として`and, or`がある。

```python
print(type(True))
```

```python
x=True
y=False
print(x and y)
print(x or y)
```

結果がbool型となる比較演算子`==, !=, >, <, >=, =<, in`がある。
```python
x=3
y=3
print(x==y, x!=y)
```


### 練習問題
先ほどの`myouji, namae, fullname`の長さをそれぞれ`myouji_len, namae_len, fullname`というオブジェクトに代入し、
それらを表示せよ。

さらに`myouji_len, namae_len`の合計が`fullname_len`と一致するかを確認せよ。


# リスト
同じ型の要素をまとめて扱うために、リスト型のオブジェクトを作る。
リストの要素を取り出すときには`[]`を使う。
またリストに要素を追加するには`append`、リストの要素に含まれるかには`in`を使う。

```python
x=[1,2,3,4,5]
print(x)
print(x[4])
print(x[1:3])
print(type(x), len(x))
x.append(3)
print(x)
print(3 in x)
print(7 in x)
```

### 練習問題
素数を小さい順に10個並べたリスト`primes`を作れ。

`8`が`primes`の要素でないことを確認せよ。

3番目の素数と5番目の素数の合計を表示せよ。


# 条件文と制御文

## if文
ある条件に従って異なる操作をしたい場合if文を使う。

適当な数値型のオブジェクト`x`を定義し、
`x`が正の数の時`positive`、`x`が負の数の時`negative`、
`x=0`の時`zero`と出力するコードをかこう。

```python
x=1
if x>0:
    print('positive')
elif x<0:
    print('negative')
else:
    print('zero')
```

## while文
条件が満たされるまで同じ操作を繰り返したい時while文を使う。

1から10までの整数を順番に出力するコードを書こう。
```python
c=1
while c<10.1:
    print(c)
    c=c+1
```

### 練習問題
1から100までの整数の合計を計算せよ。

## for文
同じ操作を繰り返し行いたいときfor文を使う。

`int`型のオブジェクト`n`を定義し、n回`hello`と出力するコードをかこう。

```python
n=3
for i in range(n):
    print('hello')
```

`for`文の少し変わった書き方。
```python
x='abcde'
for i in x:
    print(i)
```

### 練習問題

`30`までの自然数を順に表示するコードをかけ。
ただし3の倍数の時には数の代わりに`Fizz`と表示、
5の倍数の時には数の代わりに`Buzz`と表示、
3でも5でも割り切れる時は`FizzBuzz`と表示せよ。

# 関数
ここまで、`len, type, print`などの関数を用いてきた。
`+, *`などの演算子も関数である。

何か同じ操作を繰り返し行うような場合には、関数を自分で定義すると便利。

`int`型の`n`を引数にとり、長さ`n`のリストで要素が全て`'hello'`であるものを返す関数を作れ。
さらにそれを利用して、前の問題と同じ結果を得るコードを書こう。

```python
def hello(n):
    hellos=list()
    for i in range(n):
        hellos.append('hello')
    return hellos
n=5
for i in hello(n):
    print(i)
```

### 練習問題
与えられた自然数`n`が素数であるか判定する関数`is_prime`を定義せよ。

またそれを利用して、素数を小さい順に100個並べたリストを作れ。

さらにその素数の合計を表示せよ。

# クラス
pythonでは全てはクラス。
クラスはいくつかの`attribute`と`methodをひとまとめにしたもの。

例えば文字列であれば、
そこにどのような文字が並んでいるか、特定の位置の文字を取り出す、大文字や小文字を変える、
などの操作をひとまとめにしておくと便利。

例えばPersonクラスを以下のように定義する。
`attribute`として名前を表す`name`と`身長を表す`height`をもつ。
また`method`として、自分の名前と身長を表示する`introduce`をもつ。

```python
class Person():
    def __init__(self, name, height):
        self.name=name
        self.height=height
    def introduction(self):
        print('私は' + self.name + 'です。身長は' + str(self.height) + 'です。')

a=Person('山田', 170)
print(a.name)
print(a.height)
a.introduction()
b=Person('田中',190)
b.introduction()
```

クラスを定義するときには`__init__`メソッドを必ず用意する。
これはそのクラスのオブジェクトが定義されたときに実行される。

```python
class hoge():
    def __init__(self):
        print(0)
a=hoge()
```

### 練習問題
次の機能を持つ統計処理クラスを自作してみる。  
あるクラスで行ったテストの点数を集計して`attribute`としてもち、
その集計結果を計算する`method`を持つ
- attribute
 * namesという受験者の名前のリスト
 * scoresという点数のリスト
- method
 * 平均を計算するmean
 * 分散を計算するvar
 * 最高点とその得点者を返すmax
 * 最低点とその得点者を返すmin

これを実装し、適当なデータを入れてちゃんと動くか確かめてみる。

```python
class Stats():
    def __init__(self,names,scores):
        self.names=names
        self.scores=scores
    def mean(self):
        return sum(self.scores)/len(self.scores)
    def var(self):
        return sum(self.scores ** 2)/len(self.scores) - self.mean() ** 2
    def maximum(self):#maxは組み込みにあるので別の名前をつける
        M=max(self.scores)
        ids=[i for i in range(len(self.scores)) if self.scores[i]==M]
        return M, [self.names[i] for i in ids]
    def minimum(self):#minも同様
        m=min(self.scores)
        ids=[i for i in range(len(self.scores)) if self.scores[i]==m]
        return m, [self.names[i] for i in ids]

sugaku=Stats(['A','B','C'],[80,70,60])
sugaku.mean(),sugaku.maximum(),sugaku.minimum()
```