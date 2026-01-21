"""
角色基类
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cards import Card


class Character:
    """角色基类"""
    
    def __init__(self, name, max_hp, max_energy):
        """
        初始化角色
        
        Args:
            name: 角色名称
            max_hp: 最大生命值
            max_energy: 最大能量
        """
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_energy = max_energy
        self.energy = max_energy
        self.armor = 0
        self.deck = []  # 牌库
        self.hand = []  # 手牌
        self.discard_pile = []  # 弃牌堆
        self.draw_pile = []  # 抽牌堆
        self.status_effects = {}  # 状态效果
        self.relics = []  # 遗物
        self.potions = []  # 药水
    
    def take_damage(self, damage):
        """
        受到伤害
        
        Args:
            damage: 伤害值
        """
        # 先扣除护甲
        if self.armor > 0:
            if self.armor >= damage:
                self.armor -= damage
                damage = 0
            else:
                damage -= self.armor
                self.armor = 0
        
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return damage
    
    def heal(self, amount):
        """
        治疗
        
        Args:
            amount: 治疗量
        """
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def add_armor(self, amount):
        """
        添加护甲
        
        Args:
            amount: 护甲值
        """
        self.armor += amount
    
    def clear_armor(self):
        """清除护甲"""
        self.armor = 0
    
    def add_status(self, status_name, value):
        """
        添加状态效果
        
        Args:
            status_name: 状态名称
            value: 状态值
        """
        if status_name in self.status_effects:
            self.status_effects[status_name] += value
        else:
            self.status_effects[status_name] = value
    
    def remove_status(self, status_name):
        """移除状态效果"""
        if status_name in self.status_effects:
            del self.status_effects[status_name]
    
    def has_status(self, status_name):
        """检查是否有状态效果"""
        return status_name in self.status_effects
    
    def get_status(self, status_name):
        """获取状态效果值"""
        return self.status_effects.get(status_name, 0)
    
    def add_card_to_deck(self, card):
        """
        添加卡牌到牌库
        
        Args:
            card: 卡牌对象
        """
        self.deck.append(card.clone())
    
    def start_turn(self):
        """回合开始"""
        self.energy = self.max_energy
        self.clear_armor()
        
        # 处理状态效果
        if self.has_status("demon_form"):
            strength = self.get_status("demon_form")
            self.add_status("strength", strength)
    
    def end_turn(self):
        """回合结束"""
        # 清除未使用的护甲
        self.clear_armor()
    
    def is_alive(self):
        """检查是否存活"""
        return self.hp > 0
    
    def draw_cards(self, num):
        """
        抽牌
        
        Args:
            num: 抽牌数量
        """
        for _ in range(num):
            if len(self.draw_pile) == 0:
                # 抽牌堆为空，洗牌
                self.draw_pile = self.discard_pile[:]
                self.discard_pile = []
                import random
                random.shuffle(self.draw_pile)
                
                if len(self.draw_pile) == 0:
                    return  # 没有牌可抽
            
            card = self.draw_pile.pop()
            self.hand.append(card)
    
    def play_card(self, card_index, enemy):
        """
        使用卡牌
        
        Args:
            card_index: 卡牌在手牌中的索引
            enemy: 敌人对象
        """
        if card_index < 0 or card_index >= len(self.hand):
            return None
        
        card = self.hand[card_index]
        
        # 检查能量是否足够
        if card.cost > self.energy:
            return None
        
        # 使用卡牌
        self.energy -= card.cost
        result = card.play(self, enemy)
        
        # 将卡牌移到弃牌堆
        self.hand.pop(card_index)
        self.discard_pile.append(card)
        
        return result
    
    def discard_all(self):
        """弃掉所有手牌"""
        self.discard_pile.extend(self.hand)
        self.hand = []
    
    def reset_deck(self):
        """重置牌库"""
        self.draw_pile = self.deck[:]
        self.discard_pile = []
        self.hand = []
        import random
        random.shuffle(self.draw_pile)
