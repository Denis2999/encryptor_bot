import telebot
from cryptography.fernet import Fernet

API_TOKEN = '1549432801:AAGWmNkchUICa8GIF64kDSCb-L7YpMeyeRg'

bot = telebot.TeleBot(API_TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/decoding_text', '/decoding_file')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, send message or file!', reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, """\
Bot Commands:
[01] Start
/start
[02] Help
/help
[03] Decoding text
/decoding_text
[04] Decoding file
/decoding_file
""")


@bot.message_handler(commands=['decoding_text'])
def send_enctext_step(message):
    msg = bot.reply_to(message, "Send me text, you would like decrypt")
    bot.register_next_step_handler(msg, get_enctext_step)


def get_enctext_step(message):
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
        ['+', '-', '*', '/', '=', 'J', ';', ':', '(', ')'],
        ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И'],
        ['Й', 'К', 'Ч', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С'],
        ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
        ['Э', 'Ю', 'Я', 'Ї', 'Є', 'І', 'Ґ', 'Ą', 'Ć', 'Ę'],
        ['Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż', '%', '@', '#', '№'],
    ]

    coord = crypto(message.text)

    coord_1 = [coord.pop(0) for i in range(int(len(coord) / 2))]
    coord_2 = coord

    for i in range(len(coord_1)):
        coord_2.insert(i * 2, coord_1[i])

    half_coord_1 = coord_2[::2]
    half_coord_2 = coord_2[1::2]

    decoder_word = ""
    for i, j in zip(half_coord_1, half_coord_2):
        decoder_word = decoder_word + alphabet[i][j]

    bot.send_message(message.chat.id, decoder_word, reply_markup=keyboard1)


@bot.message_handler(commands=['decoding_file'])
def send_encfile_step(message):
    msg = bot.reply_to(message, "Send me file, you would like decrypt")
    bot.register_next_step_handler(msg, get_encfile_step)


def get_encfile_step(message):
    file_name = message.document.file_name
    file_id = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)

    src = file_name
    with open("C:\Python_telegram_bot\Encrypted_files\ " + src, 'wb') as new_file:
        new_file.write(downloaded_file)

    msg = bot.send_message(message.chat.id, 'Send me key, please')
    bot.register_next_step_handler(msg, get_key_step)

    file_source = "C:\Python_telegram_bot\Encrypted_files\ " + src
    return file_source


def get_key_step(message):
    file_name = message.document.file_name
    file_id = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)

    with open("C:\Python_telegram_bot\Encrypted_files\ " + 'mykey.key', 'wb') as new_file:
        new_file.write(downloaded_file)

    file_decrypt(file_source)

    bot.send_document(message.chat.id, open(get_encfile_step(message), 'rb'))


def file_decrypt(File_name):
    with open("C:\Python_telegram_bot\Encrypted_files\ " + 'mykey.key', 'rb') as mykey:
        key = mykey.read()
    print(key)
    print("File_name ", File_name)

    f = Fernet(key)
    with open(File_name, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(File_name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
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
        ['+', '-', '*', '/', '=', 'J', ';', ':', '(', ')'],
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


@bot.message_handler(content_types=['document'])
def get_file_message(message):
    file_name = message.document.file_name
    file_id = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)

    src = file_name
    with open("C:\Python_telegram_bot\Downloaded_files\ " + src, 'wb') as new_file:
        new_file.write(downloaded_file)

    file_encrypt(src)

    bot.send_document(message.chat.id, open("C:\Python_telegram_bot\Downloaded_files\ " + src, 'rb'))
    bot.send_document(message.chat.id, open("C:\Python_telegram_bot\Downloaded_files\ " + 'mykey.key', 'rb'),
                      reply_markup=keyboard1)


@bot.message_handler(content_types=['photo'])
def get_photo_message(message):
    print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    src = "image.jpg"
    with open("C:\Python_telegram_bot\Downloaded_files\ " + src, 'wb') as new_file:
        new_file.write(downloaded_file)

    file_encrypt(src)

    bot.send_document(message.chat.id, open("C:\Python_telegram_bot\Downloaded_files\ " + src, 'rb'))
    bot.send_document(message.chat.id, open("C:\Python_telegram_bot\Downloaded_files\ " + 'mykey.key', 'rb'),
                      reply_markup=keyboard1)


def file_encrypt(File_name):
    key = Fernet.generate_key()

    with open("C:\Python_telegram_bot\Downloaded_files\ " + 'mykey.key', 'wb') as mykey:
        mykey.write(key)
    with open("C:\Python_telegram_bot\Downloaded_files\ " + 'mykey.key', 'rb') as mykey:
        key = mykey.read()
    print("key is ", key)

    f = Fernet(key)
    with open("C:\Python_telegram_bot\Downloaded_files\ " + File_name, 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open("C:\Python_telegram_bot\Downloaded_files\ " + File_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


bot.polling(none_stop=True, interval=0)
