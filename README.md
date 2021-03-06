pythonの勉強
========

どんなプログラム言語を学ぶべきか。

３つのジャンルを試すべきだと思った。pythonの記事「[Pythonで学ぶ 基礎からのプログラミング入門 (1) Pythonでプログラミングを学ぶ理由とは? | マイナビニュース](http://news.mynavi.jp/series/python/001/)」にあった以下の図を見て、ビビッと。

<img src="http://news.mynavi.jp/series/python/001/images/003.jpg" style="width:400px;border:2px solid yellow">

Javaは、C#で代替えが可能だと思うけれど、確かにpythonは面白そう。

この記事の筆者は、あるタスクについて、上記の３つのプログラム言語でコードを書いて、比較している。pythonはとてもシンプル。アルゴリズムに集中して記述できるところがいい。

そもそも、pythonのこの記事をどうして見たのか、というと、hugoが始まり。使いたいテーマ「[Hugo Theme: Base16](http://themes.gohugo.io/base16/)」があり、そのテーマの機能を使いこなすには、pythonのAPIが必要とあり…。

<img src="https://raw.githubusercontent.com/htdvisser/hugo-base16-theme/master/images/screenshot.png" style="width:400px;border:2px solid yellow">

なので、pythonの入門編を探していたら、上記のサイトに来た、というわけ。ちょこっと使って終わりにしようと思っていたけど、改心して、少し真面目に勉強してみようか。そんな半端な動機なので、忘れないように、githubでgitしながらチョコチョコとやろう。

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

Visual Studio Codeで使えるか？
---------------------------------

これから試す。以下は参考サイト。

[Visual Studio Code で Python - JH1LHVの雑記帳](http://jh1lhv.hatenablog.jp/entry/2015/11/24/211052)

リンク
-------

- [python.jp](http://www.python.jp/)
- [Welcome to Python.org](https://www.python.org/)
- [Pythonや機械学習、そして言語の競争について – 極めて主観的な見地から | コンピュータサイエンス | POSTD](http://postd.cc/python-machine-learning-and-language-wars-a-highly-subjective-point-of-view/)
- [Python入門](http://www.tohoho-web.com/python/index.html)
- [[python] 細かすぎて伝わりにくい、Pythonの本当の落とし穴10選 | 私の小岩ホッチキス](http://kwatch.houkagoteatime.net/blog/2014/08/24/python-pitfalls/)

python勉強のサイト作った
----------------------------
gh-pagesなのだけど。以下。
[ぐだぐだ版 python memo](http://ged1959.github.io/python/)