class Customer:
    def __init__(self, name):
        self.name = None
        self.set_name(name)
        self._orders = []

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    name = property(get_name, set_name)
