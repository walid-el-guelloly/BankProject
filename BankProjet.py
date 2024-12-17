class CompteBancaire : 
    def __init__(self,numerocompte,nom,solde,dhs) : 
        self.numerocompte = numerocompte
        self.nom = nom
        self.solde = solde
        self.g = None

    def VersementRetrait(self) :
        print("choisis parmi les deux : ")
        self.g = int(input("Versement = 1 / Retrait = 2 : "))
        if self.g == 1 :
            self.x = int(input("Entrer combien tu doit verser :  "))
            self.solde = self.solde + self.x
            print("Votre solde totole apres le versement est : ",self.solde, "$")
        elif self.g == 2 :
            while True : 
                self.y = int(input("Entrer le montant de retrait : "))
                if  self.y <= self.solde :
                    self.solde = self.solde - self.y
                    print("Votre solde totole apres le retrait est : ",self.solde, "$")
                    break
                else : 
                    print("Erreur! impossible de retrait un montant sup que votre solde totale ")

    def Login(self) :
        print("\033[32m------------ Login ------------\033[0m")
        pass
        U = str(input("Username : "))
        pass
        print("-----------------------------")
        pass
        p = input("Password : ")
        pass


    def affichage(self):
        print(f"\033[32m--------- Bienvenue {b}---------\033[0m") 
        pass
        print("• Numero de compte est : ",self.numerocompte)
        print("• Votre Nom complet est : ",b)
        print("• Votre solde est : ",self.solde, "$")
        pass
        print("\033[32m-------------- Opération -------------- \033[0m")
    
    def Recu(self) :
        while True : 
            R = int(input("Appuyer sur 1 pour decouvrire votre recu Banquaire : "))  
            if R == 1 :
                print("\033[32m+-----------Recu Bancaire--------------+\033[0m")
                pass
                if self.g == 1 :
                    print("|•Nom Complet :               ")
                    print("|\033[32m      ",b,"       \033[0m")
                    print("|•Numero de compte :          ")
                    print("|\033[32m      1865247               \033[0m")
                    print("|•Operation éfectuée :        ")
                    print("|\033[32m      versement,            \033[0m")
                    print("|•Montant de Versement :      ")
                    print("|\033[32m      ",self.x,"$" "            \033[0m")
                    pass
                elif self.g == 2 :
                    print("|•Nom Complet :               ")
                    print("|\033[32m      ",b,"                 \033[0m")
                    print("|•Numero de compte :          ")
                    print("|\033[32m      1865247               \033[0m")
                    print("|•Operation éfectuée :        ")
                    print("|\033[32m      Retrait,              \033[0m")
                    print("|•Montant de Versement :      ")
                    print("|\033[32m      ",self.y,"$""            \033[0m")
                    pass
                print("|.")
                print("|"                   "Merci de vous utiliser Snail Bank!")
                print("\033[32m+---------------------------------------+\033[0m")
                break
            else : 
                print("Erreur! vous devez appuyer sur 1 ")    
            
    
b = str(input("Entrer Votre Nom Complet : ")).title()
 
User1 = CompteBancaire(1865247, b, 500, "$")
User1.Login()
User1.affichage()
User1.VersementRetrait()
User1.Recu()