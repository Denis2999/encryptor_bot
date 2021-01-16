import telebot

bot = telebot.TeleBot('1549432801:AAGWmNkchUICa8GIF64kDSCb-L7YpMeyeRg')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Расшифровать текст', 'Расшифровать файл')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    def crypto(text="Sometext"):
        list_text = list(text.upper())
        number_text = ""
        coordinates = []
        for i in list_text:
            for index_list, char_list in enumerate(alphabet):
                joined_str = ''.join(char_list)
                if i in joined_str:
                    index_str = joined_str.index(i)
                    coordinates.append(index_list)
                    coordinates.append(index_str)
                    # print(index_list, index_str, end=" ", sep="")
                else:
                    number_text = i + i
        return coordinates

    alphabet = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z', ',', '.', '!', '?', ' '],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['+', '-', '*', '/', '=', '>', ';', ':', '(', ')'],
        ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И'],
        ['Й', 'К', 'Ч', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С'],
        ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
        ['Э', 'Ю', 'Я', 'Ї', 'Є', 'І', 'Ґ', 'Ą', 'Ć', 'Ę'],
        ['Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż', '%', '@', '#', '№'],

    ]

    coord = crypto(message.text)

    half_coord_1 = coord[::2]
    half_coord_2 = coord[1::2]
    new_coord = half_coord_1 + half_coord_2

    half_coord_3 = new_coord[::2]
    half_coord_4 = new_coord[1::2]

    encoder_word = ""
    for i, j in zip(half_coord_3, half_coord_4):
        encoder_word = encoder_word + alphabet[i][j]

    bot.send_message(message.chat.id, encoder_word, reply_markup=keyboard1)


# @bot.message_handler(commands=['Расшифровать текст'])
# def send_welcome(message):
#     bot.send_message('Расшифровать текст', 'Расшифровать файл')


@bot.message_handler(content_types=['document', 'photo'])
def get_file_messages(message):
    document_id = message.document.file_id
    file_info = bot.get_file(document_id)
    # urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}',
    #                            file_info.file_path)
    bot.send_message(message.chat.id, "document_id", reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)
