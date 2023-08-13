class Animal:
    def __init__(self, name: str, color: str, size: float) -> None:
        self.name = name
        self.color = color
        self.size = size

    def show_unique(self):
        pass
    
    def get_info(self):
        return self.name, self.color, self.size
