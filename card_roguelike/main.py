"""
卡牌Roguelike游戏主程序
"""
import pygame
import sys
import random
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from characters import Warrior
from enemies import GoblinWarrior, GoblinArcher, Slime
from battle_system import BattleSystem, BattleState
from ui import BattleUI


class Game:
    """游戏主类"""
    
    def __init__(self):
        """初始化游戏"""
        self.ui = BattleUI()
        self.ui.init()
        
        # 创建玩家角色
        self.player = Warrior()
        
        # 创建敌人
        self.enemies = [GoblinWarrior(), GoblinArcher(), Slime()]
        self.current_enemy_index = 0
        
        # 创建战斗系统
        self.enemy = self.enemies[self.current_enemy_index]
        self.battle_system = BattleSystem(self.player, self.enemy)
        
        # 开始第一回合
        self.battle_system.start_player_turn()
        
        self.running = True
    
    def handle_events(self):
        """处理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            
            elif event.type == pygame.KEYDOWN:
                # ESC退出
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return
                
                # 检查战斗是否结束
                if self.battle_system.is_battle_over():
                    # 按任意键继续或退出
                    if event.key == pygame.K_SPACE:
                        if self.battle_system.state == BattleState.VICTORY:
                            # 继续下一个敌人
                            self.next_enemy()
                        else:
                            # 游戏结束
                            self.running = False
                    return
                
                # 玩家回合才能操作
                if self.battle_system.state == BattleState.PLAYER_TURN:
                    # 数字键1-9使用卡牌
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        card_index = event.key - pygame.K_1
                        if card_index < len(self.player.hand):
                            self.battle_system.play_card(card_index)
                    
                    # E键结束回合
                    elif event.key == pygame.K_e:
                        self.battle_system.end_player_turn()
                    
                    # 敌人回合自动执行
                    if self.battle_system.state == BattleState.ENEMY_TURN:
                        self.battle_system.execute_enemy_action()
    
    def next_enemy(self):
        """下一个敌人"""
        self.current_enemy_index += 1
        if self.current_enemy_index < len(self.enemies):
            # 创建新的战斗
            self.enemy = self.enemies[self.current_enemy_index]
            self.battle_system = BattleSystem(self.player, self.enemy)
            self.battle_system.start_player_turn()
        else:
            # 所有敌人都击败了
            self.running = False
    
    def update(self):
        """更新游戏状态"""
        pass
    
    def draw(self):
        """绘制游戏画面"""
        self.ui.draw_battle(self.battle_system)
        self.ui.flip()
    
    def run(self):
        """运行游戏主循环"""
        print("=" * 60)
        print("卡牌Roguelike游戏")
        print("=" * 60)
        print("\n操作说明:")
        print("  - 数字键1-9: 使用对应的卡牌")
        print("  - E键: 结束回合")
        print("  - ESC键: 退出游戏")
        print("  - 空格键: 战斗结束后继续")
        print("\n游戏开始！")
        print("=" * 60)
        
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.ui.tick()
        
        pygame.quit()
        print("\n游戏结束！")
        print(f"最终HP: {self.player.hp}/{self.player.max_hp}")


def main():
    """主函数"""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
