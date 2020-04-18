require 'telegram_bot'
token = '822081181:AAHqSiiWPGeoKCcAaMPeMhWwMkCwkeH8vWI'
bot = TelegramBot.new(token: token)


bot.get_updates(fail_silently: true) do |message|
    puts "@#{message.from.username}: #{message.text}"
    command = message.get_command_for(bot)

    message.reply do |reply|
        contador = 0
        
        case command
        when /start/i
            reply.text = ("¡Bienvenido al Bot del estudiadero de Ingeniería, #{message.from.first_name}! 🤖 
            \nEntiendo los siguientes comandos: \n/info te brinda más información sobre el estudiadero
/ayuda te ofrece opciones de ayuda en tus materias \n/contacto te pone en contacto con soporte técnico")
        when /info/i
            reply.text = ("Este Bot fue creado para ayudar a la población estudiantil en sus estudios durante la pandemia del CoVid-19. Te permite ponerte en contacto con un facilitador del estudiadero que de dará asesoria en los cursos de Cálculo, Física y Química.
\nPara desplegar el menú escribe el comando /menu")
        when /menu/i
            reply.text = ("Entiendo los siguientes comandos:\n/info te brinda más información sobre el estudiadero
/ayuda te ofrece opciones de ayuda en tus materias \n/contacto te pone en contacto con soporte técnico")
        else
            reply.text = "No sé que significa #{command.inspect}. Escribe /menu para ver opciones válidas."
        end
        puts "sending #{reply.text.inspect} to @#{message.from.username}"
        reply.send_with(bot)
    end
end