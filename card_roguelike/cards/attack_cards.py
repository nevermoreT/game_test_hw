"""
攻击卡牌
"""
from .card_base import Card, CardType


class Strike(Card):
    """打击 - 基础攻击卡"""
    
    def __init__(self, upgraded=False):
        damage = 9 if upgraded else 6
        super().__init__(
            name="打击",
            card_type=CardType.ATTACK,
            cost=1,
            description=f"造成{damage}点伤害",
            upgraded=upgraded
        )
        self.damage = damage
    
    def play(self, player, enemy):
        """造成伤害"""
        enemy.take_damage(self.damage)
        return f"使用了{self.name}，对敌人造成{self.damage}点伤害"
    
    def _apply_upgrade(self):
        """升级效果"""
        self.damage = 9
        self.description = f"造成{self.damage}点伤害"


class HeavyAttack(Card):
    """重击 - 高伤害攻击"""
    
    def __init__(self, upgraded=False):
        damage = 20 if upgraded else 15
        super().__init__(
            name="重击",
            card_type=CardType.ATTACK,
            cost=2,
            description=f"造成{damage}点伤害",
            upgraded=upgraded
        )
        self.damage = damage
    
    def play(self, player, enemy):
        """造成大量伤害"""
        enemy.take_damage(self.damage)
        return f"使用了{self.name}，对敌人造成{self.damage}点伤害"
    
    def _apply_upgrade(self):
        """升级效果"""
        self.damage = 20
        self.description = f"造成{self.damage}点伤害"


class Whirlwind(Card):
    """旋风斩 - 全体攻击"""
    
    def __init__(self, upgraded=False):
        damage = 7 if upgraded else 5
        super().__init__(
            name="旋风斩",
            card_type=CardType.ATTACK,
            cost=2,
            description=f"对所有敌人造成{damage}点伤害",
            upgraded=upgraded
        )
        self.damage = damage
    
    def play(self, player, enemy):
        """对所有敌人造成伤害"""
        # 简化版：只对当前敌人造成伤害
        enemy.take_damage(self.damage)
        return f"使用了{self.name}，对敌人造成{self.damage}点伤害"
    
    def _apply_upgrade(self):
        """升级效果"""
        self.damage = 7
        self.description = f"对所有敌人造成{self.damage}点伤害"
