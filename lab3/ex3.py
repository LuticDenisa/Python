# dictionare egale sau nu, fara sa fol ==
def verif(dict1,dict2):
    if len(dict1) != len(dict2):
        return False

    for key,value in dict1.items():
        if not key in dict2.keys():
            return False
        if isinstance(value,dict):
            if not verif(value,dict2[key]):
                return False
        else:
            if value != dict2[key]:
                return False
    return True


dict1 = {'a':1, 'b':{'c':2,'d':[3, {'e':4}]}}
dict2 = {'a':1, 'b':{'c':2,'d':[3, {'e':4}]}}

print(verif(dict1,dict2))


