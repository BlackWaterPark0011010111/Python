


class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def describe_user(self):
        print(f'Sooo... this is {self.first_name} {self.last_name}, hes a new one here. please welcome {self.first_name}')

    def greet_user(self):
        print(f'Hello {self.first_name}')

user=User('Jack','Smith')
user.describe_user()
user.greet_user()

class User():
    #метод
    def __init__(self,first_name,last_name):
        self.first_name=first_name#атрибут экземпляра
        self.last_name=last_name#атрибут экземпляра
class Admin(User):
    def __init__(self,first_name,last_name,):
        super().__init__(first_name,last_name)
        self.first_name=first_name
        self.last_name=last_name
        self.priviliges=['allowed to add','allowed to delete','allowed to banned']
    def show_priviliges(self):
        print(f'{self.first_name}, {self.last_name} so, heres your lettings {self.priviliges}')
admee=Admin('Rick','Fellns')
admee.show_priviliges()

class Privileges:
    def __init__(self):
        #атрибут экземпляра
        self.privileges=['allowed to add', 'allowed to delete', 'allowed to ban']
#метод
    def show_privileges(self):
        print(f'heres ure priv {self.privileges}')

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=Privileges()#экземпляр Privileges как атрибут класса Admin.

admin_user=Admin('Rick','Fellins')
admin_user.privileges.show_privileges()