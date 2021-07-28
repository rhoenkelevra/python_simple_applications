class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name


customers = [
    Customer("Rhoen", "Gold"),
    Customer("Caleb", "Silver")
]

print(customers[0].name)
