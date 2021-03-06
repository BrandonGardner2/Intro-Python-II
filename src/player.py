# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory

    def __str__(self):
        return f"Location: {getattr(self, 'location')}\n----------"

    def get_inventory(self):
        results = [i.name for i in self.inventory]
        return ', '.join(results)
