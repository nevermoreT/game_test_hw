"""
史莱姆
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from enemies.enemy import Enemy, IntentType


class Slime(Enemy):
    """史莱姆 - 普通敌人"""
    
    def __init__(self):
        super().__init__(
            name="史莱姆",
            max_hp=50
        )
        
        # 行动模式：攻击→分裂→攻击
        self.actions = [
            {"type": IntentType.ATTACK, "value": 3},
            {"type": IntentType.BUFF, "value": 1},  # 分裂：获得力量
            {"type": IntentType.ATTACK, "value": 3}
        ]
        
        # 初始意图
        self.plan_next_action()
