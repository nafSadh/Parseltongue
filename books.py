# -*- coding: utf-8 -*-
import unicodedata


def bn_digit(d):
    return unichr(ord(u'০')+d)


def bn_num(n):
    bn = ''
    while n>0:
        bn = bn_digit(n % 10)+bn
        n /= 10
    return bn


for i in xrange(50, 96):
    #print u'ন/হু '+bn_num(i)
    print 100170+i



