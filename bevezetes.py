def feladat1():
    Jatekos_neve = input("Kérem, adja meg a játékos nevét: ")
    Szerepkor= input("Kérem, adja meg a szerepkört: ")
    if "varázsló" in Szerepkor: 
        print("Üdvözlunk{Jatekos_neve},2 életed van")
    elif"harcos"in Szerepkor:
        print("Üdvözlünk{Jatekos_neve},10 élete van")
    else:
         print("üdvözlünk {Jatekos_neve} 8 élete van")




  