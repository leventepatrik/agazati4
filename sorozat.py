import random

def dobas():
    eredmenyek=[]
    for i in range(0,7,1):
        eredmenyek.append(random.randint(0,1))
        return eredmenyek
                    

def fejek_szama(eredmenyek):
    return eredmenyek.count(1)



    