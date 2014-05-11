#!/usr/bin/python
# coding: utf-8

import random  # @UnresolvedImport

print random.random()

var = 25
print var
var = "日本語"
print var

str1 = "ABC"
str2 = "ABC"
print str1 == str2
print str1 is not str2

str1 = "ABC"
str2 = str1
print str1 == str2
print str1 is not str2

amari = [10 % 3, 10 % 4, 10 % 2]
for i in amari :
  if i != 0:
    print "割り切れませんでした"
    print "余りは"+ str(i) + "です"
  else:
    print "割り切れました"
