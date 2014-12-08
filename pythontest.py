#!/usr/bin/env python
import sys
import mod1
import mod2
#print sys.path

print "sum module test"
print str(mod1.sum(10, 20))
print
print "strsum module test"
print mod2.strsum("Hello", "World")