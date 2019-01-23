class Character():
    # Create a character
    def __init__(self, char_name, char_description):
        # the word "description" was abused as i mainly used it as a title
        # more than anything else
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self._introduced = False
        self._backpack = []
        self._defeated = {
            "Darius": False,
            "Fiora": False
        }

    @property
    def backpack(self):
        return self._backpack

    @property
    def defeated(self):
        return self._defeated

    def has_no_items(self):
        """Check if the player has no items in their backpack"""
        return len(self._backpack) == 0

    def get_backpack(self):
        """Returns the player's backpack"""
        return self._backpack

    def in_backpack(self, item):
        """Check if the given item is in the player's backpack"""
        return item in [i.name.lower() for i in self._backpack]  # i = item

    def give_item(self, item):
        """Place the given item into the player's backpack"""
        self._backpack.append(item)

    def defeat(self, enemy):
        """Sets the given enemy as defeated only if they have not been"""
        if self._defeated.get(enemy.name) is False:
            self._defeated[enemy.name] = True

    def has_won(self):
        """Checks if all enemies have been defeated and returns True, returns
        False otherwise"""
        return all(self._defeated.values())

    def introduce(self):
        """Describes the player if they have not been introduced yet

        Used to introduce the character to the player when the game has been
        booted up for the first time"""
        if self._introduced is False:
            self._introduced = True
            self.describe()

    # Describe this character
    def describe(self):
        print(f"{self.description}, {self.name} is here!\n")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation + "\n")
        else:
            print(self.name + " doesn't want to talk to you\n")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Friend(Character):
    """A more limited Character class built to assist the player
    on their conquest"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self._gift = None

    @property
    def gift(self):
        return self._gift

    def get_gift(self):
        """Returns the friend's gift"""
        return self._gift

    def give_gift(self, item):
        """Set the item given as the friend's gift"""
        self._gift = item

    # overwritten function inherited from Character - polymorphism
    def give_item(self, item):
        self.give_gift(item)

    def remove_gift(self):
        """Removes the friend's gift - called when given to the player to
        avoid item duplication"""
        self._gift = None


class Enemy(Character):
    """Combat-built character designed to crush the player without a
    specified weakness"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self._weakness = None

    @property
    def weakness(self):
        return self._weakness

    def set_weakness(self, weakness):
        """Set the enemy's weakness"""
        self._weakness = weakness

    def fight(self, weapon):
        """Fights the enemy with the given weapon

        The player wins if the weapon is the enemy's weakess, otherwise
        the player loses"""
        if weapon == self.weakness.name.lower():
            print(f"You fend {self.name} off with {weapon.title()}!\n")

            return True
        else:
            print(f"{self.name} crushed you. Maybe try finding it's weakness?")

            return False
