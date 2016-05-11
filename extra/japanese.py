#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
count=0
def isHiragana(char):
    #引数がひらがなならTrue、さもなければFalseを返す
    if u'ぁ' <= char <= u'ん':
        return True
    return False

def isKatakana(char):
        #引数がカタカナならTrue,さもなければFalseを返す
	if  u'ァ' <= char <= u'ン':
		return True
	return False

def isKanji(char):
        #引数が漢字ならTrue,さもなければFalseを返す
	if u'一' <= char <= u'龥':
		return True
	return False

def isAlphabet(char):
	#引数がアルファベットならTrue,さもなければFalseを返す
	if u'a' <= char <= u'z' or u'A' <= char <= u'Z':
		return True
	return False 

def Hiragana(string,count):
        #引数の中のひらがなを返す
	string = unicode(string, 'utf-8')
	for i in string:
		if isHiragana(i):
#			print i.encode("utf-8"),
                        count+=1;
#	print "\n"
        return count

def Katakana(string,count):
        #引数の中のカタカナを返す
	string = unicode(string,'utf-8')
	for i in string:
		if isKatakana(i):
		#	print i.encode("utf-8"),
                        count+=1
#	print "\n"
        return count

def Kanji(string,count):
        #引数の中の漢字を返す
	string = unicode(string,'utf-8')
	for i in string:
		if isKanji(i):
		#	print i.encode("utf-8"),
                        count+=1
	#print "\n"
        return count
def Alphabet(string,count):
        #引数の中のアルファベットを返す
	string = unicode(string,'utf-8')
	for i in string:
		if isAlphabet(i):
			#print i.encode("utf-8"),
			count+=0
	#print "\n"

def charAnalysis(string,count):
        #引数をひらがな、カタカナ、漢字、アルファベットに分離する
	count=Hiragana(string,count)
	count=Katakana(string,count)
	count=Kanji(string,count)
	Alphabet(string,count)
        return count

param=sys.argv[1]
count=charAnalysis(param,count)
#print count

if count>0:
	print u'日本語版'
else:
	print u'多言語版'




