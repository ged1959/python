# coding: utf-8
# 「超」入門。p.159

'''
import calendar
print( calendar.month(2016, 3) )
'''

from datetime import date
date.today()
kyou = date.today()
# kyoubi = kyou.strftime('%Y年%m月%d日')
# kyoubi = kyou.strftime('%Y%m%d')
# kyoubi = kyou.day
# print (str(kyoubi)+u"日")
# print ('{}日'.format(kyou.day))
kyoubi = str(kyou.day)
print(kyoubi + "日")
# print("{kyoubi}日".format(**locals()))
kyounen = str(kyou.year)
kyoutuki = str(kyou.month)
print (kyounen+"年"+kyoutuki+"月"+kyoubi+"日")