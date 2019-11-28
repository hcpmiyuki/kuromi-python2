from janome.tokenizer import Tokenizer
 
t = Tokenizer()
tokens = t.tokenize(u'pythonの本を読んだ')
 
for token in tokens:
    print(token)
