"""
敌人类
"""
from enum import Enum


class IntentType(Enum):
    """敌人意图类型"""
    ATTACK = "攻击"
    DEFEND = "防御"
    BUFF = "增益"
    DEBUFF = "减益"


class Enemy:
    """敌人类"""
    
    def __init__(self, name, max_hp):
        """
        初始化敌人
        
        Args:
            name: 敌人名称
            max_hp: 最大生命值
        """
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.armor = 0
        self.status_effects = {}
        self.intent = None
        self.intent_value = 0
        self.action_index = 0
        self.actions = []  # 行动模式列表
    
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
    
    def add_armor(self, amount):
        """添加护甲"""
        self.armor += amount
    
    def clear_armor(self):
        """清除护甲"""
        self.armor = 0
    
    def add_status(self, status_name, value):
        """添加状态效果"""
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
    
    def set_intent(self, intent_type, value):
        """
        设置敌人意图
        
        Args:
            intent_type: 意图类型
            value: 意图值
        """
        self.intent = intent_type
        self.intent_value = value
    
    def execute_action(self, player):
        """
        执行行动
        
        Args:
            player: 玩家对象
        """
        if self.intent == IntentType.ATTACK:
            damage = self.intent_value
            # 考虑力量加成
            if self.has_status("strength"):
                damage += self.get_status("strength")
            player.take_damage(damage)
            return f"{self.name}攻击了，造成{damage}点伤害"
        elif self.intent == IntentType.DEFEND:
            self.add_armor(self.intent_value)
            return f"{self.name}获得了{self.intent_value}点护甲"
        elif self.intent == IntentType.BUFF:
            self.add_status("strength", self.intent_value)
            return f"{self.name}获得了{self.intent_value}点力量"
        elif self.intent == IntentType.DEBUFF:
            player.add_status("poison", self.intent_value)
            return f"{self.name}给你施加了{self.intent_value}层毒"
        
        return f"{self.name}什么也没做"
    
    def plan_next_action(self):
        """计划下一个行动"""
        if not self.actions:
            return
        
        action = self.actions[self.action_index % len(self.actions)]
        self.set_intent(action["type"], action["value"])
        self.action_index += 1
    
    def end_turn(self):
        """回合结束"""
        self.clear_armor()
        
        # 处理状态效果
        if self.has_status("burning"):
            damage = self.get_status("burning")
            self.take_damage(damage)
            return f"{self.name}受到了{damage}点火伤"
        
        if self.has_status("poison"):
            poison = self.get_status("poison")
            self.take_damage(poison)
            return f"{self.name}受到了{poison}点毒伤害"
        
        return None
    
    def is_alive(self):
        """检查是否存活"""
        return self.hp > 0
