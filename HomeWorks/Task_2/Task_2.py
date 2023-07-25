# Команда (Транзакция, Action)
# Это поведенческий паттерн проектирования, который позволяет разделить например интерфейс и бизнес-логику,
# используя класс, который делегирует бизнес-логике действие, запрашиваемое отправителем команды.
# Паттерн Команда по сути устанавливает одностороннюю связь от заказчика к исполнителю.
# Паттерн Команда (как впрочем и другие паттерны проектирования отношений между отправителем и получателем запросов)
# ведет к появлению дополнительных классов и усложнению кода.

class Light:
    def turn_on(self):
        print('Включить свет')

    def turn_off(self):
        print('Выключить свет')


class CommandBase:
    def execute(self):  # НЕ ПОНЯТНО ЧТО ДЕЛАЕТ??????
        raise NotImplementedError() # Исключение, возникающее в случаях, когда наследник класса не переопределил метод,
                                     # который должен был (я так понимаю что у наследников метод должен быть определён).


class LightCommandBase(CommandBase):
    def __init__(self, light):
        self.light = light


class TurnOnLightCommand(LightCommandBase):

    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_off()


class Switch:
    """Выключатель
    ...
    Методы
    ------
    on()
        переводит выключатель в положение включено
    off()
        переводит выключатель в положение включено
    """

    def __init__(self, on_cmd, off_cmd):
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd

    def on(self):
        """Включает выключатель"""
        self.on_cmd.execute()

    def off(self):
        self.off_cmd.execute()


light = Light()
switch = Switch(on_cmd=TurnOnLightCommand(light),
                off_cmd=TurnOffLightCommand(light))
switch.on()  # Включить свет
switch.off()  # Выключить свет
