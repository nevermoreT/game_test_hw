# -*- coding: utf-8 -*-
"""
游戏平台测试脚本
测试各个模块的功能
"""
import sys
import os
import io

# 设置标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("开始测试游戏平台")
print("=" * 60)

# 测试1: 导入game_base
print("\n[测试1] 测试game_base模块...")
try:
    from game_base import GameBase
    print("✓ game_base模块导入成功")
    
    # 检查GameBase是否是抽象基类
    from abc import ABC
    assert issubclass(GameBase, ABC), "GameBase应该是ABC的子类"
    print("✓ GameBase是抽象基类")
    
    # 检查所有必需的抽象方法
    required_methods = [
        'get_name', 'get_description', 'init', 
        'handle_events', 'update', 'draw', 'cleanup'
    ]
    for method in required_methods:
        assert hasattr(GameBase, method), f"GameBase缺少方法: {method}"
    print(f"✓ GameBase包含所有必需的方法: {', '.join(required_methods)}")
    
except Exception as e:
    print(f"✗ 测试失败: {e}")
    sys.exit(1)

# 测试2: 导入snake_game
print("\n[测试2] 测试snake_game模块...")
try:
    from games.snake_game import SnakeGame
    print("✓ snake_game模块导入成功")
    
    # 检查SnakeGame是否是GameBase的子类
    assert issubclass(SnakeGame, GameBase), "SnakeGame应该是GameBase的子类"
    print("✓ SnakeGame是GameBase的子类")
    
    # 创建实例
    snake = SnakeGame(800, 600)
    print("✓ SnakeGame实例创建成功")
    
    # 测试必需方法
    assert hasattr(snake, 'get_name'), "缺少get_name方法"
    assert hasattr(snake, 'get_description'), "缺少get_description方法"
    assert hasattr(snake, 'init'), "缺少init方法"
    assert hasattr(snake, 'handle_events'), "缺少handle_events方法"
    assert hasattr(snake, 'update'), "缺少update方法"
    assert hasattr(snake, 'draw'), "缺少draw方法"
    assert hasattr(snake, 'cleanup'), "缺少cleanup方法"
    print("✓ SnakeGame包含所有必需的方法")
    
    # 测试get_name和get_description
    name = snake.get_name()
    desc = snake.get_description()
    print(f"✓ 游戏名称: {name}")
    print(f"✓ 游戏描述: {desc}")
    
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试3: 测试GameCenter
print("\n[测试3] 测试GameCenter模块...")
try:
    from main import GameCenter
    print("✓ GameCenter模块导入成功")
    
    # 创建实例
    center = GameCenter(800, 600)
    print("✓ GameCenter实例创建成功")
    
    # 测试load_games方法
    games = center.load_games()
    print(f"✓ 加载了 {len(games)} 个游戏")
    
    if len(games) > 0:
        for i, game in enumerate(games):
            print(f"  游戏{i+1}: {game.get_name()} - {game.get_description()}")
    else:
        print("  警告: 没有找到任何游戏")
    
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试4: 测试pygame是否可用
print("\n[测试4] 测试pygame环境...")
try:
    import pygame
    print(f"✓ pygame已安装")
    print(f"  版本: {pygame.version.ver}")
    
    # 测试pygame初始化
    pygame.init()
    print("✓ pygame初始化成功")
    
    # 测试创建窗口
    screen = pygame.display.set_mode((800, 600))
    print("✓ 创建测试窗口成功")
    
    # 测试关闭
    pygame.quit()
    print("✓ pygame关闭成功")
    
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("所有测试通过! ✓")
print("=" * 60)
print("\n提示: 运行 'python main.py' 启动游戏平台")
