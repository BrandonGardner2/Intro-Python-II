class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __string__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def on_take(self):
        return f"You have picked up {self.name}."

    def on_drop(self):
        return f"You have dropped {self.name}"
