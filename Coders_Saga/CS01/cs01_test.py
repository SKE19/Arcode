'''Tester for CS01'''
from random import randint
import unittest
from unittest.mock import patch
from itertools import chain

import cs01 as cs

names = []

with open('dict.txt') as f:
    names = f.readlines()

def generate_errormancer():
    return randint(1,4), randint(1,30)

def validate_find_hero(heroes, attr, score):
    valid = []
    for hero in heroes:
        if heroes[hero][attr-1] >= score:
            if not heroes[hero][attr-1] > 30:
                valid.append(hero)
    if valid == []:
        return None
    return valid

def list_monsters(heroes):
    monsters = []
    for hero in heroes:
        for attrib in heroes[hero]:
            if int(attrib) >= 31:
                monsters.append(hero)
    if monsters == None:
        return [0]
    return monsters

def gen_char():
    return names.pop(randint(1,len(names))-1).removesuffix('\n'), [randint(1,30), randint(1,30), randint(1,30), randint(1,30)]

def make_char_list(number):
    characters = dict()
    if number < 1:
        return None
    for _ in range(number):
        name, stats = gen_char()
        characters[name] = stats
    return characters

def convert_to_list(entries):
    final_list = []
    for entry in entries:
        s = entry + ',' + ','.join(str(x) for x in entries[entry])
        final_list.append(s)
    return final_list

""" heroes = make_char_list(10)
attr, score = generate_errormancer()
print(validate_find_hero(heroes, attr, score))
convert_to_list(heroes) """

class TestCoderSaga(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestCoderSaga, self).__init__(*args, **kwargs)

        self.heroes_one = make_char_list(9)
        self.heroes_one.update(Brave = [30,30,30,30])
        self.heroes_two = make_char_list(10)
        self.heroes_two.update(NotAMonster = [31,31,31,31])
        self.heroes_three = make_char_list(999)
        self.heroes_four = make_char_list(998)
        self.heroes_four.update(DemonLord = [100, 100, 100, 100])
        
        self.case_one_input = list(chain(['10'], convert_to_list(self.heroes_one)))
        self.case_two_input = list(chain(['11'], convert_to_list(self.heroes_two)))
        self.case_three_input = list(chain(['999'], convert_to_list(self.heroes_three)))
        self.case_four_input = list(chain(['999'], convert_to_list(self.heroes_four)))

        self.case_one_attr, self.case_one_score = generate_errormancer()
        self.case_two_attr, self.case_two_score = generate_errormancer()
        self.case_three_attr, self.case_three_score = generate_errormancer()
        self.case_four_attr, self.case_four_score = generate_errormancer()

    def test_one(self):
        with patch('builtins.input', side_effect=self.case_one_input):
            ans = cs.find_hero(self.case_one_attr, self.case_one_score)
            monsters = list_monsters(self.heroes_one)
            self.assertEqual(ans, validate_find_hero(self.heroes_one, self.case_one_attr, self.case_one_score))
            if all([ans != None, validate_find_hero(self.heroes_one, self.case_one_attr, self.case_one_score) != None]):
                self.assertEqual(any(x in monsters for x in ans), False)

    def test_two(self):
        with patch('builtins.input', side_effect=self.case_two_input):
            ans = cs.find_hero(self.case_two_attr, self.case_two_score)
            monsters = list_monsters(self.heroes_two)
            self.assertEqual(ans, validate_find_hero(self.heroes_two, self.case_two_attr, self.case_two_score))
            if all([ans != None, validate_find_hero(self.heroes_two, self.case_two_attr, self.case_two_score) != None]):
                self.assertEqual(any(x in monsters for x in ans), False)
    
    def test_three(self):
        with patch('builtins.input', side_effect=self.case_three_input):
            ans = cs.find_hero(self.case_three_attr, self.case_three_score)
            monsters = list_monsters(self.heroes_three)
            self.assertEqual(ans, validate_find_hero(self.heroes_three, self.case_three_attr, self.case_three_score))
            if all([ans != None, validate_find_hero(self.heroes_three, self.case_three_attr, self.case_three_score) != None]):
                self.assertEqual(any(x in monsters for x in ans), False)

    def test_four(self):
        with patch('builtins.input', side_effect=self.case_four_input):
            ans = cs.find_hero(self.case_four_attr, self.case_four_score)
            monsters = list_monsters(self.heroes_four)
            self.assertEqual(ans, validate_find_hero(self.heroes_four, self.case_four_attr, self.case_four_score))
            if all([ans != None, validate_find_hero(self.heroes_four, self.case_four_attr, self.case_four_score) != None]):
                self.assertEqual(any(x in monsters for x in ans), False)

if __name__ == '__main__':
    unittest.main()