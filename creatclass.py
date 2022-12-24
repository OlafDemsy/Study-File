class Person:
    def __init__(self, name) :
        self.name = name
    def talk(self):
        print(f'Hi,I am {self.name}')
Olaf = Person("Olaf Demsy")
Olaf.talk()
