"""
能力卡牌
"""
from .card_base import Card, CardType


class Burning(Card):
    """燃烧 - 持续火伤"""
    
    def __init__(self, upgraded=False):
        damage = 5 if upgraded else 3
        super().__init__(
            name="燃烧",
            card_type=CardType.ABILITY,
            cost=1,
            description=f"每回合造成{damage}点火伤",
            upgraded=upgraded
        )
        self.damage = damage
    
    def play(self, player, enemy):
        """给敌人施加燃烧效果"""
        enemy.add_status("burning", self.damage)
        return f"使用了{self.name}，敌人每回合受到{self.damage}点火伤"
    
    def _apply_upgrade(self):
        """升级效果"""
        self.damage = 5
        self.description = f"每回合造成{damage}点火伤"


class DemonForm(Card):
    """恶魔形态 - 力量提升"""
    
    def __init__(self, upgraded=False):
        strength = 2 if upgraded else 1
        super().__init__(
            name="恶魔形态",
            card_type=CardType.ABILITY,
            cost=3,
            description=f"每回合获得{strength}点力量",
            upgraded=upgraded
        )
        self.strength = strength
    
    def play(self, player, enemy):
        """获得力量提升"""
        player.add_status("demon_form", self.strength)
        return f"使用了{self.name}，每回合获得{self.strength}点力量"
    
    def _apply_upgrade(self):
        """升级效果"""
        self.strength = 2
        self.description = f"每回合获得{self.strength}点力量"
