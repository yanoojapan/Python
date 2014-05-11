#!/usr/bin/python
# coding: utf-8

# 条件分岐
x = int(input('数字を入力してください'))
if 10 < x :
  print('10 より大きい数字です')
else:
  print('10 より小さい数字です')

x = int(input('数字を入力してください: '))

if 10 < x and x % 2 == 0 :  # 最初の条件、かつ、二つ目の条件
  print('10 より大きく、かつ、偶数です')
else:
  print('10 より大きくないかまたは奇数です')
