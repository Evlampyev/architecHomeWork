# Принцип сегрегации интерфейса (Interface Segregation Principle, ISP).
# Он гласит: "Клиенты не должны зависеть от интерфейсов, которые они не используют".

from robotWorker import RobotWorker
from humanWorker import HumanWorker

worker1 = RobotWorker()
worker2 = HumanWorker()
worker1.work()
worker2.eat()
worker2.work()
