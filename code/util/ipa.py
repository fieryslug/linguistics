from util.misc import bidict



class Sound:
    def __init__(self, ch):
        self._char = ch

    def get_char(self):
        return self._char


class Consonant(Sound):
    def __init__(self, ch):
        super().__init__(ch)




class Vowel(Sound):
    def __init__(self, ch, height, backness, roundedness):
        super().__init__(ch)
        self._height = height
        self._backness = backness
        self._roundedness = roundedness

    def get_height(self):
        return self._height

    def get_backness(self):
        return self._backness

    def get_roundedness(self):
        return self._roundedness



class Feature:
    def __init__(self):
        pass


class Property:
    def __init__(self, name, values=[]):
        self._values = values
        self.name = name

    def get_values(self):
        return self._values





height = Property('height', ['open', 'near-open', 'open-mid', 'mid', 'close-mid', 'near-close', 'close'])
backness = Property('backness', ['front', 'central', 'back'])
roundedness = Property('roundedness', ['rounded', 'unrounded'])


voice = Property('voice', ['voiced', 'voiceless'])
place = Property('place', ['alveolar', 'velar', 'bilabial', 'palatal', 'uvular', 'pharyngeal'])
manner = Property('manner', ['plosive', 'fricative', 'nasal', 'trill', 'tap', 'approximant'])
lateral = Property('lateral', ['lateral', ''])
sibilant = Property('sibilant', ['sibilant', ''])




vowel_properties = [height, backness, roundedness]
consonant_properties = [voice, place, manner, lateral, sibilant]

booklet = bidict({
    'open': 'opn',
    'near-open': 'nop',
    'open-mid': 'opm',
    'mid': 'mid',
    'close-mid': 'clm',
    'near-close': 'ncl',
    'close': 'cls',

    'front': 'frt',
    'central': 'cnt',
    'back': 'bck',
    
    'rounded': 'rnd',
    'unrounded': 'unr',

    'voiced': 'vcd',
    'voiceless': 'vcl',
    'alveolar': 'avl',
    'velar': 'vlr',
    'bilabial': 'blb',
    'palatal': 'plt',
    'uvular': 'uvl',
    'pharyngeal': 'phr',
    'plosive': 'pls',
    'fricative': 'frc',
    'nasal': 'nsl',
    'trill': 'trl',
    'tap': 'tap',
    'approximant': 'apr',
    'lateral': 'ltr',
    'sibilant': 'sbl',
    '': ''
})

booklet_inv = booklet.inverse