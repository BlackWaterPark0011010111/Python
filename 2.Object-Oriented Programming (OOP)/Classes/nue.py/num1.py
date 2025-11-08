import copy



#class Giraffes(Mammals):
#    #def__init__-- это функция инициализации
#    def __init__(self, spots):#self, spots -здесь это аргументы,значения self и spots
#        #здесь строка присваивает значение аргумента spots свойству объекта,свойство-это принадлежащая объекту переменная
#        #эта строка означает «Взять значение аргумента spots и поместить его в переменную объекта (свойство объекта) с именем giraffe_spots»
#        self.giraffe_spots = spots
#    def this_is_a_normal_function():
#        print('Я — обычная функция')
#    def eat_leaves_from_trees(self):
#        print('ест листья')

#сущность,объект класса ,экземпляр класса Giraffes
#reginald=Giraffes()
#reginald.move()
#reginald.eat_leaves_from_trees()
#harold=Giraffes()
#harold.move()
class Things:
    def __init__(self,species,number_of_legs,color):
        self.species=species
        self.number_of_legs=number_of_legs
        self.color=color
harry=Things('гиппогриф',6,'черный')
harriet=copy.copy(harry)
print(harriet.species)


carrie = Things('химера', 4, 'зеленый горошек')
billy = Things('богл', 0, 'узорчатый')

my_animals = [harry, carrie, billy]

more_animals = copy.copy(my_animals)
print(more_animals[0].color)
print(more_animals[1].species)


class Book:
    def __init__(self,title,tags,author):
        self.title=title
        self.tags=tags
        self.author=author
    def main(self):
        print(f'So here is {self.title}')

books=Book('Mirac','dark','King')
print(f'its a {books.author}')
more_books=Book('Joood','horror','koons')
ko=copy.deepcopy(more_books)
print(ko.author)
print(ko.author[1])
print(books.title,books.tags,books.author)

print(books.__init__)
print(books.__dict__)

animals=[['cat','dog'],['eagle', 'rawk']]
deep=copy.deepcopy(animals)
deep[0][0]='lion'

print('original: ',animals)
print('deep copy: ', deep)
'''Мы изменили элемент внутри
 копии — и он изменился и в оригинале.
Потому что copy() не копировал 
вложенный список, а просто сослался на него'''
'''| Тип копии         | Что копирует           | Вложенные объекты       | Изменения в копии влияют на оригинал |
| ----------------- | ---------------------- | ----------------------- | ------------------------------------ |
| `copy.copy()`     | Только верхний уровень | ❌ Нет (ссылки остаются) | ✅ Да                                 |
| `copy.deepcopy()` | Всё дерево объектов    | ✅ Да                    | ❌ Нет                                |
'''
class Pet:
    def __init__(self,name):
        self.name=name

class Wizard:
    def __init__(self,name,spellbook,pet):
        self.name=name
        self.spellbook=spellbook
        self.pet=pet

pet=Pet('Fenix')
wizard=Wizard('Gendalf', ['Light','bore'], pet)

wizard_copy=copy.copy(wizard)
wizard_deep=copy.deepcopy(wizard)
wizard.pet.name='Forest'

print("Поверхностная копия:")
print("Оригинал:", wizard.pet.name)
print("Копия:", wizard_copy.pet.name)   #изменится, потому что ссылка общая

print("\nГлубокая копия:")
print("Оригинал:", wizard.pet.name)
print("Глубокая копия:", wizard_deep.pet.name)  #останется "Феникс"
pet1 = Pet("Феникс")
pet2 = Pet("Ворон")
wizard[0].name='vampire'
print(wizard[0].name)
wizard=[
    Wizard('Gendalf',['Light','bore'], pet1),
    Wizard('Marlin',['illusion'],pet2)
]
wizard_copy=copy.copy(wizard)
wizard[0].name='Vampire'
print('original: ', wizard[0].name)
print('Copy: ', wizard_copy[0].name)
