#!/usr/bin/env python
#Author: Sheryl Joy S. Pascua
#Date: March 9, 2016
#Purpose: Python Script for displaying output in three ways

def FuncOut(name, age):
          print "Hi! My name is ", name + "and my age is", age
          print "Hi! My name is %s and my age is %d" %(name, age)
          print "Hi! My name is {} and my age is {}".format(name,age)

print FuncOut("Sheryl Joy Pascua", 19)
