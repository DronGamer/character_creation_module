from random import randint


# Все базовые параметры в одном словаре
GAME_CONSTANTS = {
    'base_stats': {
        'attack': 5,
        'defence': 10,
        'stamina': 80
    },
    'bonus': {'min': 10, 'max': 40},
    'crit': {'min': 5, 'max': 12},
    'dmg_multiple': 2
}

# Описания классов
CLASS_DESCRIPTIONS = {
    'warrior': ('Воитель — дерзкий воин ближнего боя. '
                'Сильный, выносливый и отважный.'),
    'mage': ('Маг — находчивый воин дальнего боя. '
             'Обладает высоким интеллектом.'),
    'healer': ('Лекарь — могущественный заклинатель. '
               'Черпает силы из природы, веры и духов.')
}

# Характеристики классов
CHAR_CLASSES = {
    'warrior': {
        'description': '{name}, ты Воитель — отличный боец ближнего боя.',
        'attack': (3, 9),
        'defence': (5, 10),
        'special': ('Выносливость', 'stamina')
    },
    'mage': {
        'description': '{name}, ты Маг — превосходный укротитель стихий.',
        'attack': (5, 10),
        'defence': (-2, 2),
        'special': ('Атака', 'attack')
    },
    'healer': {
        'description': '{name}, ты Лекарь — чародей, исцеляющий раны.',
        'attack': (-3, -1),
        'defence': (2, 5),
        'special': ('Защита', 'defence')
    }
}

# Тексты игры
GAME_TEXTS = {
    'welcome': ('Приветствую тебя, искатель приключений!\n'
                'Кто же ты, путник?'),
    'stats': ('Здравствуй, {name}!\n'
              'Сейчас твоя выносливость — {stamina}, '
              'атака — {attack}, защита — {defence}.\n'
              'Ты можешь выбрать один из трёх путей силы: '
              'Воитель, Маг, Лекарь'),
    'training': ('Потренируйся управлять своими навыками.\n'
                 "Введи команду: 'attack' — атаковать, "
                 "'defence' — блокировать, 'special' — суперсила.\n"
                 "Для пропуска введи 'skip'.")
}

# Команды для тренировки
COMMANDS = {
    'attack': lambda name, cls: attack(name, cls),
    'defence': lambda name, cls: defence(name, cls),
    'special': lambda name, cls: special(name, cls)
}


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи класс (warrior, mage, healer): ')
        if char_class in CLASS_DESCRIPTIONS:
            print(CLASS_DESCRIPTIONS[char_class])
        else:
            print('Такого класса нет, выбери из: warrior, mage, healer')
        approve_choice = input('Подтвердить (Y) или выбрать снова '
                               '(любой символ): ').lower()
    return char_class


def attack(char_name, char_class):
    damage_range = CHAR_CLASSES[char_class]['attack']
    damage = (GAME_CONSTANTS['base_stats']['attack'] +
              randint(*damage_range))
    return f'{char_name} нанёс урон противнику равный {damage}'


def defence(char_name, char_class):
    block_range = CHAR_CLASSES[char_class]['defence']
    block = (GAME_CONSTANTS['base_stats']['defence'] +
             randint(*block_range))
    return f'{char_name} блокировал {block} урона'


def special(char_name, char_class):
    special_name, base_stat_key = CHAR_CLASSES[char_class]['special']
    base_value = GAME_CONSTANTS['base_stats'][base_stat_key]
    rand_bonus = randint(GAME_CONSTANTS['bonus']['min'],
                         GAME_CONSTANTS['bonus']['max'])
    crit = randint(GAME_CONSTANTS['crit']['min'],
                   GAME_CONSTANTS['crit']['max'])
    bonus = crit * GAME_CONSTANTS['dmg_multiple']
    special_value = base_value + rand_bonus + bonus
    return f'{char_name} применил «{special_name} {special_value}»'


def start_training(char_name, char_class):
    print(CHAR_CLASSES[char_class]['description'].format(name=char_name))
    print(GAME_TEXTS['training'])
    while True:
        cmd = input('Введи команду: ')
        if cmd == 'skip':
            break
        elif cmd in COMMANDS:
            print(COMMANDS[cmd](char_name, char_class))
        else:
            print('Неизвестная команда!')
    return 'Тренировка окончена.'


def main():
    print(GAME_TEXTS['welcome'])
    char_name = input('...назови себя: ')
    stats = GAME_CONSTANTS['base_stats']
    print(GAME_TEXTS['stats'].format(name=char_name, **stats))
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


if __name__ == '__main__':
   main()
   