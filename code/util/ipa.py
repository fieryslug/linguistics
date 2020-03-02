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
place = Property('place', ['bilabial', 'labiodental', 'linguolabial', 'dental', 'alveolar', 'postalveolar', 'retroflex', 'palatal', 'velar', 'uvular', 'pharyngeal', 'glottal'])
manner = Property('manner', ['plosive', 'fricative', 'affricate', 'nasal', 'trill', 'approximant', 'tap',
'lateral-fricative', 'lateral-affricate', 'lateral-approximant', 'lateral-tap', 'sibilant-fricative', 'sibilant-affricate'])



vowel_properties = [height, backness, roundedness]
consonant_properties = [voice, place, manner]

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
    'postalveolar': 'pal',
    'retroflex': 'rtf',

    'velar': 'vlr',
    'bilabial': 'blb',
    'labiodental': 'lbd',
    'linguolabial': 'lgl',
    'dental': 'dnt',
    'palatal': 'plt',
    'uvular': 'uvl',
    'pharyngeal': 'phr',
    'glottal': 'glt',

    'plosive': 'pls',
    'fricative': 'frc',
    'affricate': 'afr',
    'nasal': 'nsl',
    'trill': 'trl',
    'tap': 'tap',
    'approximant': 'apr',
    'lateral-fricative': 'lfr',
    'lateral-affricate': 'laf',
    'lateral-approximant': 'lap',
    'lateral-tap': 'ltp',
    'sibilant-fricative': 'sfr',
    'sibilant-affricate': 'saf',
    '': ''
})

booklet_inv = booklet.inverse