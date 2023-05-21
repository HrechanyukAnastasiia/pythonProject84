class FoodItem:
    def __init__(self, назва, опис, ціна):
        self.назва = назва
        self.опис = опис
        self.ціна = ціна

class Menu:
    def __init__(self):
        self.страви = []

    def додати_страву(self, страва):
        self.страви.append(страва)

    def видалити_страву(self, страва):
        self.страви.remove(страва)

    def вивести_меню(self):
        print("Меню:")
        for страва in self.страви:
            print(f"{страва.назва} - {страва.опис}, {страва.ціна} грн")

class Order:
    def __init__(self):
        self.страви = []

    def додати_страву(self, страва):
        self.страви.append(страва)

    def розрахувати_суму(self):
        загальна_сума = 0
        for страва in self.страви:
            загальна_сума += страва.ціна
        return загальна_сума

class Restaurant:
    def __init__(self):
        self.меню = Menu()

    def додати_страву_в_меню(self, страва):
        self.меню.додати_страву(страва)

    def видалити_страву_з_меню(self, страва):
        self.меню.видалити_страву(страва)

    def вивести_меню(self):
        self.меню.вивести_меню()

    def зробити_замовлення(self, замовлення):
        загальна_сума = замовлення.розрахувати_суму()
        print("Замовлення прийнято!")
        print("Страви:")
        for страва in замовлення.страви:
            print(f"{страва.назва} - {страва.ціна} грн")
        print(f"Загальна сума: {загальна_сума} грн")

        # Збереження замовлення у файл
        with open("orders.txt", "a") as файл:
            файл.write("Замовлення:\n")
            for страва in замовлення.страви:
                файл.write(f"{страва.назва} - {страва.ціна} грн\n")
            файл.write(f"Загальна сума: {загальна_сума} грн\n")
            файл.write
vareniki = FoodItem("Вареники", "Вареники з сиром", 100)
tea = FoodItem("Чай", "Чай з молоком", 50)
cheesecake = FoodItem("Чизкейк", "Шоколадний чизкейк", 80)


меню = Menu()
меню.додати_страву(vareniki)
меню.додати_страву(tea)
меню.додати_страву(cheesecake)


ресторан = Restaurant()
ресторан.додати_страву_в_меню(vareniki)
ресторан.додати_страву_в_меню(tea)
ресторан.додати_страву_в_меню(cheesecake)


ресторан.вивести_меню()


замовлення = Order()
замовлення.додати_страву(vareniki)
замовлення.додати_страву(tea)
замовлення.додати_страву(cheesecake)

ресторан.зробити_замовлення(замовлення)
