確認してほしいことは以下の3点です。
- python3がインストールされているか
- 必要なpythonのライブラリがインストールされているか
- pycharmからライブラリが使えるか

すでにpython3や必要なライブラリをインストールしている方は、
PyCharmから必要なライブラリを使うことができるかを確認してください。

以下の操作はターミナルを起動して行います。

# Homebrewのインストール
まずすでにHomebrewが入っているかどうか確かめましょう。
ターミナルに
```brew
which brew
```
と入力して`Enter`で実行してください。

インストールされていなければ以下のように何も表示されず次の行が出てきますので、
下の手順にしたがってインストールしてください。
![1](images/brew.png)

インストールされていれば以下のように表示されます。
![1](images/which_brew.png)
すでにインストールされている場合
```bash
brew update
```
しておきます。
![1](images/brew_update.png)

## インストールの手順
以下のwebpageにあるように、
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
を実行するとHomebrewのインストールが始まります。
![1](images/brew_webpage.png)

下の画面で止まったら`Enter`をおしてください。
![1](images/brew_install.png)
下の画面で止まったらmac起動時に入力するパスワードを入力してください。
![1](images/brew_install2.png)

そのまましばらく待てばHomebrewのインストールが終了します。


# pythonのインストール
次にHomebrewを使ってpython3をインストールします。
以下を実行します。
```bash
brew install python
```
![1](images/brew_install_python.png)

終了後
```bash
brew list
```
として`python`が表示されればokです。
![1](images/brew_list.png)

## python3が起動するかの確認
ターミナルから
```bash
python
```
で起動できるか確かめます。
![1](images/python_version_wrong.png)
このままだとPython 2.7.10となっていてpython3が起動できていません。
そのためにPATHを通します。

まず
```bash
vi .bash/profile
```
と入力してviを起動します。
次にキーボードの`i`を入力し
`export PATH="/usr/local/opt/python/libexec/bin:$PATH"`
と入力します。
その後`esc`キーをおし、`:wq`と入力し`Enter`キーをおします。
![1](images/path.png)

その後
```bash
source .bash_profile
```
を実行したのち、改めて
```bash
python
```
と実行すると以下のようにPython 3.6.5が起動されます。
![1](images/python_version.png)


# パッケージのインストール
次に必要なパッケージのインストールを行います。
```bash
pip install scipy
```
と入力し、実行します。
![1](images/install_scipy.png)

同様にして
```bash
pip install pandas
pip install matplotlib
pip install scikit-learn
```
を実行します。
![1](images/install_scikit-learn.png)

その後`pip list`を実行して、以下のように必要なパッケージが表示されればokです。
![1](images/fin_install_pkgs.png)

# PyCharmのインストール
まずbrew caskをインストールするため
```bash
brew tap caskroom/cask
brew install caskroom/cask
```
を実行します。

次にPyCharmをインストールするため
```bash
brew cask install pycharm-ce
```
を実行します。
![1](images/install_pycharm.png)

# PyCharmの実行
アプリケーションからPyCharmを選んで起動すると、
下のような画面が出てくるので、
Create New Projectを選びます。
![1](images/welcome.png)

Project InterpreterからExisting interpreterを選び、
先ほどインストールしたpython 3.6を選びます。
![1](images/select_env.png)

画面上部の`File` -> `New` -> `Python file`と選びます。
![1](images/pycharm.png)

下の画面と同じコードを書き、画面上部の`Run`から実行します。
![1](images/test_code.png)

次の画面下半分と同じものが出力されれば成功です。
![1](images/output.png)

