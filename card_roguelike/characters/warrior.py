"""
战士职业
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from characters.character import Character
from cards import Strike, Defend, HeavyAttack, IronWave


class Warrior(Character):
    """战士职业 - 高生命值，擅长攻击和护甲"""
    
    def __init__(self):
        super().__init__(
            name="战士",
            max_hp=80,
            max_energy=3
        )
        
        # 初始化初始卡组
        self._init_deck()
    
    def _init_deck(self):
        """初始化战士的初始卡组"""
        # 5张打击
        for _ in range(5):
            self.add_card_to_deck(Strike())
        
        # 4张防御
        for _ in range(4):
            self.add_card_to_deck(Defend())
        
        # 1张重击
        self.add_card_to_deck(HeavyAttack())
        
        # 1张铁波
        self.add_card_to_deck(IronWave())
