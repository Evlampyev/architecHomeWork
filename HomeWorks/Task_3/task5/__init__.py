# Принцип инверсии зависимостей (Dependency Inversion Principle, DIP)
# гласит: "Зависимости на абстракциях. Нет зависимостей на что-то конкретное".
# Это означает, что высокоуровневые модули, которые обеспечивают сложную логику,
# должны быть независимы от низкоуровневых модулей, которые обеспечивают
# утилитарные функции. Оба типа модулей должны зависеть от абстракций.

from text import Text
from printer import Printer

myText = Text("Привет, мир!")
myPrinter = Printer()
myPrinter.printT(myText.__getinitargs__())