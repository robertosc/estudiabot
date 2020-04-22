contador_calc1 = 0
dicts = {"RobertoSanchez":{"quimica": 0, "calc1":1}}


def turnos(firstname, lastname, contador, dict_asignacion, curso):
    if firstname+lastname not in dict_asignacion:
        dict_asignacion[firstname+lastname] = {curso: contador}
    else:
        if curso not in dict_asignacion[firstname+lastname]:
            dict_asignacion[firstname+lastname][curso] = contador
            print(dict_asignacion[firstname+lastname])
    contador+=1
    return dict_asignacion[firstname+lastname][curso]

turnos("Roberto", "Sanche", contador_calc1, dicts, "quimicaa")

#print(dicts["RobertoSanchez"])
x = turnos("Roberto", "Sanche", contador_calc1, dicts, "quimic")
print(x)

