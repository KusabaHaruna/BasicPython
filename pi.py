#問２ 文字列

#Text = ["How", "I", "want", "a", "drink", "alcoholic", "of", "course", "after", "the", "heavy", "chapters", "involving","quantum","mechanis","All","of","thy","geometry","Herr","planck","is","fairely","haed"]
#print(list(map(len, Text)))
text = " How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard"
txt=list(map(len,text.replace(","," ").replace("."," ").split()))
print(txt)

result = "".join(map(str,txt))

print(result)

#print(text.splitlines())
#print(len(text.splitlines()))
#print([len(line) for line in text.splitlines()])

