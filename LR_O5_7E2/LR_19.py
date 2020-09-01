
import random

WORDS = ('питон', 'анаграмма', 'простая', 'сложная', 'ответ', 'подстаканник','мизинец','жвачка','комиссия','бадминтон','рощ','помощь','пошагово','растет','дартс','триста','проект','коридор','корзина','рассвет')

word = random.choice(WORDS)
correct = word
jumble = ''

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print('Надо переставить буквы так, что бы получилось осмысленное слово.')
print('\nВот слово ', jumble)

guess = input('\nПопробуйте отгадать исходное слово: ')
while guess != correct and guess != '':
    print('не прав!')
    guess = input('Попробуйте еще раз: ')
    if guess == correct:
        print('Именно так!')
print('Спасибо за игру!')