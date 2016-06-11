import nltk
import ancora
path = 'ancora/ancora-3.0.1es/'
corpus = ancora.AncoraCorpusReader(path)


t = corpus.parsed_sents()[0]
t.draw()
t.productions()

prods = []
for t in corpus.parsed_sents():
    prods += t.productions()
    
#print (prods)

S = nltk.Nonterminal('sentence')
grammar = nltk.induce_pcfg(S, prods)



#prods2 = grammar.productions(lhs=nltk.Nonterminal('ncms000'))
#print (prods2)

print ("===============================================================")
print ("===============================================================")

parser = nltk.ViterbiParser(grammar)
for tree in parser.parse("El gato come pescado crudo .".split()):
    print (tree)
    tree.draw()
    tree.prob()












