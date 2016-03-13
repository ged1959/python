pythonの勉強
========

どんなプログラム言語を学ぶべきか。

３つのジャンルを試すべきだと思った。pythonの記事「[Pythonで学ぶ 基礎からのプログラミング入門 (1) Pythonでプログラミングを学ぶ理由とは? | マイナビニュース](http://news.mynavi.jp/series/python/001/)」にあった以下の図を見て、ビビッと。

<img src="http://news.mynavi.jp/series/python/001/images/003.jpg" style="width:400px;border:2px solid yellow">

Javaは、C#でも代替えが可能だと思うけれど、確かにpythonは、面白そう。

この記事の筆者は、あるタスクについて、上記の３つのプログラム言語でコードを書いて、比較している。pythonはとてもシンプル。アルゴリズムに集中して、記述できるところがいい。

そもそも、pythonのこの記事をどうして見たのか、というと、hugoが始まり。使いたいテーマ「[Hugo Theme: Base16](http://themes.gohugo.io/base16/)」があり、そのテーマの機能を使いこなすには、pythonのAPIが必要とあり…。

<img src="https://raw.githubusercontent.com/htdvisser/hugo-base16-theme/master/images/screenshot.png" style="width:400px;border:2px solid yellow">

なので、pythonの入門編を探していたら、ここに来た、というわけ。という、かなり半端な動機なので、忘れないように、githubでgitしながらチョコチョコとやろう。

で、最初のメモ。

python2系、python3系
-------------------------

ここは面倒。使い分けが必要らしい。とりあえず、動かすには、

```
python2系 ==> py
python2系 ==> python
```

日本語をコメントし、出力するには、スクリプト冒頭に以下。

```
# coding: utf-8
```

<code>print</code>の際には、

```
u
```
を日本語の冒頭につけること。

参考サイト
- [文字コードの指定 - 日本語と文字コード - Python入門](http://www.pythonweb.jp/tutorial/japan/index1.html)
- [#02 はじめてのPythonプログラム | Python入門 - プログラミングならドットインストール](http://dotinstall.com/lessons/basic_python_v2/26002)