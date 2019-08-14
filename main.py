print('Добро пожаловать в "Дезинтегратор 3000"')
gamer = {
    'name': input('Укажите Ваше имя: '),
    'age': int(input('Укажите Ваш возраст: ')),
    'sex': input('Укажите Ваш пол: '),
    'pet_name': input('Укажите имя Вашего питомца: '),
    'game_love': False,
}

if input('Вы любите играть?\n') == 'Да':
    gamer['game_love'] = True
else:
    gamer['game_love'] = False

access = True

if gamer['age'] < 18:
    access = False

elif gamer['age'] > 90:
    if input('Ваш возраст превышает 90 лет, игра для Вас может быть утомительной. Продолжить?\n') == 'Нет':
        access = False;
    elif input('Вы полностью уверены в своём решении?\n') == 'Нет':
        access = False;

if access:
    print('Приветсвую, ', gamer['name'])
    print('Я могу назвать буквы алфавита, которых нет в твоем имени.')
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for char in alphabet:
        if char in gamer['name'].lower():
            continue
        print(char)
else:
    print('Всего доброго,', gamer['name'])

