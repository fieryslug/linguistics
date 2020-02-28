from util.ipa import Consonant, Vowel, Feature


opn_frt_unr = Vowel('a', 'open', 'front', 'unrounded')
mid_frt_unr = Vowel('e', 'mid', 'front', 'unrounded')
cls_frt_unr = Vowel('i', 'close', 'front', 'unrounded')
mid_bck_rnd = Vowel('o', 'mid', 'back', 'rounded')
cls_bck_rnd = Vowel('u', 'close', 'back', 'rounded')

vcl_avl_pls = Consonant('t')
vcd_avl_pls = Consonant('d')




vowels = [
    opn_frt_unr,
    mid_frt_unr,
    cls_frt_unr,
    mid_bck_rnd,
    cls_bck_rnd
]

consonants = [
    vcl_avl_pls,
    vcd_avl_pls
]