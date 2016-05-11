#!/usr/bin/env python
# -*- coding: utf-8 -*-
import japanese
import sys 


#日本語の個数の変数
count=0
#引数
word =sys.argv[1]
count=japanese.charAnalysis(word,count)
#print count

if count>0:
    import japan_rest
else:
    import fore_rest
