import nltk
groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
# target sentence
sent = "I shot an elephant in my pajamas"
tokens = nltk.word_tokenize(sent)
# tag tokens
tagged = nltk.pos_tag(tokens)
print tagged
# supposed result ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)


count = 0
for tree in parser.parse(tokens):
	print count
	print(tree)
	count = count + 1
# show the tree structure as a figure
tree.draw()
