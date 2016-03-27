# coding: UTF-8
# i have tried these, on 0321.

# 比較の構文。こんなの！
'''
a = 30
if 1 < a < 5:
    print u'aは1から5の間'
else:
    print u'ちゃうがな'
'''

# True, Falseも奥深い。
'''
print "True = ", True
print "False = ", False

print "True + 3 = ", True + 3

if True:
  print "Always True"

print True # OK!
print hoge # エラーになる。
'''

# 複素数
# print((1 + 2j) * (3 + 4j))
# (-5+10j)
# print((1 + 2j) / (3 + 4j))
# (0.44+0.08j))

# コマンド引数
import sys   # sysモジュールをimport

# sys.argvにコマンドライン引数が「リスト」で格納されている
print(sys.argv) 
print(len(sys.argv))