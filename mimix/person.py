import random


class Person:
    female_names = ['Olivia',
                    'Emma',
                    'Ava',
                    'Sophia',
                    'Isabella',
                    'Charlotte',
                    'Amelia',
                    'Mia',
                    'Harper',
                    'Evelyn',
                    'Abigail',
                    'Emily',
                    'Ella',
                    'Elizabeth',
                    'Camila',
                    'Luna',
                    'Sofia',
                    'Avery',
                    'Mila',
                    'Aria',
                    'Scarlett',
                    'Penelope',
                    'Layla',
                    'Chloe',
                    'Victoria',
                    'Madison',
                    'Eleanor',
                    'Grace',
                    'Nora',
                    'Riley',
                    'Zoey',
                    'Hannah',
                    'Hazel',
                    'Lily',
                    'Ellie',
                    'Violet',
                    'Lillian',
                    'Zoe',
                    'Stella',
                    'Aurora',
                    'Natalie',
                    'Emilia',
                    'Everly',
                    'Leah',
                    'Aubrey',
                    'Willow',
                    'Addison',
                    'Lucy',
                    'Audrey',
                    'Bella']
    male_names = ['Liam',
                  'Noah',
                  'Oliver',
                  'William',
                  'Elijah',
                  'James',
                  'Benjamin',
                  'Lucas',
                  'Mason',
                  'Ethan',
                  'Alexander',
                  'Henry',
                  'Jacob',
                  'Michael',
                  'Daniel',
                  'Logan',
                  'Jackson',
                  'Sebastian',
                  'Jack',
                  'Aiden',
                  'Owen',
                  'Samuel',
                  'Matthew',
                  'Joseph',
                  'Levi',
                  'Mateo',
                  'David',
                  'John',
                  'Wyatt',
                  'Carter',
                  'Julian',
                  'Luke',
                  'Grayson',
                  'Isaac',
                  'Jayden',
                  'Theodore',
                  'Gabriel',
                  'Anthony',
                  'Dylan',
                  'Leo',
                  'Lincoln',
                  'Jaxon',
                  'Asher',
                  'Christopher',
                  'Josiah',
                  'Andrew',
                  'Thomas',
                  'Joshua',
                  'Ezra',
                  'Hudson']
    surnames = ['Smith',
                'Johnson',
                'Williams',
                'Brown',
                'Jones',
                'Garcia',
                'Miller',
                'Davis',
                'Rodriguez',
                'Martinez',
                'Hernandez',
                'Lopez',
                'Gonzalez',
                'Wilson',
                'Anderson',
                'Thomas',
                'Taylor',
                'Moore',
                'Jackson',
                'Martin',
                'Lee',
                'Perez',
                'Thompson',
                'White',
                'Harris',
                'Sanchez',
                'Clark',
                'Ramirez',
                'Lewis',
                'Robinson',
                'Walker',
                'Young',
                'Allen',
                'King',
                'Wright',
                'Scott',
                'Torres',
                'Nguyen',
                'Hill',
                'Flores',
                'Green',
                'Adams',
                'Nelson',
                'Baker',
                'Hall',
                'Rivera',
                'Campbell',
                'Mitchell',
                'Carter',
                'Roberts']

    all_names = female_names + male_names

    def __init__(self):
        ...

    @classmethod
    def name(cls, gender='any'):
        def name_gen():
            if gender == 'f' or gender == 'female':
                ix = random.randint(0, len(cls.female_names) - 1)
                return cls.female_names[ix]
            elif gender == 'm' or gender == 'male':
                ix = random.randint(0, len(cls.male_names) - 1)
                return cls.male_names[ix]
            else:
                ix = random.randint(0, len(cls.all_names) - 1)
                return cls.all_names[ix]

        return lambda: name_gen()

    @classmethod
    def first_name(cls, gender='any'):
        def first_name_gen():
            if gender == 'f' or gender == 'female':
                ix = random.randint(0, len(cls.female_names) - 1)
                return cls.female_names[ix]
            elif gender == 'm' or gender == 'male':
                ix = random.randint(0, len(cls.male_names) - 1)
                return cls.male_names[ix]
            else:
                ix = random.randint(0, len(cls.all_names) - 1)
                return cls.all_names[ix]

        return lambda: first_name_gen()

    @classmethod
    def last_name(cls):
        def last_name_gen():
            ix = random.randint(0, len(cls.surnames) - 1)
            return cls.surnames[ix]

        return last_name_gen

    @classmethod
    def full_name(cls, gender='any'):
        def full_name_gen():
            f_name = cls.first_name(gender=gender)()
            l_name = cls.last_name()()
            return f'{f_name} {l_name}'

        return full_name_gen

    @classmethod
    def email(cls, first_name: str = None, last_name: str = None):
        def inner():
            f_name = first_name or cls.first_name()()
            l_name = last_name or cls.last_name()()
            return f'{f_name.lower()}.{l_name.lower()}@gmail.com'

        return inner
