import random

with open('words.txt', 'r', encoding = 'utf-8') as text:
        tx=text.read()

a = ['0','1','2','3','4','5','6','7','8','9','0']

for i in a:
    tx = tx.replace(i,'')
tx = tx.split()
word_new = random.choice(tx)
life = 0
word = []
stages = ["",
            "________        ",
            "|               ",
            "|        |      ",
            "|        0      ",
            "|       /|\     ",
            "|       / \     ",
            "|               "
            ]
for i in word_new:
    word.append(i)
letter_past = []
word_win = []
for i in range(0, len(word)):
    word_win.append('-')

print('Добро пожаловать в игру')
print(f'В загаданном слове {len(word)} букв')
print(*word_win)
while True:
    if len(word) == 0:
        print(f'Ура, победа! Слово: {word_new}')
        break
    letter = input('Введите букву: ')
    if len(letter) != 1:
        print('Только один символ!')
    elif letter in letter_past:
        print('Эта буква уже была!')
    elif letter in word:
        print('Молодец!')
        letter_past.append(letter)
        while letter in word:
            word.remove(letter)
        for index, i in enumerate(word_new):
            if i == letter:
                word_win[index] = letter
        print(*word_win)
    else:
        letter_past.append(letter)
        life = life + 1
        print('Неправильно!')
        print("\n".join(stages[:life]))
        if life == 8:
            print(f'Ты проиграл, слово было: {word_new}')
            break