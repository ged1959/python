# coding: UTF-8
# 変数（データにつけるラベル）
from datetime import datetime

msg = "hello world"
print msg
ja_msg = u"こんにちわ！"
print ja_msg

now = datetime.now()
print now
print str(now.year) + u"年"