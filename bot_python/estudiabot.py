import telegram, logging

from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram.ext import MessageHandler, Filters

from datetime import datetime
from time import sleep

#updater lo que hace es recibir la que se envía a Telegram
updater = Updater(token='822081181:AAHqSiiWPGeoKCcAaMPeMhWwMkCwkeH8vWI', use_context=True) #822081181:AAHqSiiWPGeoKCcAaMPeMhWwMkCwkeH8vWI


#para acceso más veloz a dispatcher
dispatcher = updater.dispatcher

#Se añade un logging para obtener info de las cosas que fallan, cuando y xq
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#globales
usuarios = {}

contador_precalc = contador_calc1 = contador_mates = 0
contador_fisica1 = contador_fisicas = 0 
contador_quimica = 0

#Contactos
case1 = telegram.Contact(+50625110000, "CASE Ingeniería")

#roberto = telegram.Contact(+50684069486, "@RobertoSanchezC")
cursos_robert = [[11,12,13,14], "@RobertoSanchezC" , 'precalc', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

#josue = telegram.Contact(+50689703121, "Josue")
cursos_josue = [[9,10,11,12], "@josue", 'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']##

#ricardo = telegram.Contact(+50687726153, "Ricardo") ##FALTA HORARIO
cursos_ricardo = [[11,12,13,15], "@ricardo", 'precacl', 'calc1','calc2','calc3', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']##

#laura = telegram.Contact(+50689559126, "Laura")
cursos_lau = [[11,12,13,14], "@laura", 'precacl', 'calc1','fisica1', 'fisica2', 'ecua']

#mateo = telegram.Contact(+50663940369, "Mateo")
cursos_mateo = [[10,11,12,13,14], "@mateo", 'precacl', 'calc1', 'fisica1', 'fisica3', 'fisica2']

#joseluis = telegram.Contact(+50671036681, "Jose Luis")
cursos_josel = [[], "@joseluis", 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']##

#domenico = telegram.Contact(+50670030300, "Domenico")
cursos_dome = [[9,10,11], "@domenico", 'precacl', 'calc1', 'quimica']

#mariela = telegram.Contact(+50672004056, "Mariela")
cursos_mariela = [[13,14,15,16], "@mariela", 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

#rafael = telegram.Contact(+50684449292, "Rafael")
cursos_rafa = [[9,10,11,12], "@rafael", 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

#jean = telegram.Contact(+50687102598, "Jean")
cursos_jean = [[9,10,11,12,13,14], "@jean", 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

#maulin = telegram.Contact(+50688108840, "Maulin")
cursos_maulin = [[12,13,14,15], "@maulin", 'precacl', 'calc1', 'calc3', 'fisica1', 'fisica3', 'ecua']

#david = telegram.Contact(+50689419343, "David")
cursos_david = [[13,14,15,16,17], "@david", 'precacl', 'calc1', 'fisica1', 'fisica2', 'fisica3', 'ecua', 'algebra']


#nombres = ["Roberto", "Josue", "Ricardo", "David", "Maulin", "Jean", "Laura", "Domenico", "JoseL", "Mateo", "Rafa"]

lista_cursos_persona = [cursos_ricardo ,cursos_robert, cursos_david, cursos_dome, cursos_jean, cursos_josel, cursos_josue, cursos_lau, cursos_mariela, cursos_mateo,
    cursos_maulin, cursos_rafa]

FIRST = range(1)
CALCULO1, CALCULO2, CALCULO3 = range(3)

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
al desarrollador: @RobertoSanchezC")
    #context.bot.send_contact(chat_id=update.effective_chat.id, contact = roberto)

def case(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Te adjunto el contacto del case, puedes llamar de 7am-4pm")
    context.bot.send_contact(chat_id=update.effective_chat.id, contact = case1)

def contador(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text= f"{usuarios}")
    context.bot.send_message(chat_id = update.effective_chat.id, text= f"{turnos_d}")

def hora(opcion): #Opcion 1 devuelve hora como int, 2 devuelve hora completa con str
    now = datetime.now()
    if opcion==1:
        return int(now.strftime("%H"))
    else:
        return now.strftime("%H:%M")

def horario(update, context):
    current_time = hora(2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"El estudiadero está disponible los viernes de 9:00 a 18:00. \
    \nSon las {current_time}")

def ayuda(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¿Con qué curso necesitas ayuda?\n\
/precalculo\n/calculo1\n/calculo2\n/calculo3\n/algebra lineal\n/ecuaciones diferenciales\n/fisica1\n\
/fisica2\n/fisica3\n/quimica1")

#def ayuda(update, context):
#    keyboard = [[telegram.InlineKeyboardButton("Cálculo 1", callback_data='calculo1'),
#                telegram.InlineKeyboardButton("Cálculo 2", callback_data='calculo2')],
#                [telegram.InlineKeyboardButton("Calculo 3", callback_data='calculo3')]]
#
#    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
#
#    update.message.reply_text('Please choose:', reply_markup=reply_markup)
#    return FIRST
#
#def button(update, context):
#    query = update.callback_query
#    query.answer()
#    query.edit_message_text(text="Selected option: {}".format(query.data))

turnos_d = {}

def turnos(firstname, lastname, contador, dict_asignacion, curso, hora):
    lista_asistentes = horario_asist(curso, hora)
    if lista_asistentes == 0:
        return 0, contador

    if contador >= len(lista_asistentes)-1:
        contador = 0 ####REVISAR SI PUEDE ESTAR AFUERA

    if firstname+lastname not in dict_asignacion:
        dict_asignacion[firstname+lastname] = {curso: contador}
    else:
        if curso not in dict_asignacion[firstname+lastname]:
            dict_asignacion[firstname+lastname][curso] = contador
            print(dict_asignacion[firstname+lastname])
    contador+=1
    #print(lista_asistentes[dict_asignacion[firstname+lastname][curso]])
    return lista_asistentes[dict_asignacion[firstname+lastname][curso]], contador

def horario_asist(curso, hora): #Se le pasa un str con el curso
    #lista_precal, lista_calculo, lista_calculo2, lista_calculo3, lista_fisica, lista_fisica2 , lista_fisica3 , lista_quimica , lista_quimica2 = ([] for i in range(9))
    lista_asistentes = []
    for persona in lista_cursos_persona:
        if hora in persona[0] and curso in persona:
            lista_asistentes.append(persona[1])
    if len(lista_asistentes) == 0:
        return 0
    return lista_asistentes

def sos(update, context):
    contact_keyboard = telegram.KeyboardButton(text="Enviar número telefónico para contacto", request_contact=True)
    custom_keyboard = [[contact_keyboard]]

    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text="¿Podrías enviarnos tu número de teléfono para ponernos en contacto contigo?",
        reply_markup=reply_markup)


def get_contact(update, context):
    contact = update.message.contact
    context.bot.send_message(chat_id=update.effective_chat.id, text="Serás contactado en breve. :)")
    context.bot.send_message(chat_id=-389144116, text=f"{contact['first_name']} necesita ayuda.")
    context.bot.send_contact(chat_id=-389144116, contact = contact)

    #context.bot.send_message(chat_id=-389144116, text=f"https://web.telegram.org/#/im?p=u{user['id']}")

def calculo1(update, context):
    global contador_calc1
    user = update.message.from_user
    now = hora(1)
    contacto_info, contador_calc1 = turnos(str(user['first_name']), str(user['last_name']), contador_calc1, turnos_d, 'calc1', now)
    
    # print(contacto_info)
    
    #contacto_a = telegram.Contact(contacto_info['phone_number'], contacto_info['first_name'])

    #context.bot.send_contact(chat_id=update.effective_chat.id, contact = contacto_a) ##ERROR

    if contacto_info == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay asesor disponible")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"Parece que necesitas ayuda en cálculo 1,\
puedes contactar a {contacto_info} para que te ayude. Si no te contesta en 10min, selecciona /sos y alguien te contactará")
        #context.bot.send_contact(chat_id=update.effective_chat.id, contact = contacto_a)
        #context.bot.send_contact(chat_id=update.effective_chat.id, contact = contacto_a[''])

def calculo2(update, context):
    global contador_mates

    user = update.message.from_user
    now = hora(1)
    contacto_info, contador_mates = turnos(str(user['first_name']), str(user['last_name']), contador_mates, turnos_d, 'calc2', now)
    if contacto_info == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay asesor disponible")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"Parece que necesitas ayuda en cálculo 2,\
        puedes contactar a {contacto_info} para que te ayude. Si no te contesta en 10min, selecciona /sos y\
        alguien te contactará")
        #context.bot.send_contact(chat_id=update.effective_chat.id, contact = contacto_a)
    
def calculo3(update, context):
    global contador_calc1
    user = update.message.from_user
    now = hora(1)
    contacto_info, contador_mates = turnos(str(user['first_name']), str(user['last_name']), contador_mates, turnos_d, 'calc3', now)
    if contacto_info == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay asesor disponible")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"Parece que necesitas ayuda en cálculo 3,\
        puedes contactar a {contacto_info} para que te ayude. Si no te contesta en 10min, selecciona /sos y alguien te contactará")
        #context.bot.send_contact(chat_id=update.effective_chat.id, contact = contacto_a)

def fisica1(update, context):
    global contador_fisica1
    user = update.message.from_user
    now = hora(1)
    contacto_info, contador_fisica1 = turnos(str(user['first_name']), str(user['last_name']), contador_fisica1, turnos_d, 'fisica1', now)
    if contacto_info == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay asesor disponible")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"Parece que necesitas ayuda en física 1,\
        puedes contactar a {contacto_info} para que te ayude. Si no te contesta en 10min, selecciona /sos y alguien te contactará")
        #context.bot.send_contact(chat_id=update.effective_chat.id, contact = contacto_a)

def fisica2(update, context):
    global contador_fisicas
    user = update.message.from_user
    now = hora(1)
    contacto_info, contador_fisicas = turnos(str(user['first_name']), str(user['last_name']), contador_fisicas, turnos_d, 'fisica2', now)
    if contacto_info == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay asesor disponible")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"Parece que necesitas ayuda en física 2,\
        puedes contactar a {contacto_info} para que te ayude. Si no te contesta en 10min, selecciona /sos y alguien te contactará")
        #context.bot.send_contact(chat_id=update.effective_chat.id, contact = contacto_a)

def fisica3(update, context):
    global contador_fisicas
    user = update.message.from_user
    now = hora(1)
    contacto_info, contador_fisicas = turnos(str(user['first_name']), str(user['last_name']), contador_fisicas, turnos_d, 'fisica3', now)
    if contacto_info == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay asesor disponible")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"Parece que necesitas ayuda en física 3,\
        puedes contactar a {contacto_info} para que te ayude. Si no te contesta en 10min, selecciona /sos y alguien te contactará")
        #context.bot.send_contact(chat_id=update.effective_chat.id, contact = contacto_a)

def quimica(update, context):
    global contador_quimica
    user = update.message.from_user
    now = hora(1)
    contacto_info, contador_quimica =  turnos(str(user['first_name']), str(user['last_name']), contador_fisicas, turnos_d, 'quimica', now)
    if contacto_info == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay asesor disponible")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"Parece que necesitas ayuda en física 3,\
        puedes contactar a {contacto_info} para que te ayude. Si no te contesta en 10min, selecciona /sos y alguien te contactará")



start_handler = CommandHandler('start', start)
time_handler = CommandHandler('horario', horario)
info_handler = CommandHandler('info', info)
menu_handler = CommandHandler('menu', menu)
contador_handler = CommandHandler('contador', contador)
ayuda_handler = CommandHandler('ayuda', ayuda)
calc1_handler = CommandHandler('calculo1', calculo1)
calc2_handler = CommandHandler('calculo2', calculo2)
calc3_handler = CommandHandler('calculo3', calculo3)
fisica1_handler = CommandHandler('fisica1', fisica1)
fisica2_handler = CommandHandler('fisica2', fisica2)
fisica3_handler = CommandHandler('fisica3', fisica3)
sos_handler = CommandHandler('sos', sos)


#conv_handler = ConversationHandler(
#        entry_points=[CommandHandler('start', start)],
#        states={
#            FIRST: [CallbackQueryHandler(calculo1, pattern='^' + str(CALCULO1) + '$'),
#                    CallbackQueryHandler(calculo2, pattern='^' + str(CALCULO2) + '$'),
#                    CallbackQueryHandler(calculo3, pattern='^' + str(CALCULO3) + '$')]
#        },
#        fallbacks=[CommandHandler('start', start)]
#    )

#dispatcher.add_handler(conv_handler)

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
dispatcher.add_handler(calc3_handler)
dispatcher.add_handler(contacto_handler)
dispatcher.add_handler(case_handler)
dispatcher.add_handler(fisica1_handler)
dispatcher.add_handler(fisica2_handler)
dispatcher.add_handler(fisica3_handler)


#updater.dispatcher.add_handler(CallbackQueryHandler(button))
dispatcher.add_handler(sos_handler)
dispatcher.add_handler(MessageHandler(Filters.contact, get_contact))
updater.start_polling()

#sleep(25)
#updater.stop()
###print(bot.get_me())


