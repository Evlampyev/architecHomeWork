from iWorker import IHumanWorker


class HumanWorker(IHumanWorker):
    def work(self):
        print("Человек работает")

    def eat(self):
        print("Человек ест")
