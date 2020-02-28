import sys
sys.path.insert(1, 'code')
from util import ipa
from util import misc
from util import static
from pprint import pprint
import json

ipa_path = static.assets_path + 'ipa/'

def construct_vowels():
    l = []
    for p in ipa.vowel_properties:
        l.append(p.get_values())

    res = misc.tensor(*l)
    res1 = []
    for r in res:
        tmp = dict()
        for i in range(len(ipa.vowel_properties)):
            p = ipa.vowel_properties[i]
            tmp[p.name] = r[i]
        res1.append(tmp)
    
    vowels = dict()
    with open(ipa_path + 'vowels.json', 'r') as f:
        vowels = json.load(f)
    
    

    j = 0
    tmp_vowels = dict()
    def func(k):
        r = res1[k]
        short_name = []
        for i in range(len(ipa.vowel_properties)):
            p = ipa.vowel_properties[i]
            short = ipa.booklet[r[p.name]]
            short_name.append(short)
        short_name = '_'.join(short_name)
        if not short_name in vowels:
            symbol = input(short_name + ': ')
            r['symbol'] = symbol
            r['name'] = short_name

            if symbol.startswith('/prev'):
                l = symbol.split()
                skip = 0
                if len(l) == 1:
                    skip = 1
                else:
                    skip = int(l[1])
                if k - skip >= 0:
                    k -= skip
                else:
                    k = 0
                return k
            if symbol == '/null':
                r['symbol'] = 'NULL'
            
            if not symbol == '':
                tmp_vowels[short_name] = r
            
        k += 1
        return k

    while j < len(res1):
        print(j)
        j = func(j)

    for tr in tmp_vowels:
        if not tr in vowels:
            vowels[tr] = tmp_vowels[tr]

    pprint(vowels)

    with open(ipa_path + 'vowels.json', 'w') as f:
        json.dump(vowels, f, indent=4)
    return vowels

def construct_consonants():
    l = []
    for p in ipa.consonant_properties:
        l.append(p.get_values())

    res = misc.tensor(*l)
    res1 = []
    for r in res:
        tmp = dict()
        for i in range(len(ipa.consonant_properties)):
            p = ipa.consonant_properties[i]
            tmp[p.name] = r[i]
        res1.append(tmp)
    
    consonants = dict()
    with open(ipa_path + 'consonants.json', 'r') as f:
        consonants = json.load(f)
    
    

    j = 0
    tmp_consonants = dict()
    def func(k):
        r = res1[k]
        short_name = []
        for i in range(len(ipa.consonant_properties)):
            p = ipa.consonant_properties[i]
            short = ipa.booklet[r[p.name]]
            short_name.append(short)
        short_name = '_'.join(misc.cleanup(short_name))
        if not short_name in consonants:
            symbol = input(short_name + ': ')
            r['symbol'] = symbol
            r['name'] = short_name

            if symbol.startswith('/prev'):
                l = symbol.split()
                skip = 0
                if len(l) == 1:
                    skip = 1
                else:
                    skip = int(l[1])
                if k - skip >= 0:
                    k -= skip
                else:
                    k = 0
                return k
            if symbol == '/null':
                r['symbol'] = 'NULL'
            
            if not symbol == '':
                tmp_consonants[short_name] = r
            
        k += 1
        return k

    while j < len(res1):
        print(j)
        j = func(j)

    for tr in tmp_consonants:
        if not tr in consonants:
            consonants[tr] = tmp_consonants[tr]

    pprint(consonants)

    with open(ipa_path + 'consonants.json', 'w') as f:
        json.dump(consonants, f, indent=4)
    return consonants

construct_consonants()