#!/usr/bin/python
# coding: utf-8

def add(x, y):
  return x + y

print add(1, 3)
print add('Hello', ',World')

bar = add
print 'bar=', bar(10, 20)

print '==='
i = int(raw_input('Enter number: '))
if i == 1:
  def foo(x, y):
    return x + y
else:
  def foo(x, y):
    return x - y

print 'foo=', foo(10, 5)

print '==lambda=='
a = [ lambda x, y: x + y, lambda x, y: x * y ]

for f in a:
  print f(10, 5)
