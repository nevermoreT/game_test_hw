# -*- coding: utf-8 -*-
"""
卡牌Roguelike游戏测试脚本
"""
import sys
import os
import io

# 设置标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("卡牌Roguelike游戏测试")
print("=" * 60)

# 测试1: 导入模块
print("\n[测试1] 导入模块...")
try:
    from cards import Card, CardType, Strike, Defend, HeavyAttack
    from characters import Character, Warrior
    from enemies import Enemy, GoblinWarrior, GoblinArcher, Slime
    from battle_system import BattleSystem, BattleState
    from ui import FontManager, BattleUI
    print("✓ 所有模块导入成功")
except Exception as e:
    print(f"✗ 模块导入失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试2: 创建角色
print("\n[测试2] 创建角色...")
try:
    player = Warrior()
    print(f"✓ 创建战士成功")
    print(f"  名称: {player.name}")
    print(f"  HP: {player.hp}/{player.max_hp}")
    print(f"  能量: {player.energy}/{player.max_energy}")
    print(f"  牌库大小: {len(player.deck)}")
    print(f"  初始卡牌: {[card.name for card in player.deck]}")
except Exception as e:
    print(f"✗ 创建角色失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试3: 创建敌人
print("\n[测试3] 创建敌人...")
try:
    enemies = [
        GoblinWarrior(),
        GoblinArcher(),
        Slime()
    ]
    
    for enemy in enemies:
        print(f"✓ 创建{enemy.name}成功")
        print(f"  HP: {enemy.hp}/{enemy.max_hp}")
        print(f"  意图: {enemy.intent.value} {enemy.intent_value}")
except Exception as e:
    print(f"✗ 创建敌人失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试4: 战斗系统
print("\n[测试4] 测试战斗系统...")
try:
    player = Warrior()
    enemy = GoblinWarrior()
    battle = BattleSystem(player, enemy)
    
    print(f"✓ 战斗系统创建成功")
    print(f"  状态: {battle.state.value}")
    print(f"  回合数: {battle.turn_count}")
    
    # 开始玩家回合
    battle.start_player_turn()
    print(f"✓ 玩家回合开始")
    print(f"  手牌数: {len(player.hand)}")
    print(f"  手牌: {[card.name for card in player.hand]}")
    print(f"  能量: {player.energy}")
    
    # 使用一张攻击卡
    if len(player.hand) > 0:
        result = battle.play_card(0)
        print(f"✓ 使用卡牌成功: {result}")
        print(f"  敌人HP: {enemy.hp}/{enemy.max_hp}")
        print(f"  剩余能量: {player.energy}")
    
    # 结束回合
    battle.end_player_turn()
    print(f"✓ 结束玩家回合")
    print(f"  状态: {battle.state.value}")
    
    # 执行敌人行动
    battle.execute_enemy_action()
    print(f"✓ 敌人行动完成")
    print(f"  玩家HP: {player.hp}/{player.max_hp}")
    print(f"  状态: {battle.state.value}")
    
except Exception as e:
    print(f"✗ 战斗系统测试失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试5: pygame环境
print("\n[测试5] 测试pygame环境...")
try:
    import pygame
    print(f"✓ pygame已安装")
    print(f"  版本: {pygame.version.ver}")
    
    # 测试初始化
    pygame.init()
    print("✓ pygame初始化成功")
    
    # 测试UI
    ui = BattleUI()
    ui.init()
    print("✓ UI初始化成功")
    
    pygame.quit()
    print("✓ pygame关闭成功")
    
except Exception as e:
    print(f"✗ pygame测试失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试6: 完整战斗模拟
print("\n[测试6] 完整战斗模拟...")
try:
    player = Warrior()
    enemy = GoblinWarrior()
    battle = BattleSystem(player, enemy)
    
    print("开始战斗模拟...")
    battle.start_player_turn()
    
    # 模拟使用几张卡牌
    for i in range(min(3, len(player.hand))):
        if player.energy >= player.hand[0].cost:
            result = battle.play_card(0)
            print(f"  {result}")
    
    battle.end_player_turn()
    
    # 敌人回合
    battle.execute_enemy_action()
    
    print(f"✓ 战斗模拟完成")
    print(f"  玩家HP: {player.hp}/{player.max_hp}")
    print(f"  敌人HP: {enemy.hp}/{enemy.max_hp}")
    
except Exception as e:
    print(f"✗ 战斗模拟失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("所有测试通过! ✓")
print("=" * 60)
print("\n游戏已准备就绪，可以正常运行！")
print("\n运行命令: python main.py")
print("\n操作说明:")
print("  - 数字键1-9: 使用对应的卡牌")
print("  - E键: 结束回合")
print("  - ESC键: 退出游戏")
print("  - 空格键: 战斗结束后继续")
