from telegram import ReplyKeyboardMarkup
import random

word_win = []
stages = ["",
            "________        ",
            "|               ",
            "|        |      ",
            "|        0      ",
            "|       /|\     ",
            "|       / \     ",
            "|               "
            ]

life = 0
letter_past = []
word = []
letter = '.'

def keyboard():
    return ReplyKeyboardMarkup('Начать игру')



def start_game(bot, update):
    update.message.reply_text('Добро пожаловать в игру Висилица!')
    reply_keyboard = [['Старт']]
    update.message.reply_text('Для начала игры нажмите Старт',
            reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True, resize_keyboard = True)
            )
    return 'game'


def game_play(bot, update):
    with open('words.txt', 'r', encoding = 'utf-8') as text:
        tx=text.read()

    a = ['0','1','2','3','4','5','6','7','8','9','0']
    for i in a:
        tx = tx.replace(i,'')
    tx = tx.split()
    global letter_past
    letter_past = []
    global word_new
    word_new = 'a'
    word_new = random.choice(tx)
    global word
    word = []
    for i in word_new:
        word.append(i)
    global word_win
    word_win = []
    for i in range(0, len(word)):
        word_win.append('-')
    global life
    life = 0
    update.message.reply_text('Добро пожаловать в игру')
    update.message.reply_text(f'В загаданном слове {len(word)} букв')
    update.message.reply_text(word_win)
    update.message.reply_text('Введите букву: ')
    return 'letter_game'

def let_game(bot, update):
    global letter
    letter = update.message.text.lower()
    if len(letter) != 1:
        update.message.reply_text('Только один символ!')
        update.message.reply_text('Введите букву: ')
        return 'letter_game'
    elif letter in letter_past:
        update.message.reply_text('Эта буква уже была!')
        update.message.reply_text('Введите букву: ')
        return 'letter_game'

    reply_keyboard = [['ДААаа!']]
    
    if letter in word:
        update.message.reply_text('Молодец!')
        letter_past.append(letter)
        while letter in word:
            word.remove(letter)
        for index, i in enumerate(word_new):
            if i == letter:
                word_win[index] = letter
        update.message.reply_text(str(word_win))
    else:
        letter_past.append(letter)
        global life
        life = life + 1
        update.message.reply_text('Неправильно!')
        update.message.reply_text("\n".join(stages[:life]))
        if life == 8:
            update.message.reply_text(f'Ты проиграл, слово было: {word_new}')
            update.message.reply_text('Сыграем еще?',
            reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True, resize_keyboard = True)
            )
            return 'game'
       
    if len(word) == 0:
        update.message.reply_text(f'Ура, победа! Слово: {word_new}')
        update.message.reply_text(f'Поиграем еще?',
            reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True, resize_keyboard = True)
            )
        return 'game'
    update.message.reply_text('Введите букву: ')