# -*- coding: utf-8 -*-
"""
测试游戏平台中的所有游戏
"""
import sys
import os
import io

# 设置标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("游戏平台完整测试")
print("=" * 60)

# 测试1: 导入游戏平台
print("\n[测试1] 导入游戏平台...")
try:
    from main import GameCenter
    print("✓ GameCenter导入成功")
except Exception as e:
    print(f"✗ 导入失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试2: 创建游戏中心并加载所有游戏
print("\n[测试2] 加载所有游戏...")
try:
    center = GameCenter(800, 600)
    print(f"✓ GameCenter创建成功")
    
    games = center.load_games()
    print(f"✓ 成功加载 {len(games)} 个游戏")
    
    for i, game in enumerate(games):
        print(f"\n  游戏{i+1}:")
        print(f"    名称: {game.get_name()}")
        print(f"    描述: {game.get_description()}")
        
        # 测试游戏实例化
        try:
            game_instance = game.__class__(800, 600)
            print(f"    ✓ 游戏实例创建成功")
        except Exception as e:
            print(f"    ✗ 游戏实例创建失败: {e}")
    
except Exception as e:
    print(f"✗ 加载游戏失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试3: 测试贪吃蛇游戏
print("\n[测试3] 测试贪吃蛇游戏...")
try:
    from games.snake_game import SnakeGame
    snake = SnakeGame(800, 600)
    print(f"✓ 贪吃蛇游戏创建成功")
    print(f"  名称: {snake.get_name()}")
    print(f"  描述: {snake.get_description()}")
except Exception as e:
    print(f"✗ 贪吃蛇游戏测试失败: {e}")

# 测试4: 测试卡牌Roguelike游戏
print("\n[测试4] 测试卡牌Roguelike游戏...")
try:
    from games.card_roguelike_game import CardRoguelikeGame
    card_game = CardRoguelikeGame(1200, 800)
    print(f"✓ 卡牌Roguelike游戏创建成功")
    print(f"  名称: {card_game.get_name()}")
    print(f"  描述: {card_game.get_description()}")
except Exception as e:
    print(f"✗ 卡牌Roguelike游戏测试失败: {e}")

print("\n" + "=" * 60)
print("所有游戏测试完成！")
print("=" * 60)
print(f"\n游戏平台包含 {len(games)} 个游戏:")
for game in games:
    print(f"  - {game.get_name()}")
print("\n运行命令: python main.py")
print("\n操作说明:")
print("  - 鼠标左键点击游戏按钮启动对应游戏")
print("  - 按ESC键退出程序")
print("  - 在游戏中按ESC返回主菜单")
