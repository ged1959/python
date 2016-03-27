# coding: utf-8
# 「超」入門。p.163

'''
このページのコードはうまくいかない。これ。python2、3のどちらでも。

>>> today.strftime('%Y年%m月%d日')

エラーは以下。

>>> today.strftime('%Y年%m月%d日')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 2: Il
legal byte sequence

考えられること。==> strftimeの使い方のミス？引数の指定方法？

いずれにせよ、年月日での表示は必須（になる可能性がある）。どんくさい方法でも試しておく。
'''

# 1. たぶん、最もどんくさい。
from datetime import date
date.today()
kyou = date.today()
kyounen = str(kyou.year)
kyoutuki = str(kyou.month)
kyoubi = str(kyou.day)
print (kyounen+"年"+kyoutuki+"月"+kyoubi+"日")

# 2. もっとコンパクトにならんのか。
print ('{0}年{1}月{2}日'.format(kyounen, kyoutuki, kyoubi))

# 3. もっと、もっと。
print ('{0}年{1}月{2}日'.format(kyou.year, kyou.month, kyou.day))

# 4. もっと、もっと、もっと。これなら2行になるが…。
print ('{0}年{1}月{2}日'.format(date.today().year, date.today().month, date.today().day))

# 5. 別の方法
print (str(kyou.year)+"年"+str(kyou.month)+"月"+str(kyou.day)+"日")

# でも、どれもどんくさい。いい方法はないのか。