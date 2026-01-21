"""
卡牌Roguelike游戏模块
整合到游戏平台中
"""
import pygame
import sys
import os
import importlib.util

# 导入游戏平台基类
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game_base import GameBase

# 导入卡牌游戏模块
# card_roguelike目录在game_platform的父目录中
card_game_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'card_roguelike')

CARD_GAME_AVAILABLE = False
Warrior = None
GoblinWarrior = None
GoblinArcher = None
Slime = None
BattleSystem = None
BattleState = None
BattleUI = None

try:
    # 添加路径到sys.path
    if card_game_path not in sys.path:
        sys.path.insert(0, card_game_path)

    # 使用spec方式导入card_roguelike包
    spec = importlib.util.spec_from_file_location("card_roguelike", os.path.join(card_game_path, "__init__.py"))
    card_roguelike_package = importlib.util.module_from_spec(spec)
    sys.modules["card_roguelike"] = card_roguelike_package
    spec.loader.exec_module(card_roguelike_package)

    # 导入各个模块
    spec_char = importlib.util.spec_from_file_location("card_roguelike.characters", os.path.join(card_game_path, "characters", "__init__.py"))
    characters_module = importlib.util.module_from_spec(spec_char)
    sys.modules["card_roguelike.characters"] = characters_module
    spec_char.loader.exec_module(characters_module)

    spec_enemy = importlib.util.spec_from_file_location("card_roguelike.enemies", os.path.join(card_game_path, "enemies", "__init__.py"))
    enemies_module = importlib.util.module_from_spec(spec_enemy)
    sys.modules["card_roguelike.enemies"] = enemies_module
    spec_enemy.loader.exec_module(enemies_module)

    spec_battle = importlib.util.spec_from_file_location("card_roguelike.battle_system", os.path.join(card_game_path, "battle_system.py"))
    battle_system_module = importlib.util.module_from_spec(spec_battle)
    sys.modules["card_roguelike.battle_system"] = battle_system_module
    spec_battle.loader.exec_module(battle_system_module)

    spec_ui = importlib.util.spec_from_file_location("card_roguelike.ui", os.path.join(card_game_path, "ui", "__init__.py"))
    ui_module = importlib.util.module_from_spec(spec_ui)
    sys.modules["card_roguelike.ui"] = ui_module
    spec_ui.loader.exec_module(ui_module)

    # 从模块中获取类
    Character = getattr(characters_module, 'Character')
    Warrior = getattr(characters_module, 'Warrior')
    Enemy = getattr(enemies_module, 'Enemy')
    GoblinWarrior = getattr(enemies_module, 'GoblinWarrior')
    GoblinArcher = getattr(enemies_module, 'GoblinArcher')
    Slime = getattr(enemies_module, 'Slime')
    BattleSystem = getattr(battle_system_module, 'BattleSystem')
    BattleState = getattr(battle_system_module, 'BattleState')
    BattleUI = getattr(ui_module, 'BattleUI')

    CARD_GAME_AVAILABLE = True
    print(f"成功导入卡牌游戏模块，路径: {card_game_path}")
except ImportError as e:
    print(f"警告: 无法导入卡牌游戏模块: {e}")
    print(f"尝试的路径: {card_game_path}")
    print(f"路径是否存在: {os.path.exists(card_game_path)}")
    if os.path.exists(card_game_path):
        print(f"路径内容: {os.listdir(card_game_path)}")
    import traceback
    traceback.print_exc()


class CardRoguelikeGame(GameBase):
    """卡牌Roguelike游戏实现"""

    def __init__(self, width=1200, height=800):
        super().__init__(width, height)

        if not CARD_GAME_AVAILABLE:
            print("错误: 卡牌游戏模块不可用")
            return

        # UI界面
        self.ui = None
        self.clock = None
        self.return_to_menu = False

        # 游戏状态
        self.player = None
        self.enemies = None
        self.current_enemy_index = 0
        self.battle_system = None
        self.running = False

    def get_name(self):
        return "卡牌Roguelike"

    def get_description(self):
        return "策略卡牌战斗游戏，使用卡牌击败敌人"

    def init(self):
        """初始化游戏"""
        if not CARD_GAME_AVAILABLE:
            print("错误: 卡牌游戏模块不可用")
            self.return_to_menu = True
            return

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("卡牌Roguelike - 按ESC返回主菜单")
        self.clock = pygame.time.Clock()

        # 初始化UI
        self.ui = BattleUI()
        self.ui.init()

        # 创建玩家角色
        self.player = Warrior()

        # 创建敌人列表
        self.enemies = [GoblinWarrior(), GoblinArcher(), Slime()]
        self.current_enemy_index = 0

        # 创建战斗系统
        self.enemy = self.enemies[self.current_enemy_index]
        self.battle_system = BattleSystem(self.player, self.enemy)

        # 开始第一回合
        self.battle_system.start_player_turn()

        self.running = True
        self.return_to_menu = False
        print("卡牌Roguelike游戏初始化成功")

    def handle_events(self, events):
        """处理游戏事件"""
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.return_to_menu = True
                    return

                # 检查战斗是否结束
                if self.battle_system.is_battle_over():
                    # 按任意键继续或退出
                    if event.key == pygame.K_SPACE:
                        if self.battle_system.state == BattleState.VICTORY:
                            # 继续下一个敌人
                            self.next_enemy()
                        else:
                            # 游戏结束，返回主菜单
                            self.return_to_menu = True
                    elif event.key == pygame.K_ESCAPE:
                        # 返回主菜单
                        self.return_to_menu = True
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
            # 所有敌人都击败了，返回主菜单
            print("恭喜！所有敌人都被击败了！")
            self.return_to_menu = True

    def update(self):
        """更新游戏逻辑"""
        pass

    def draw(self, screen):
        """绘制游戏画面"""
        if self.ui and self.battle_system:
            self.ui.draw_battle(self.battle_system)
            self.ui.flip()

    def cleanup(self):
        """清理游戏资源"""
        pass

    def should_return_to_menu(self):
        """检查是否应该返回主菜单"""
        return self.return_to_menu

    def run(self):
        """运行游戏主循环"""
        self.init()

        if not CARD_GAME_AVAILABLE:
            print("错误: 卡牌游戏模块不可用，无法运行")
            return

        print("\n" + "=" * 60)
        print("卡牌Roguelike游戏")
        print("=" * 60)
        print("\n操作说明:")
        print("  - 数字键1-9: 使用对应的卡牌")
        print("  - E键: 结束回合")
        print("  - ESC键: 返回主菜单")
        print("  - 空格键: 战斗结束后继续")
        print("\n游戏开始！")
        print("=" * 60)

        while self.running:
            # 检查是否返回主菜单
            if self.should_return_to_menu():
                break

            # 处理事件
            events = pygame.event.get()
            self.handle_events(events)

            # 更新游戏状态
            self.update()

            # 绘制游戏画面
            self.draw(self.screen)

            # 控制游戏速度
            self.clock.tick(60)

        # 清理资源
        self.cleanup()

        # 重新初始化pygame
        pygame.init()
