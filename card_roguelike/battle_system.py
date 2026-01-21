"""
战斗系统
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from characters import Character
from enemies import Enemy
from enum import Enum


class BattleState(Enum):
    """战斗状态"""
    PLAYER_TURN = "玩家回合"
    ENEMY_TURN = "敌人回合"
    VICTORY = "胜利"
    DEFEAT = "失败"


class BattleSystem:
    """战斗系统"""
    
    def __init__(self, player: Character, enemy: Enemy):
        """
        初始化战斗系统
        
        Args:
            player: 玩家角色
            enemy: 敌人
        """
        self.player = player
        self.enemy = enemy
        self.state = BattleState.PLAYER_TURN
        self.turn_count = 0
        self.battle_log = []  # 战斗日志
        
        # 初始化牌组
        self.player.reset_deck()
        
        # 记录战斗开始
        self.add_log(f"战斗开始！{self.player.name} VS {self.enemy.name}")
    
    def add_log(self, message):
        """添加战斗日志"""
        self.battle_log.append(message)
        if len(self.battle_log) > 10:  # 只保留最近10条
            self.battle_log.pop(0)
    
    def start_player_turn(self):
        """开始玩家回合"""
        self.state = BattleState.PLAYER_TURN
        self.turn_count += 1
        self.add_log(f"\n=== 第{self.turn_count}回合 ===")
        
        # 玩家回合开始
        self.player.start_turn()
        self.add_log(f"{self.player.name}回合开始，能量: {self.player.energy}")
        
        # 抽牌（默认5张）
        self.player.draw_cards(5)
        self.add_log(f"抽了{len(self.player.hand)}张牌")
    
    def play_card(self, card_index):
        """
        玩家使用卡牌
        
        Args:
            card_index: 卡牌索引
        """
        if self.state != BattleState.PLAYER_TURN:
            return None
        
        result = self.player.play_card(card_index, self.enemy)
        if result:
            self.add_log(result)
            
            # 检查敌人是否死亡
            if not self.enemy.is_alive():
                self.state = BattleState.VICTORY
                self.add_log(f"{self.enemy.name}被击败！")
        
        return result
    
    def end_player_turn(self):
        """结束玩家回合"""
        if self.state != BattleState.PLAYER_TURN:
            return
        
        self.add_log(f"{self.player.name}结束回合")
        
        # 弃掉所有手牌
        self.player.discard_all()
        
        # 玩家回合结束
        self.player.end_turn()
        
        # 检查玩家是否死亡
        if not self.player.is_alive():
            self.state = BattleState.DEFEAT
            self.add_log(f"{self.player.name}战败了...")
            return
        
        # 开始敌人回合
        self.start_enemy_turn()
    
    def start_enemy_turn(self):
        """开始敌人回合"""
        self.state = BattleState.ENEMY_TURN
        self.add_log(f"{self.enemy.name}回合开始")
        
        # 敌人计划下一个行动
        self.enemy.plan_next_action()
        
        # 显示敌人意图
        intent_text = self.get_enemy_intent_text()
        self.add_log(intent_text)
    
    def execute_enemy_action(self):
        """执行敌人行动"""
        if self.state != BattleState.ENEMY_TURN:
            return
        
        # 执行敌人行动
        result = self.enemy.execute_action(self.player)
        self.add_log(result)
        
        # 检查玩家是否死亡
        if not self.player.is_alive():
            self.state = BattleState.DEFEAT
            self.add_log(f"{self.player.name}战败了...")
            return
        
        # 敌人回合结束
        self.end_enemy_turn()
    
    def end_enemy_turn(self):
        """结束敌人回合"""
        # 处理敌人状态效果
        status_result = self.enemy.end_turn()
        if status_result:
            self.add_log(status_result)
        
        # 检查敌人是否死亡
        if not self.enemy.is_alive():
            self.state = BattleState.VICTORY
            self.add_log(f"{self.enemy.name}被击败！")
            return
        
        self.enemy.clear_armor()
        
        # 开始玩家回合
        self.start_player_turn()
    
    def get_enemy_intent_text(self):
        """获取敌人意图文本"""
        if self.enemy.intent:
            return f"{self.enemy.name}的意图: {self.enemy.intent.value} {self.enemy.intent_value}"
        return f"{self.enemy.name}的意图: 未知"
    
    def is_battle_over(self):
        """检查战斗是否结束"""
        return self.state == BattleState.VICTORY or self.state == BattleState.DEFEAT
    
    def get_winner(self):
        """获取获胜者"""
        if self.state == BattleState.VICTORY:
            return self.player
        elif self.state == BattleState.DEFEAT:
            return self.enemy
        return None
    
    def get_battle_status(self):
        """获取战斗状态信息"""
        return {
            "state": self.state.value,
            "turn": self.turn_count,
            "player_hp": self.player.hp,
            "player_max_hp": self.player.max_hp,
            "player_energy": self.player.energy,
            "player_max_energy": self.player.max_energy,
            "player_armor": self.player.armor,
            "enemy_hp": self.enemy.hp,
            "enemy_max_hp": self.enemy.max_hp,
            "enemy_armor": self.enemy.armor,
            "enemy_intent": self.get_enemy_intent_text(),
            "hand_size": len(self.player.hand),
            "deck_size": len(self.player.deck),
            "discard_size": len(self.player.discard_pile),
            "log": self.battle_log
        }
