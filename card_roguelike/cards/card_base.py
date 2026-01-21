"""
卡牌基类
"""
from enum import Enum


class CardType(Enum):
    """卡牌类型"""
    ATTACK = "攻击"
    SKILL = "技能"
    ABILITY = "能力"
    CURSE = "诅咒"


class Card:
    """卡牌基类"""
    
    def __init__(self, name, card_type, cost, description, upgraded=False):
        """
        初始化卡牌
        
        Args:
            name: 卡牌名称
            card_type: 卡牌类型
            cost: 能量消耗
            description: 卡牌描述
            upgraded: 是否升级
        """
        self.name = name
        self.card_type = card_type
        self.cost = cost
        self.description = description
        self.upgraded = upgraded
        self.base_cost = cost  # 记录基础消耗
    
    def play(self, player, enemy):
        """
        使用卡牌
        
        Args:
            player: 玩家对象
            enemy: 敌人对象
        """
        raise NotImplementedError("子类必须实现play方法")
    
    def upgrade(self):
        """升级卡牌"""
        self.upgraded = True
        self._apply_upgrade()
    
    def _apply_upgrade(self):
        """应用升级效果"""
        pass
    
    def clone(self):
        """克隆卡牌"""
        new_card = self.__class__(upgraded=self.upgraded)
        return new_card
    
    def __str__(self):
        upgraded_text = " (升级)" if self.upgraded else ""
        return f"{self.name}{upgraded_text} [{self.card_type.value}] {self.cost}能量"
