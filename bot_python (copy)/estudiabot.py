import telegram, logging

from telegram.ext import Updater
from telegram.ext import CommandHandler

from datetime import datetime
from time import sleep

#updater lo que hace es recibir la que se envía a Telegram
updater = Updater(token='822081181:AAHqSiiWPGeoKCcAaMPeMhWwMkCwkeH8vWI', use_context=True)

#para acceso más veloz a dispatcher
dispatcher = updater.dispatcher

#Se añade un logging para obtener info de las cosas que fallan, cuando y xq
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#globales
usuarios = {}

asignacion_calculo1 = {}
asignacion_calculo2 = {}
asignacion_calculo3 = {}
asignacion_fisica = {}


contador_mate = 0
contador_fisica = 0 
contador_quimica = 0

#Contactos
case1 = telegram.Contact(+50625110000, "CASE Ingeniería")

roberto = telegram.Contact(+50684069486, "Roberto")
cursos_robert = [[11,12,13,14], roberto, 'precalc', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

josue = telegram.Contact(+50689703121, "Josue")
cursos_josue = [[], josue, 'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']##

ricardo = telegram.Contact(+50687726153, "Ricardo")
cursos_ricardo = [[], ricardo, 'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']##

laura = telegram.Contact(+50689559126, "Laura")
cursos_lau = [[11,12,13,14], laura, 'precacl', 'calc1','fisica1', 'fisica2', 'ecua']

mateo = telegram.Contact(+50663940369, "Mateo")
cursos_mateo = [[10,11,12,13,14], mateo, 'precacl', 'calc1', 'fisica1', 'fisica3', 'fisica2']

joseluis = telegram.Contact(+50671036681, "Jose Luis")
cursos_josel = [[], joseluis, 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']##

domenico = telegram.Contact(+50670030300, "Domenico")
cursos_dome = [[9,10,11], domenico, 'precacl', 'calc1', 'quimica']

mariela = telegram.Contact(+50672004056, "Mariela")
cursos_mariela = [[13,14,15,16], mariela, 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

rafael = telegram.Contact(+50684449292, "Rafael")
cursos_rafa = [[9,10,11,12], rafael, 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

jean = telegram.Contact(+50687102598, "Jean")
cursos_jean = [[9,10,11,12,13,14], jean, 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

maulin = telegram.Contact(+50688108840, "Maulin")
cursos_maulin = [[12,13,14,15], maulin, 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

david = telegram.Contact(+506, "David")
cursos_david = [[13,14,15,16,17], david, 'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']


#nombres = ["Roberto", "Josue", "Ricardo", "David", "Maulin", "Jean", "Laura", "Domenico", "JoseL", "Mateo", "Rafa"]

lista_cursos_persona = [cursos_david, cursos_dome, cursos_jean, cursos_josel, cursos_josue, cursos_lau, cursos_mariela, cursos_mateo,
    cursos_maulin, cursos_rafa, cursos_ricardo, cursos_robert]

def horario(curso, hora): #Se le pasa un str con el curso
    lista_precal, lista_calculo, lista_calculo2, lista_calculo3, lista_fisica, lista_fisica2 , lista_fisica3 , lista_quimica , lista_quimica2 = ([] for i in range(9))

    for persona in lista_cursos_persona:
        #print(curso in persona[0])
        if hora in persona[0] and curso in persona:
            print(persona)


def selector(curso, firstname, lastname):
    
    hora = hora(1)

    lista_precal,lista_calculo, lista_calculo2, lista_calculo3, lista_fisica, lista_fisica2 , lista_fisica3 , lista_quimica , lista_quimica2 = ([] for i in range(9))







#Cada comando se añade como una funció:
def start(update, context):
    user = update.message.from_user
    bienvenida = f"¡Bienvenido al Bot del estudiadero de Ingeniería, {user['first_name']}! 🤖 \
            \nEntiendo los siguientes comandos: \n/info te brinda más información sobre el estudiadero \
            \n/ayuda te ofrece ayuda en tus materias \n/contacto te pone en contacto con soporte técnico \
            \n/horario te muestra el horario de atención\n/case te pasa el contacto del CASE de Ingeniería(nolista)"
    context.bot.send_message(chat_id=update.effective_chat.id, text=bienvenida)    
    usuarios[str(user['first_name']) + str(user['last_name'])] = user['id'] #Si una persona entra y 


def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Este Bot fue creado para ayudar a la población estudiantil en sus estudios durante la pandemia del CoVid-19. \
        Te permite ponerte en contacto con un facilitador del estudiadero que de dará asesoria en los cursos de Cálculo, Física y Química.\
        \nPara desplegar el menú escribe el comando /menu")


def menu(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text= "Entiendo los siguientes comandos:\n/info te brinda más información sobre el estudiadero\
        \n/ayuda te ofrece ayuda en tus materias \n/contacto te pone en contacto con soporte técnico\
        \n/horario te muestra el horario de atención\n/case te pasa el contacto del CASE de Ingeniería (nolista)") 

def contacto(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Si tienes alguna duda sobre el Bot, puedes contactar \
al desarrollador.")
    context.bot.send_contact(chat_id=update.effective_chat.id, contact = roberto)

def case(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Este es el contacto del CASE de Ingeniería")
    context.bot.send_contact(chat_id=update.effective_chat.id, contact = case1)


def contador(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text= f"{usuarios}")
    context.bot.send_message(chat_id = update.effective_chat.id, text= f"{asignacion_calculo1}")

def hora(opcion): #Opcion 1 devuelve hora como int, 2 devuelve hora completa con str
    now = datetime.now()
    if opcion==1:
        return int(now.strftime("%H"))
    else:
        return now.strftime("%H:%M")

def horario(update, context):
    current_time = hora(2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"El estudiadero está disponible de 9:00 a 18:00. \
    \nSon las {current_time}")

def ayuda(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¿Con qué curso necesitas ayuda?\n\
/calculo1\n/calculo2\n/calculo3\n/algebra lineal\n/ecuaciones diferenciales\n/fisica1\n\
/fisica2\n/fisica3\n/quimica1\n/quimica2")

def calculo1(update, context):
    global contador_mate

    #if contador_mate > len(lista_calculo1)-1:
    #    contador_mate = 0

    user = update.message.from_user
    hora1 = hora(1)
    contador_mate = turnos(str(user['first_name']), str(user['last_name']), contador_mate, asignacion_calculo1)

    if hora1 > 0 and hora1 < 24:
        context.bot.send_contact(chat_id=update.effective_chat.id, contact=lista_calculo1[asignacion_calculo1[str(user['first_name']) + str(user['last_name'])]])
        #telegram.Message(contact=roberto)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay")

def turnos(firstname, lastname, contador, dict_asignacion):
    if firstname+lastname not in dict_asignacion:
        dict_asignacion[firstname+lastname] = contador
        contador+=1
        return contador


#ARREGLAR CALCULO2

def calculo2(update, context):
    global contador_mate

    user = update.message.from_user
    hora1 = hora(1)
    contador_mate = turnos(str(user['first_name']), str(user['last_name']), contador_mate, asignacion_calculo1)

#    if hora1 > 0 and hora1 < 24:
#        context.bot.send_contact(chat_id=update.effective_chat.id, contact=lista_calculo2[asignacion_calculo1[str(user['first_name']) + str(user['last_name'])]])
#        #telegram.Message(contact=roberto)
#    else:
#        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay")










start_handler = CommandHandler('start', start)
time_handler = CommandHandler('horario', horario)
info_handler = CommandHandler('info', info)
menu_handler = CommandHandler('menu', menu)
contador_handler = CommandHandler('contador', contador)
ayuda_handler = CommandHandler('ayuda', ayuda)
calc1_handler = CommandHandler('calculo1', calculo1)
calc2_handler = CommandHandler('calculo2', calculo2)
#calc3_handler = CommandHandler('calculo3', calculo3)




contacto_handler = CommandHandler('contacto', contacto)
case_handler = CommandHandler('case', case)


dispatcher.add_handler(time_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(contador_handler)
dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(calc1_handler)
dispatcher.add_handler(calc2_handler)
#dispatcher.add_handler(calc3_handler)
dispatcher.add_handler(contacto_handler)
dispatcher.add_handler(case_handler)


updater.start_polling()

#sleep(25)
#updater.stop()
###print(bot.get_me())


