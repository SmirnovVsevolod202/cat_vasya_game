from abc import ABC, abstractmethod


class Unit(ABC):
    """
    Абстрактный базовый класс для всех игровых юнито.
    Содержит шесть основных характеристик.
    """
    
    def __init__(self, strength, dexterity, constitution, 
                 wisdom, intelligence, charisma):
        """
        Инициализация характеристик юнита.
        
        strength (int): Сила
        dexterity (int): Ловкость
        constitution (int): Телосложение
        wisdom (int): Мудрость
        intelligence (int): Интеллект
        charisma (int): Харизма
        """
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self):
        """Вычисляет максимальное здоровье юнита."""
        pass

    @abstractmethod
    def calculate_damage(self):
        """Вычисляет базовый урон юнита."""
        pass

    @abstractmethod
    def calculate_defense(self):
        """Вычисляет показатель защиты юнита."""
        pass


class Character(Unit):
    """
    Класс персонажа игрока.
    Наследуется от Unit и реализует абстрактные методы.
    """
    
    def __init__(self, strength, dexterity, constitution,
                 wisdom, intelligence, charisma):
        """Инициализация персонажа с расчётом характеристик."""
        super().__init__(strength, dexterity, constitution,
                        wisdom, intelligence, charisma)
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        """
        Формула здоровья персонажа:
        телосложение * 10 + сила // 2
        """
        return self.constitution * 10 + self.strength // 2

    def calculate_damage(self):
        """
        Формула урона персонажа:
        сила * 1.5 + ловкость // 4
        """
        return int(self.strength * 1.5 + self.dexterity // 4)

    def calculate_defense(self):
        """
        Формула защиты персонажа:
        телосложение * 1.5 + ловкость // 3
        """
        return int(self.constitution * 1.5 + self.dexterity // 3)


class Monster(Unit):
    """
    Класс монстра.
    Наследуется от Unit и реализует абстрактные методы.
    """
    
    def __init__(self, strength, dexterity, constitution,
                 wisdom, intelligence, charisma):
        """Инициализация монстра с расчётом характеристик."""
        super().__init__(strength, dexterity, constitution,
                        wisdom, intelligence, charisma)
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        """
        Формула здоровья монстра:
        телосложение * 8 + сила // 3
        """
        return self.constitution * 8 + self.strength // 3

    def calculate_damage(self):
        """
        Формула урона монстра:
        сила * 2 + телосложение // 5
        """
        return int(self.strength * 2 + self.constitution // 5)

    def calculate_defense(self):
        """
        Формула защиты монстра:
        телосложение * 1.2 + сила // 5
        """
        return int(self.constitution * 1.2 + self.strength // 5)