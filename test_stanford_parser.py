import os
from nltk.parse import stanford
import nltk
os.environ['STANFORD_PARSER'] = '/home/rmqlife/work/stanford-parser/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/home/rmqlife/work/stanford-parser/stanford-parser-3.7.0-models.jar'

parser = stanford.StanfordParser()

sent = "move near the red box and the blue crate"
tokens = nltk.word_tokenize(sent)

for tree in parser.parse(tokens):
	print(tree)
	tree.draw()
