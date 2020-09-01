import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = {
    'Цвета': 'красный оранжевый желтый зеленый синий индиго фиолетовый белый черный коричневый'.split(),
    'фигуры': 'квадрат треугольник прямоугольник круг эллипс ромб трапеция шестиугольник пятиугольник восьмиугольник'.split(),
    'фрукты': 'яблоко апельсин лайм груша арбуз виноград грейпфрут вишня'.split(),
    'животные': 'бабуин барсук медведь бобр верблюд кошка кобра пума койот олень собака осел утка лиса лама обезьяна лось мышь выдра панда питон кролик баран крыса носорог тигра ласка кит волк вомбат зебра'.split(),
    'спорт': 'баскетбол футбол хоккей тенис биатлон бокс керлинг'.split(),
    'алкoголь': 'пиво шампанское вино коньяк виски водка ликер мартини сидр самагон абсент медовуха настойка брага бренди джин ром самбука'.split()
}


def getRandomWord(wordDict):
    # Эта функция возвращает случайное слово, которое выбирает из заранее созданного словаря
    # Сначала случайным образом выберем ключ из словаря
    wordKey = random.choice(list(wordDict.keys()))

    # Далее выберем случайное слово из списка, который соответствует выбранному ключу
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(HANGMANPICS, missedletters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Неправильные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '*' * len(secretWord)

    for i in range(len(secretWord)):  # Заменяем звездочки на правильно угаданные буквы
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # Показываем загаданное слово с пробелами между буквами
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Возвращает букву, которую ввел игрок. Эта функция проверяет, что введена буква, а не какой-то другой символ
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Ваша буква:')
        elif guess in alreadyGuessed:
            print('Вы уже пробовали эту букву. Выберите другую')
        elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Пожалуйста, введите букву кириллицы')
        else:
            return guess


def playAgain():
    # Эта функция возвращает True если игрок решит сыграть еще раз. В противном случае возвращается False
    print('Хотите попробовать еще раз? ("Да" или "Нет")')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:
    print('Секретное слово относится к категории: ' + secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Вычисляем количество букв, которые ввел игрок

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Проверка условия победы игрока
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Превосходно! Было загадано слово "' + secretWord + '"! Вы победили!')

            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверка условия проигрыша игрока
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('У вас не осталось попыток!\nПосле ' + str(len(missedLetters)) + ' ошибок и ' + str(
                len(correctLetters)) + 'угаданных букв. Загаданное слово:' + secretWord + '"')
            gameIsDone = True
    # Спрашиваем, хочет ли игрок сыграть еще раз.

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretKey = getRandomWord(words)
        else:
            break