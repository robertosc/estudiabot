from datetime import datetime


cursos_robert = [[11,12,13,14],'precalc', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']


cursos_josue = [[],'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']##


cursos_ricardo = [[],'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']##

cursos_lau = [[11,12,13,14],'precacl', 'calc1','fisica1', 'fisica2', 'ecua']

cursos_mateo = [[10,11,12,13,14], 'precacl', 'calc1', 'fisica1', 'fisica3', 'fisica2']

cursos_josel = [[],'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']##

cursos_dome = [[9,10,11],'precacl', 'calc1', 'quimica']

cursos_mariela = [[13,14,15,16],'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

cursos_rafa =[[9,10,11,12],'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']


cursos_jean = [[9,10,11,12,13,14], 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

cursos_maulin = [[12,13,14,15],'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']


cursos_david = [[13,14,15,16,17],'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']

#nombres = ["Roberto", "Josue", "Ricardo", "David", "Maulin", "Jean", "Laura", "Domenico", "JoseL", "Mateo", "Rafa"]

lista_cursos_persona = [cursos_david, cursos_dome, cursos_jean, cursos_josel, cursos_josue, cursos_lau, cursos_mariela, cursos_mateo,
    cursos_maulin, cursos_rafa, cursos_ricardo, cursos_robert]


def horario(curso, hora): #Se le pasa un str con el curso
    lista_precal, lista_calculo, lista_calculo2, lista_calculo3, lista_fisica, lista_fisica2 , lista_fisica3 , lista_quimica , lista_quimica2 = ([] for i in range(9))
    #now = datetime.now()
    #hora = int(now.strftime("%H"))

    for persona in lista_cursos_persona:
        #print(curso in persona[0])
        if hora in persona[0] and curso in persona:
            print(persona)


horario('calc1', 10)