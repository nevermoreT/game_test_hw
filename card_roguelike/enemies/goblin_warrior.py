"""
地精战士
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from enemies.enemy import Enemy, IntentType


class GoblinWarrior(Enemy):
    """地精战士 - 普通敌人"""
    
    def __init__(self):
        super().__init__(
            name="地精战士",
            max_hp=40
        )
        
        # 行动模式：攻击→防御→攻击
        self.actions = [
            {"type": IntentType.ATTACK, "value": 6},
            {"type": IntentType.DEFEND, "value": 5},
            {"type": IntentType.ATTACK, "value": 6}
        ]
        
        # 初始意图
        self.plan_next_action()
