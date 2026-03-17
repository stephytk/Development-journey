"""
"""


from abc import ABC,abstractmethod


class Bike(ABC):

    @abstractmethod
    def transmission(self):pass
    
    @abstractmethod
    def start(self):pass


class Pulsar(Bike):

    def transmission(self):
        print("transmission method")

    def start(self):
        print("start method")

pul_instance = Pulsar()

pul_instance.transmission()
pul_instance.start()


