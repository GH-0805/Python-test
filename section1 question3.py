class father():
    def property(self):
        print("father property")
    def buisness(self):
        print("father buisness")
class son(father):
    def study(self):
        print("son study")
class daughter(father):
    def dance(self):
        print("daughter dance")
class grandson(son,daughter):
    def gaming(self):
        print("grandson gaming")
g=grandson()
g.property()    
g.buisness()
g.study()   
g.dance()
g.gaming()