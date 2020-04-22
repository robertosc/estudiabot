dict = {'Rafael':["precalc", "calc1", "fisica1"], 'Domenico':['precalc', 'calc1, quimica']}

nombres = []#['Rafael', 'Domenico']

#print(dict(nombres[i] for i in nombres))
for i in dict:
    if "precalc" in dict[i]:
        nombres.append(i)

cursos_maulin = {"Maulin": [[12,13,14,15,16],'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']}
cursos_david = {"David": [[13,14,15,16,17],'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']}

lista= [cursos_david, cursos_maulin]
print(lista[1]['Maulin'])

