# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Conection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password= None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def creat_whit_auth(cls, user, password):
        Conection = cls
        Conection.user = user
        Conection.password = password
        return Conection

#c1 = Conection()
c1 = Conection.creat_whit_auth('maria', 1234)
#c1.set_user('maria')
#c1.set_password(123)
print(c1.user)
print(c1.password)