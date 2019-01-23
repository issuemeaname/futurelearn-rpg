class Item:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def get_name(self):
        """Returns the item's name"""
        return self._name

    def get_description(self):
        """Returns the item's description"""
        return self._description

    def set_name(self, name):
        """Renames the item"""
        self._name = name

    def set_description(self, description):
        """Sets the given description as the item's"""
        self._description = description
