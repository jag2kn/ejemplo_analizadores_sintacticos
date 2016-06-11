import nltk
from nltk import CFG

grammar = CFG.fromstring("""
	S -> NP VP
	NP -> Det Noun | Noun Adj
	VP -> Verb NP
	Det -> 'el'
	Noun -> 'gato' | 'pescado'
	Verb -> 'come'
	Adj -> 'crudo'
	""")

def dibujo_arbol(texto):
	sent = texto.split()
	parser = nltk.ChartParser(grammar)
	for tree in parser.parse(sent):
		print(tree)
		tree.draw()


dibujo_arbol('el gato come pescado crudo')
dibujo_arbol('gato crudo come el gato')
dibujo_arbol('el pescado come gato crudo')
	

