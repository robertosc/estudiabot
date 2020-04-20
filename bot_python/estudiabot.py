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


contador_mate = 0

#Contactos
case = telegram.Contact(+50625110000, "Case")
roberto = telegram.Contact(+50684069486, "Roberto")
josue = telegram.Contact(+50689703121, "Josue")
ricardo = telegram.Contact(+50687726153, "Ricardo")

lista_calculo1 = [roberto, josue, ricardo] 
lista_calculo2 = []
lista_calculo3 = []
lista_fisica1 = []

#Cada comando se añade como una funció:
def start(update, context):
    user = update.message.from_user
    bienvenida = f"¡Bienvenido al Bot del estudiadero de Ingeniería, {user['first_name']}! 🤖 \
            \nEntiendo los siguientes comandos: \n/info te brinda más información sobre el estudiadero \
            \n/ayuda te ofrece opciones de ayuda en tus materias \n/contacto te pone en contacto con soporte técnico \
            \n/horario te muestra el horario de atención\n/case te pasa el contacto del CASE de Ingeniería(nolista)"
    context.bot.send_message(chat_id=update.effective_chat.id, text=bienvenida)    
    usuarios[str(user['first_name']) + str(user['last_name'])] = user['id'] #Si una persona entra y 


def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Este Bot fue creado para ayudar a la población estudiantil en sus estudios durante la pandemia del CoVid-19. \
        Te permite ponerte en contacto con un facilitador del estudiadero que de dará asesoria en los cursos de Cálculo, Física y Química.\
        \nPara desplegar el menú escribe el comando /menu")


def menu(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text= "Entiendo los siguientes comandos:\n/info te brinda más información sobre el estudiadero\
        \n/ayuda te ofrece opciones de ayuda en tus materias \n/contacto te pone en contacto con soporte técnico\
        \n/horario te muestra el horario de atención\n/case te pasa el contacto del CASE de Ingeniería (nolista)") 

def contacto(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Si tienes alguna duda sobre el Bot, puedes contactar\
al desarrollador.")
    context.bot.send_contact(chat_id=update.effective_chat.id, contact = roberto)

def case(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Este es el contacto del CASE de Ingeniería")
    context.bot.send_contact(chat_id=update.effective_chat.id, contact = case)


def contador(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text= f"{usuarios}")
    context.bot.send_message(chat_id = update.effective_chat.id, text= f"{asignacion_calculo1}")



def horario(update, context):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"El estudiadero está disponible\
        de 9:00am a 6:00pm. \nSon las {current_time}")

def ayuda(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¿Con qué curso necesitas ayuda?\n\
/calculo1\n/calculo2\n/calculo3\n/algebra lineal\n/ecuaciones diferenciales\n/fisica1\n\
/fisica2\n/fisica3\n/quimica1\n/quimica2")

def calculo1(update, context):
    global contador_mate

    if contador_mate > len(lista_calculo1)-1:
        contador_mate = 0

    user = update.message.from_user
    now = datetime.now()
    hora = int(now.strftime("%H"))

    if str(user['first_name']) + str(user['last_name']) not in asignacion_calculo1:
        asignacion_calculo1[str(user['first_name']) + str(user['last_name'])] = contador_mate
        contador_mate +=1
    

    if hora > 0 and hora < 24:
        context.bot.send_contact(chat_id=update.effective_chat.id, contact=lista_calculo1[asignacion_calculo1[str(user['first_name']) + str(user['last_name'])]])
        #telegram.Message(contact=roberto)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "No hay")




start_handler = CommandHandler('start', start)
time_handler = CommandHandler('horario', horario)
info_handler = CommandHandler('info', info)
menu_handler = CommandHandler('menu', menu)
contador_handler = CommandHandler('contador', contador)
ayuda_handler = CommandHandler('ayuda', ayuda)
calc1_handler = CommandHandler('calculo1', calculo1)
contacto_handler = CommandHandler('contacto', contacto)
case_handler = CommandHandler('case', case)


dispatcher.add_handler(time_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(contador_handler)
dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(calc1_handler)
dispatcher.add_handler(contacto_handler)
dispatcher.add_handler(case_handler)


updater.start_polling()

#sleep(25)
#updater.stop()
###print(bot.get_me())


