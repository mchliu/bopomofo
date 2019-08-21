#!/usr/bin/env python3

import os
import subprocess as sp
import json
import sys
words = {}
words[""] = ""

def load(filename):
	tmp_words = json.loads(open(filename).read())
	words.update(tmp_words)

def getJiao(out, dup):
	data = (dict(list(words.items())[0::]).values())
	data = [x.rstrip('ˊ') for x in data]
	data = [x.rstrip('-') for x in data]
	data = [x.rstrip('ˋ') for x in data]
	data = [x.rstrip('ˇ') for x in data]
	jiao = [x[-1::] for x in data]

	for index in range(len(jiao)):
		if jiao[index] == inp:
			for i in range(len(data[index]) - 2):
				if data[index][-1-i] == ' ':
					if data[index][-3-i] == inp2:
						if index not in dup:
							if len(out)%5 == 0:
								print(len(out))
							out.append(list(words.keys())[index])
							dup.append(index)
						break
					else:
						break
		if len(out) == in_num:
			print(out)
			sys.exit()
	return 0

#main的概念
directory = os.path.dirname(os.path.realpath(__file__))

inp = input("單押>>> ")
inp2 = input("雙押>>> ")
in_num = int(input("要幾個>>>"))
out = []
dup = []

for root, dirnames, filenames in os.walk("%s/dict"%(directory)):
	for filename in filenames:
		load('%s/dict/%s'%(directory, filename))
		getJiao(out, dup)

try:
	load('%s/extension.dict'%(directory))
except:
	pass
