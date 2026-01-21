"""
技能卡牌
"""
from .card_base import Card, CardType


class Defend(Card):
    """防御 - 基础防御卡"""
    
    def __init__(self, upgraded=False):
        armor = 8 if upgraded else 5
        super().__init__(
            name="防御",
            card_type=CardType.SKILL,
            cost=1,
            description=f"获得{armor}点护甲",
            upgraded=upgraded
        )
        self.armor = armor
    
    def play(self, player, enemy):
        """获得护甲"""
        player.add_armor(self.armor)
        return f"使用了{self.name}，获得{self.armor}点护甲"
    
    def _apply_upgrade(self):
        """升级效果"""
        self.armor = 8
        self.description = f"获得{self.armor}点护甲"


class IronWave(Card):
    """铁波 - 攻击+防御"""
    
    def __init__(self, upgraded=False):
        damage = 8 if upgraded else 5
        armor = armor = 8 if upgraded else 5
        super().__init__(
            name="铁波",
            card_type=CardType.SKILL,
            cost=1,
            description=f"造成{damage}点伤害，获得{armor}点护甲",
            upgraded=upgraded
        )
        self.damage = damage
        self.armor = armor
    
    def play(self, player, enemy):
        """造成伤害并获得护甲"""
        enemy.take_damage(self.damage)
        player.add_armor(self.armor)
        return f"使用了{self.name}，造成{self.damage}点伤害，获得{self.armor}点护甲"
    
    def _apply_upgrade(self):
        """升级效果"""
        self.damage = 8
        self.armor = 8
        self.description = f"造成{self.damage}点伤害，获得{self.armor}点护甲"
