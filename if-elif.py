# !/usr/bin/python3
# -*- coding:utf-8 -*-

height =float( input('输入身高:') )
weight =float( input('输入体重:') )
bmi = weight / (height * height)
if bmi <18.5:
    print('你的bmi是%d,过轻,' %(bmi))
elif bmi < 25:
    print('你的bmi是%d,正常,' %(bmi))
elif bmi < 28:
    print('你的bmi是%d,过重,' %(bmi))
elif bmi < 32:
    print('你的bmi是%d,肥胖,' %(bmi))
else:
    print('你的bmi是%d,严重肥胖,' %(bmi))

