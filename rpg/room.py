class Direction:
    """Enum for the directions of the room - used for readability and
    personal preference"""
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"
    all = [NORTH, EAST, SOUTH, WEST]


class Room():
    def __init__(self, room_name):
        self._name = room_name
        self._description = None
        self._friend = None
        self._enemy = None
        self._item = None
        self.linked_rooms = {}

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def friend(self):
        return self._friend

    @property
    def enemy(self):
        return self._enemy

    @property
    def item(self):
        return self._item

    def get_name(self):
        """Get the room's name"""
        return self.name

    def get_description(self):
        """Get the room's description"""
        return self._description

    def set_description(self, room_description):
        """Set the given description as the room's"""
        self._description = room_description

    def get_friend(self):
        """Get the friend assigned to the room"""
        return self._friend

    def set_friend(self, friend):
        """Sets the given friend as the room"""
        self._friend = friend

    def get_enemy(self):
        """Returns the room's enemy"""
        return self._enemy

    def set_enemy(self, enemy):
        """Sets the given enemy as the room's"""
        self._enemy = enemy

    def get_item(self):
        """Returns the room's item"""
        return self._item

    def set_item(self, item):
        """Sets the given item as the room's"""
        self._item = item

    def describe(self):
        print(self.description)

    def link_room(self, room, direction):
        """Links the given room to this room in the given direction

        Example: the current room is the kitchen and another room exists called
        the hallway, you can set the hallway to be north of the kitchen by
        doing:

        kitchen.link_room(hallway, "north")
        kitchen.link_room(hallway, Direction.NORTH)  # using the preset enum"""
        self.linked_rooms[direction] = room

    def get_details(self):
        """Explains the content of the room, such as: friends, enemies or other
        linked rooms"""
        friend_found = self.get_friend()
        enemy_found = self.get_enemy()

        print(f"You are in the {self.get_name()}\n"
              f"{self.get_description()}\n")

        if friend_found is not None:
            friend_found.describe()
        elif enemy_found is not None:
            enemy_found.describe()

        # can get (direction, room) pairs using "dict.items()" method
        for direction in self.linked_rooms:
            room = self.linked_rooms.get(direction)
            direction = direction.title()

            print(f"{direction} is the {room.get_name()}")

    def move(self, direction):
        """Gets the room that is in the direction of the current room and
        returns it"""
        room_found = self.linked_rooms.get(direction)
        direction = direction.title()
        name = self.get_name()

        if room_found is None:
            print(f"There is nothing {direction} of the {name}")

        return room_found
