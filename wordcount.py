#Funsión para contar palabras en un texto plano.
text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar."
separedText = text.lower().replace(",","").replace(".","").split()
wcount = {word: separedText.count(word) for word in separedText}
print(dict(sorted(wcount.items(), key=lambda x: x[1], reverse=True)))
