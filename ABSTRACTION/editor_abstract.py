

from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):pass

    @abstractmethod
    def debug(self):pass

    @abstractmethod
    def execute(self):pass

class Vscode(Editor):

    def open(self):
        print("Vscode open method")

    def debug(self):

        print("Vscode debug method")

    def execute(self):
        
        print("vscode execute method")

vsc_instance = Vscode()

vsc_instance.open()

vsc_instance.debug()

vsc_instance.execute()