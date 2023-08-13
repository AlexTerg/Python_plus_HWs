from task5Animal import Animal

class Fish(Animal):
    def __init__(self, name: str, color: str, size: float, max_depth: float) -> None:
        super().__init__(name, color, size)
        self.max_depth = max_depth
        
    def show_unique(self):
        print(self.max_depth)
        
class Bird(Animal):
    def __init__(self, name: str, color: str, size: float, habitate) -> None:
        super().__init__(name, color, size)
        self.habitate = habitate
        
        
    def show_unique(self):
        print(self.habitate)
        
class Cat(Animal):
    def __init__(self, name: str, color: str, size: float, hairy) -> None:
        super().__init__(name, color, size)
        self.hairy = hairy
        
    def show_unique(self):
        print(self.hairy)
        
        
class Fabric:
    
    def create_animal(self, type_animal: str, *args):
        if type_animal.lower() == 'fish':
            return Fish(*args)
        elif type_animal.lower() == 'bird':
            return Bird(*args)
        elif type_animal.lower() == 'cat':
            return Cat(*args)
        else:
            raise TypeError('Данный тип животного отсутствует')
    
        
    
        

fabric = Fabric()
cat = fabric.create_animal('cat', 'Leo', 'green', 43.3, 'Yes')
cat.show_unique()
print(cat.get_info())