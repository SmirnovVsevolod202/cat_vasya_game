from abc import ABC, abstractmethod


class Unit(ABC):
    """
    Абстрактный базовый класс с поддержкой заклинаний и маны.
    """
    
    def __init__(self, strength, dexterity, constitution,
                 wisdom, intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        
        # Новые атрибуты для системы магии
        self.spells = []  # Список заклинаний
        self.mana = 0     # Текущая мана

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass

    def add_spell(self, spell):
        """
        Добавляет заклинание в список доступных.
        
        Args:
            spell (Spell): Объект заклинания
        """
        self.spells.append(spell)

    def cast_spell(self, index):
        """
        Применяет заклинание по индексу.
        
        Args:
            index (int): Индекс заклинания в списке spells
            
        Returns:
            int: Урон от заклинания
            
        Raises:
            ValueError: Если недостаточно маны или индекс неверен
        """
        if index < 0 or index >= len(self.spells):
            raise ValueError(f"Неверный индекс заклинания: {index}")
        
        spell = self.spells[index]
        
        if self.mana < spell.mana_cost:
            raise ValueError(
                f"Недостаточно маны. Нужно: {spell.mana_cost}, "
                f"есть: {self.mana}"
            )
        
        # Вычитаем ману и применяем заклинание
        self.mana -= spell.mana_cost
        return spell.cast()


class Spell(ABC):
    """
    Абстрактный класс заклинания.
    """
    
    def __init__(self, name, damage, mana_cost):
        """
        Инициализация заклинания.
        
        Args:
            name (str): Название заклинания
            damage (int): Базовый урон
            mana_cost (int): Стоимость в мане
        """
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        """
        Применяет заклинание.
        
        Returns:
            int: Итоговый урон
        """
        pass


class Fireball(Spell):
    """Заклинание 'Огненный шар'."""
    
    def __init__(self):
        super().__init__(name="Fireball", damage=35, mana_cost=15)

    def cast(self):
        return self.damage


class IceLance(Spell):
    """Заклинание 'Ледяное копьё'."""
    
    def __init__(self):
        super().__init__(name="IceLance", damage=25, mana_cost=10)

    def cast(self):
        return self.damage


class LightningBolt(Spell):
    """Заклинание 'Удар молнии'."""
    
    def __init__(self):
        super().__init__(name="LightningBolt", damage=40, mana_cost=20)

    def cast(self):
        return self.damage


class Character(Unit):
    """
    Класс персонажа с поддержкой маны и заклинаний.
    """
    
    VALID_CLASSES = ['warrior', 'mage', 'hunter']
    
    def __init__(self, strength, dexterity, constitution,
                 wisdom, intelligence, charisma, character_class):
        if character_class not in self.VALID_CLASSES:
            raise ValueError(
                f"Недопустимый класс: {character_class}. "
                f"Допустимые значения: {self.VALID_CLASSES}"
            )
        
        super().__init__(strength, dexterity, constitution,
                        wisdom, intelligence, charisma)
        self.character_class = character_class
        
        # Вычисляем характеристики
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()
        
        # Вычисляем и устанавливаем ману
        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana  # Начинаем с полной маной

    def calculate_max_health(self):
        """Телосложение * 10 + сила // 2"""
        return self.constitution * 10 + self.strength // 2

    def calculate_damage(self):
        """Урон зависит от класса персонажа."""
        if self.character_class == 'warrior':
            return int(self.strength * 2.2 + self.constitution // 3)
        elif self.character_class == 'mage':
            return int(self.intelligence * 2.5 + self.wisdom // 2)
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.9 + self.strength // 3)

    def calculate_defense(self):
        """Защита зависит от класса персонажа."""
        if self.character_class == 'warrior':
            return int(self.constitution * 1.8 + self.strength // 4)
        elif self.character_class == 'mage':
            return int(self.wisdom * 1.3 + self.intelligence // 6)
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.6 + self.constitution // 5)

    def calculate_max_mana(self):
        """
        Формула максимальной маны зависит от класса:
        - warrior: интеллект + сила // 2
        - mage: интеллект * 3 + мудрость
        - hunter: ловкость * 1.5 + мудрость // 2
        """
        if self.character_class == 'warrior':
            return self.intelligence + self.strength // 2
        elif self.character_class == 'mage':
            return self.intelligence * 3 + self.wisdom
        elif self.character_class == 'hunter':
            return int(self.dexterity * 1.5 + self.wisdom // 2)


class Monster(Unit):
    """Класс монстра (без поддержки магии)."""
    
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

    # Монстры не используют ману, но метод нужен для совместимости
    def calculate_max_mana(self):
        return 0