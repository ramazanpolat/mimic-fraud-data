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
    def first_name(cls, gender=None):
        if gender == 'f' or gender == 'female':
            ix = random.randint(0, len(cls.female_names) - 1)
            return cls.female_names[ix]
        elif gender == 'm' or gender == 'male':
            ix = random.randint(0, len(cls.male_names) - 1)
            return cls.male_names[ix]
        else:
            ix = random.randint(0, len(cls.all_names) - 1)
            return cls.all_names[ix]

    @classmethod
    def last_name(cls):
        ix = random.randint(0, len(cls.surnames) - 1)
        return cls.surnames[ix]

    @classmethod
    def full_name(cls, gender='any'):
        f_name = cls.first_name(gender=gender)
        l_name = cls.last_name()
        return f'{f_name} {l_name}'

    @classmethod
    def email(cls, first_name: str = None, last_name: str = None, domain=None):
        f_name = first_name or cls.first_name()()
        l_name = last_name or cls.last_name()()
        middle = random.choice(['', '.'])
        if middle == '':
            f_name = random.choice([f_name, f_name[0]])
        if domain:
            provider = domain
        else:
            provider = random.choice(
                ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'me.com', 'apple.com', 'nasa.gov'])
        suffix = ''
        if random.choice([True, False]):
            suffix = random.randint(1, 100)
        return f'{f_name.lower()}{middle}{l_name.lower()}{suffix}@{provider}'

    @classmethod
    def gender(cls, short=False):
        g = random.choice(['Male', 'Female'])
        if short:
            g = g[0]
        return g

    @classmethod
    def race(cls):
        return random.choice(['Black', 'White', 'Asian', 'Caucasian'])

    @classmethod
    def username(cls, first_name: str = None, last_name: str = None):
        f_name = first_name or cls.first_name()()
        l_name = last_name or cls.last_name()()
        suffix = ''
        if random.choice([True, False]):
            suffix = random.randint(1, 100)
        return f'{f_name.lower()}{l_name.lower()}{suffix}'

    @classmethod
    def password(cls):
        return None

    @classmethod
    def phone(cls, mobile=True, country=None):
        return None

    @classmethod
    def birth_date(cls, start=1980, end=2000):
        return None
