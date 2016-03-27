+++
date = "2016-03-21T16:33:26+09:00"
draft = false
slug = "dot_install"
tags = ["ドットインストール", ""]
title = "基礎中の基礎はこちらで"

+++

基礎中の基礎は、いつもお世話になっている「[ドットインストール](http://dotinstall.com/)」さんで学ぶ。「[Python入門 (全24回) - プログラミングならドットインストール](http://dotinstall.com/lessons/basic_python_v2)」から。

## データ型、None

相当に基礎なのだろうけど、[#03 変数とデータ型について | Python入門 - プログラミングならドットインストール](http://dotinstall.com/lessons/basic_python_v2/26003)の部分。ソースというか、解説メモにある```None```が謎である。
```
# coding: UTF-8
# 変数（データにつけるラベル）

# データ型
# 数値
# 真偽値 True False
# None
# 関数・オブジェクト
# 要素が並んだもの
# - 文字列：文字が並んだもの
# - リスト：データが並んだもの
# - タブル：データが並んだもの（変更ができない）
# - セット：データが並んだもの（重複を許さない）
# - 辞書：キーと値がペア

msg = "hello world" 
print msg
```
ので、調べる。というか、ググる。まず出てきたのが、「[PythonではNoneの比較は==ではなくisを使う - こんにちはこんにちはmonmonです！](http://monmon.hateblo.jp/entry/20110214/1297710749)」と、目を引くのが出てきた。あと、「[Pythonを勉強していて「こういう書き方があったのか」と思ったことを3つ - 主にプログラムを勉強するブログ](http://d.hatena.ne.jp/artgear/20131018/three_python_tricks)」とか。なんじゃ？そもそも、```None```が意味不明なんだから、まだ、自分には早い。で、後の方のリンクに、以下のような比較構文があると。
```
if 1 < a < 5:
    print u'aは1から5の間'
```
ホンマ？試す。```test0321.py```に。便利だ。また寄り道だが、「[真(true)と偽(false) - 条件分岐 - Python入門](http://www.pythonweb.jp/tutorial/if/index3.html)」には、以下のコード。
```
print "True = ", True
print "False = ", False

print "True + 3 = ", True + 3

if True:
  print "Always True"
```
でも、```print hoge```はダメ。当たり前だけど。

で、上を見ていると気が付くのは、```print```という関数は奥が深いみたい、ということで、調べてみたら、以下のようなサイトに。「[Pythonのprint文 - Life with Python](http://www.lifewithpython.com/2013/08/print-statement.html)」「[pythonのprint内で変数に代入されている数字や文字を表示する - Qiita](http://qiita.com/yuukiclass/items/760b9cd85f503fd03fbd)」「[print文 - Python入門から応用までの学習サイト](http://www.python-izm.com/contents/basis/print.shtml)」。

寄り道しすぎだ。今は、```None```。「[ネイティブデータ型 - Dive Into Python 3 日本語版](http://diveintopython3-ja.rdy.jp/native-datatypes.html)」には、こんな説明。なんだか哲学的。

> NoneはPythonの特別な定数で、これはnull値（無効値）である。NoneはFalseではないし、0でもないし、空の文字列でもない。NoneをNone以外の値と比較すると、常にFalseが返る。

で、また寄り道だけど、このサイトは、「[Dive Into Python 3 で新しくなったこと](http://diveintopython3-ja.rdy.jp/whats-new.html)」＜「[Dive Into Python 3 日本語版](http://diveintopython3-ja.rdy.jp/index.html)」なっていて、前者に以下の記述。いつか見てみよう。

> Python 3には2to3というスクリプトが付属している。これを学び、これを愛し、これを使おう。2to3を使ってコードをPython 3へ移植するは、2to3で自動的に何が修正できるのかを全て集めたレファレンスとなっている。その多くは構文の変更なので（printは今や関数であり、`x`はもう使えない、などなど）、この章はPython 3でなされた多くの構文の変更について学ぶ良い足がかりになる。

「[お気楽 Python プログラミング入門](http://www.geocities.jp/m_hiroi/light/python02.html)」には、

> Python の場合、関数の返り値は return を使って返します。これはＣ言語と同じです。Perl のように、ブロックの最後で実行された処理結果が返り値とはなりません。return のない関数は None というデータを返します。None は Python の中でただ一つしか存在しない特別なデータ型で、値がないことや偽 (False) を表すために使用されます。

で、結論。必要になったら、勉強しよう。

## 複素数とは

次に、「[#04 数値を使ってみよう | Python入門 - プログラミングならドットインストール](http://dotinstall.com/lessons/basic_python_v2/26004)」。自分で勉強して、という「複素数」だ。

```
# coding: UTF-8
# 数値
# 整数、小数、複素数

# 演算子 + - * / // % **
print 10 * 5 # 50
print 10 // 3 # 3
print 10 % 3 # 1
print 2 ** 3 # 8

# 整数と小数の演算 → 小数
print 5 + 2.0

# 整数同士の割り算 → 切り捨ての整数
print 10 / 3.0
```
さっそく、ググる。うひゃ、すぐ出た。「[Python で複素数を扱う - Qiita](http://qiita.com/shuhei/items/f5cf6c83fcfb5dd24c2d)」。感動ものとあるので、試す。

```
print((1 + 2j) * (3 + 4j))
# (-5+10j)
print((1 + 2j) / (3 + 4j))
# (0.44+0.08j))
```
ホンマ、感動や。