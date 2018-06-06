# Python3とPyCharmのインストール方法
すうがくぶんか「基礎から学ぶPython講座」受講生向けの
python3及びPyCharmインストール手順です。
python3のインストール方法はいくつかありますが、
ここでは準備が少ない方法を紹介します。

こちらはwindowsユーザー向けです。

# Python3のインストール

まずはPython3をインストールします。
すでにインストールされている場合は、こちらは飛ばしても大丈夫です。

まず、以下のページを開きます。
https://www.python.org/downloads/

Download Python 3.6.5をクリックし、実行を選択します。

![1](images/python_install.png)
![1](images/python_install2.png)

しばらくしてダウンロードが終わると、以下のようにインストーラが起動するので、
install Nowを選びます。

![1](images/python_install3.png)

しばらくするとインストールが終了するのでcloseを選びます。

![1](images/python_install4.png)

以上でPython3のインストールが終了です。

# PyCharmのインストール
次にPyCharmをインストールします。
すでにPyCharmをインストールしている場合、こちらは飛ばしても大丈夫です。

以下のページを開きます。

https://www.jetbrains.com/pycharm

DOWNLODA NOWを選択します。

![1](images/pycharm_install.png)

今回は無料のcommunity版を使いますので、そちらをDOWNLOADします。

![1](images/pycharm_install2.png)

実行するとインストーラのダウンロードが始まります。

![1](images/pycharm_install3.png)

インストーラのダウンロードが終わると、インストーラが起動し次のような画面が開くので、Nextを実行します。

![1](images/pycharm_install4.png)

次の画面もそのままNextを実行します。

![1](images/pycharm_install5.png)

何もチェックせずNextを実行します。

![1](images/pycharm_install6.png)

そのままInstallを実行します。

![1](images/pycharm_install7.png)

しばらくするとインストールが終わるので、Finishを実行して終了です。

![1](images/pycharm_install8.png)


# 必要なパッケージのインストール

最後にPyCharmを起動し、必要なパッケージをインストールします。
左下のメニューから、JetBrains -> JetBrains PyCharm Community Editionと進んでPyCharmを起動します。

![1](images/pycharm1.png)

初回起動時のみ設定が必要ですが、そのままOKを実行します。

![1](images/pycharm2.png)

画面の配色をお好みで選んでください。

![1](images/pycharm3.png)

ここは後からでも必要に応じてインストールできるので、ひとまずは何もインストールせずStart using PyCharmを実行します。

![1](images/pycharm4.png)

次回起動時からは、この画面が開くはずです。
Create New Projectを選びます。

![1](images/pycharm5.png)

Projectの名前をつけます。今回はtestとします。

![1](images/pycharm6.png)

しばらくすると、次のような画面になります。
Closeを実行します。

![1](images/pycharm7.png)

File -> Default Settings -> Project Interpreter -> Show Allと進みます。

![1](images/pycharm8.png)
![1](images/pycharm9.png)
![1](images/pycharm10.png)

右上の+マークを選び、以下の画面が出たらOKを選びます。

![1](images/pycharm11.png)

次の画面でもOKを選びます。

![1](images/pycharm12.png)

先ほどのDefault Settingsの画面で、今準備したPython 3.6 (venv)というものを選択できるので、
それを選択したのち、右の+マークを選びます。
これを選ぶことで、新しいパッケージをインストールすることができます。

![1](images/pycharm13.png)

以下では今回必要なパッケージである

- numpy
- pandas
- scipy
- matplotlib
- scikit-learn

をインストールします。

手順は全て同様で、一番上の検索欄にパッケージ名を入れると左に出てくるので、
それを選択し左下のInstall Packageを実行すればインストールできます。

![1](images/pycharm14.png)
![1](images/pycharm15.png)
![1](images/pycharm16.png)
![1](images/pycharm17.png)
![1](images/pycharm18.png)
![1](images/pycharm19.png)

全てのパッケージがインストールできると、Degault Settingsの画面が次のようになります。
今インストールしたパッケージの名前があることを確認してください。

![1](images/pycharm20.png)

セッティングがうまくいっているか確認します。
File -> Settings -> Project:test -> Project Interpreterと進んで、
今準備したPython 3.6 (venv)を選択し、インストールしたライブラリがちゃんと揃っているか確認してください。

![1](images/pycharm24.png)
![1](images/pycharm25.png)

# コードの実行確認
最後にpythonのコードがきちんと実行されるか確認します。

File -> New -> Python Fileと進むと名前の入力を求められるので、testとしておきます。

![1](images/pycharm21.png)
![1](images/pycharm22.png)
![1](images/pycharm23.png)

ソースコードエディタが起動するので、こちらにコードを書いていきます。
今回はインストールされたパッケージがきちんと起動するか確認するため、
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("packages are installed")
```
と入力します。

![1](images/pycharm26.png)

ソースコードの実行は、Run -> Run testと進んで選択します。

![1](images/pycharm27.png)

画面の下側に、以下のように表示されれば成功です。

![1](images/pycharm28.png)

