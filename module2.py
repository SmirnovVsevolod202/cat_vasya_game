from abc import ABC, abstractmethod


class Unit(ABC):
    """
    Абстрактный базовый класс для всех игровых юнитов.
    """
    
    def __init__(self, strength, dexterity, constitution,
                 wisdom, intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass


class Character(Unit):
    """
    Класс персонажа с поддержкой игровых классов:
    warrior, mage, hunter.
    """
    
    VALID_CLASSES = ['warrior', 'mage', 'hunter']
    
    def __init__(self, strength, dexterity, constitution,
                 wisdom, intelligence, charisma, character_class):
        """
        Инициализация персонажа.
        
        character_class (str): Класс персонажа 
                                ('warrior', 'mage', 'hunter')
        """
        if character_class not in self.VALID_CLASSES:
            raise ValueError(
                f"Недопустимый класс: {character_class}. "
                f"Допустимые значения: {self.VALID_CLASSES}"
            )
        
        super().__init__(strength, dexterity, constitution,
                        wisdom, intelligence, charisma)
        self.character_class = character_class
        
        # Вычисляем и сохраняем характеристики
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        """
        Единая формула для всех классов:
        телосложение * 10 + сила // 2
        """
        return self.constitution * 10 + self.strength // 2

    def calculate_damage(self):
        """
        Формула урона зависит от класса персонажа:
        - warrior: сила * 2.2 + телосложение // 3
        - mage: интеллект * 2.5 + мудрость // 2
        - hunter: ловкость * 1.9 + сила // 3
        """
        if self.character_class == 'warrior':
            return int(self.strength * 2.2 + self.constitution // 3)
        elif self.character_class == 'mage':
            return int(self.intelligence * 2.5 + self.wisdom // 2)
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.9 + self.strength // 3)

    def calculate_defense(self):
        """
        Формула защиты зависит от класса персонажа:
        - warrior: телосложение * 1.8 + сила // 4
        - mage: мудрость * 1.3 + интеллект // 6
        - hunter: ловкость * 1.6 + телосложение // 5
        """
        if self.character_class == 'warrior':
            return int(self.constitution * 1.8 + self.strength // 4)
        elif self.character_class == 'mage':
            return int(self.wisdom * 1.3 + self.intelligence // 6)
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.6 + self.constitution // 5)


class Monster(Unit):
    """Класс монстра (без изменений из модуля 1)."""
    
    def __init__(self, strength, dexterity, constitution,
                 wisdom, intelligence, charisma):
        super().__init__(strength, dexterity, constitution,
                        wisdom, intelligence, charisma)
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        return self.constitution * 8 + self.strength // 3

    def calculate_damage(self):
        return int(self.strength * 2 + self.constitution // 5)

    def calculate_defense(self):
        return int(self.constitution * 1.2 + self.strength // 5)