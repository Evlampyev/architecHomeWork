Принцип открытости/закрытости

__Исходные данные__

    class Greeting:
        def __init__(self, type):
            self.type = type

        def greet(self):
            if self.type == "formal":
                print("Добро пожаловать, уважаемый гость!")
            elif self.type == "informal":
                print("Привет, друг!")


    if __name__ == "__main__":
        greeting = Greeting("informal")
        greeting.greet()
