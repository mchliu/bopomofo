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

def getJiao(inp, out):
	data = (dict(list(words.items())[0::]).values())
	data = [x.rstrip('ˊ') for x in data]
	data = [x.rstrip('-') for x in data]
	data = [x.rstrip('ˋ') for x in data]
	data = [x.rstrip('ˇ') for x in data]
	jiao = [x[-1::] for x in data]
	for index in range(len(jiao)):
		if jiao[index] == inp:
			out.append(list(words.keys())[index])
		if len(out) % 30000 == 0:
			print(out)

directory = os.path.dirname(os.path.realpath(__file__))

inp = input(">>> ")
out = []

for root, dirnames, filenames in os.walk("%s/dict"%(directory)):
	for filename in filenames:
		load('%s/dict/%s'%(directory, filename))
		getJiao(inp, out)

try:
	load('%s/extension.dict'%(directory))
except:
	pass
