

def qosu (birinshi_san, ekinshi_san):
    nat = birinshi_san + ekinshi_san
    print("eki sannyn kosyndysy:", nat)

def azaitu (birinshi_san, ekinshi_san):
    nat = birinshi_san - ekinshi_san
    print("eki sanynyn azaityndysy: ", nat)

def kobeitu (birinshi_san, ekinshi_san):
    nat = birinshi_san * ekinshi_san
    print("eki sanynyn kobeitinddisi: ", nat)

def bolu (birinshi_san, ekinshi_san):
    if ekinshi_san == 0:
        er_message = "sandy 0 ge boluge bolmaidy"
        print(er_message)
        return
    nat = birinshi_san / ekinshi_san
    print("eki sanynyn bolindisi: ", nat)
x = 2
while x > 0:
    san1 = int(input("birinshi sandy engiz: "))
    amal = input("amaldy engiziniz(+-*/): ")
    san2 = int(input("ekinshi sandy engiz: "))
    if(amal=="+"):
        qosu(san1, san2)
    elif(amal=="*"):
        kobeitu(san1,san2)
    elif(amal=="-"):
        azaitu(san1, san2)
    elif(amal=="/"):
        bolu(san1, san2)


