def cleanup(l):
    l1 = []
    for c in l:
        if not c == '':
            l1.append(c)
    return l1


def tensor(*b_list):
    if len(b_list) == 1:
        return [[k] for k in b_list[0]]
    
    b = b_list[-1]
    b_list_1 = b_list[:-1]

    
    tmp = tensor(*b_list_1)
    res = []
    for k in b:
        for k0 in tmp:
            res.append(k0 + [k])
    return res

class bidict(dict):
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value,[]).append(key) 

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key) 
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value,[]).append(key)        

    def __delitem__(self, key):
        self.inverse.setdefault(self[key],[]).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]: 
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)


