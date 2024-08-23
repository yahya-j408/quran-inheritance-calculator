#!/usr/bin/env python3

from fractions import Fraction
import traceback, sys

_string_enf = 0x00
_number_enf = 0x02
_yn_enf = 0x04

_deceased_gender = _deceased_name = ""
_deceased_number_of_wives = 0
_deceased_surviving_spouse = _has_dad = _has_mom = False
_brothers = _sisters = _wives = _male_heirs = _female_heirs = [] 

print()
print("==== Quranic Inheritance Law Calculator (4:11, 4:12, 4:33, 4:176) ====")

def print_result_hdr():
    print()
    print("==== Results =====")
    print()

def _input(p, t=_string_enf):
    try:
        _k = ''
        while len(_k) < 1:
            _k = input("\n" + p + "\n")
            if t==_number_enf:
                try:
                    return int(_k)
                except ValueError:
                    print("Invalid number, try again.")
                    _k = ''
                    continue
            elif t==_yn_enf:
                if _k.upper() not in ('Y', 'N'):
                    print("'%s' is not a valid response, type either Y for yes or N for no." % _k)
                    _k = ''
                    continue
                else:
                    if _k.upper()=='Y':
                        _k = True
                    elif _k.upper()=='N':
                        _k = False
                    return _k
            if len(_k) < 1:
                print('Empty input, try again.')
        return _k
    except KeyboardInterrupt:
        print()
        print("Salam.")
        sys.exit(1)

def get_male_heirs():
    global _male_heirs
    _male_heirs = []
    for i in range(_input('How many living sons does %s have?' % _deceased_name, _number_enf)):
        _male_heirs.append(_input('Name of living son #%d: ' % (i+1)))

def get_brothers():
    global _brothers
    _brothers = []
    for i in range(_input('How many living brothers does %s have?' % _deceased_name, _number_enf)):
        _brothers.append(_input('Name of living brother #%d: ' % (i+1)))

def get_sisters():
    global _sisters
    _sisters = []
    for i in range(_input('How many living sisters does %s have?' % _deceased_name, _number_enf)):
        _sisters.append(_input('Name of living sister #%d: ' % (i+1)))

def get_female_heirs():
    global _female_heirs
    _female_heirs = []
    for i in range(_input('How many living daughters does %s have?' % _deceased_name, _number_enf)):
        _female_heirs.append(_input('Name of living daughter #%d: ' % (i+1)))

def get_parents():
    global _has_dad, _has_mom
    _has_dad = False
    _has_mom = False
    _has_dad = _input('Does %s have a living father (Y/N)?' % _deceased_name, _yn_enf)
    _has_mom = _input('Does %s have a living mother (Y/N)?' % _deceased_name, _yn_enf)

def get_deceased_gender():
    global _deceased_gender
    _deceased_gender = _input('Gender of %s (M for male, F for female): ' % _deceased_name)
    return _deceased_gender

def apply_411():
    global _female_heirs, _male_heirs
    results = dict()

    if len(_male_heirs)==0: # if no male heirs, the parents pool is 1/3
        female_heir_pool = Fraction(3, 3) # in this case even though there may not be 2 or more daughters, the pool starts out as theirs per 4:33, then is subject to further reductions
        dads_share = moms_share = 0
