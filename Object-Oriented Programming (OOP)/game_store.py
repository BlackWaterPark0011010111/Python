# Класс игры
class Game:
    def __init__(self, name, price):  # задаём название и цену
        self.name = name  
        self.price = price 
        self.is_bought = False  # куплена ли игра, по умолчанию False

    def buy(self):  # метод для покупки 
        if not self.is_bought:  # если игра ещё не куплена
            self.is_bought = True  # меняем статус на "куплено"
            print(f"Игра '{self.name}' куплена за {self.price} рублей!")
        else:
            print(f"Игра '{self.name}' уже куплена!")  # если уже куплена

    def __str__(self):  # для вывода информации об игре
        return f"Игра: {self.name}, Цена: {self.price} руб., Куплена: {'Да' if self.is_bought else 'Нет'}"
