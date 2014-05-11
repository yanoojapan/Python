#!/usr/bin/python
# coding: utf-8

L = ['Toyota', 'Nissan', 'Honda'] # リストを作成

for x in L :
  print x

print '==='

# 要素数をスキップ
for x in L[2:]:
  print x

print '==='
x = range(10)
print x

print '==='
x = range(5,10)
print x

print '==='
for i in range(5):
  print i

print '==='
for i in range(1,10):
  for j in range(1,10):
    print i,'×', j, '=', i * j
  print

print '==='
for i in range(3):
  print 'before=',i
  if 1<i:
    break;
  print 'after=',i
else:
  print 'else...i=',i

print '==試作=='
j = 0
for i in range(10):
  print 'i=',i
  print 'j=',j
  j += 1

print '％余りを取得'
x = 12
x %= 7
print x
x = 'hgoe'
y = 'fuga'
print x + y
