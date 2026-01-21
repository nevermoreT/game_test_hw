"""
地精射手
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from enemies.enemy import Enemy, IntentType


class GoblinArcher(Enemy):
    """地精射手 - 普通敌人，初始带毒"""
    
    def __init__(self):
        super().__init__(
            name="地精射手",
            max_hp=30
        )
        
        # 行动模式：攻击→上毒→攻击
        self.actions = [
            {"type": IntentType.ATTACK, "value": 4},
            {"type": IntentType.DEBUFF, "value": 2},
            {"type": IntentType.ATTACK, "value": 4}
        ]
        
        # 初始带1层毒
        self.add_status("poison", 1)
        
        # 初始意图
        self.plan_next_action()
