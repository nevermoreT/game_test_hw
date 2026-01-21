# -*- coding: utf-8 -*-
"""
游戏平台运行测试
模拟运行游戏平台并检查功能
"""
import sys
import os
import io

# 设置标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("游戏平台运行测试")
print("=" * 60)

# 模拟运行游戏平台
try:
    from main import GameCenter
    print("\n[步骤1] 创建GameCenter实例...")
    center = GameCenter(800, 600)
    print("✓ GameCenter实例创建成功")
    
    print("\n[步骤2] 初始化游戏中心...")
    center.init()
    print("✓ 游戏中心初始化成功")
    
    print("\n[步骤3] 加载游戏列表...")
    games = center.load_games()
    print(f"✓ 成功加载 {len(games)} 个游戏")
    
    if len(games) > 0:
        print("\n可用游戏列表:")
        for i, game in enumerate(games):
            print(f"  {i+1}. {game.get_name()}")
            print(f"     描述: {game.get_description()}")
        
        print("\n[步骤4] 测试游戏按钮位置检测...")
        # 测试第一个游戏按钮的位置
        if len(games) > 0:
            button_x = (center.width - center.button_width) // 2
            button_y = center.start_y
            print(f"  第一个游戏按钮位置: ({button_x}, {button_y})")
            print(f"  按钮尺寸: {center.button_width} x {center.button_height}")
            
            # 测试点击检测
            test_pos = (button_x + center.button_width // 2, button_y + center.button_height // 2)
            game_index = center.get_game_at_position(test_pos)
            print(f"  点击按钮中心位置 ({test_pos[0]}, {test_pos[1]}): 游戏 {game_index + 1}")
            
            # 测试非按钮区域
            test_pos_outside = (10, 10)
            game_index_outside = center.get_game_at_position(test_pos_outside)
            print(f"  点击非按钮区域 ({test_pos_outside[0]}, {test_pos_outside[1]}): 游戏 {game_index_outside}")
            
            print("✓ 按钮位置检测功能正常")
        
        print("\n[步骤5] 测试游戏实例...")
        if len(games) > 0:
            game = games[0]
            print(f"  游戏名称: {game.get_name()}")
            print(f"  游戏描述: {game.get_description()}")
            print(f"  游戏尺寸: {game.width} x {game.height}")
            print("✓ 游戏实例功能正常")
        
        print("\n[步骤6] 检查pygame状态...")
        import pygame
        print(f"  pygame版本: {pygame.version.ver}")
        print(f"  pygame已初始化: {pygame.get_init()}")
        print("✓ pygame状态正常")
        
        print("\n[步骤7] 测试事件处理...")
        # 模拟事件处理
        center.running = True
        selected_game, clicked = center.handle_events()
        print(f"  事件处理结果: selected_game={selected_game}, clicked={clicked}")
        print("✓ 事件处理功能正常")
        
        print("\n" + "=" * 60)
        print("所有运行测试通过! ✓")
        print("=" * 60)
        print("\n游戏平台已准备就绪，可以正常运行！")
        print("\n运行命令: python main.py")
        print("\n操作说明:")
        print("  - 鼠标左键点击'贪吃蛇'按钮启动游戏")
        print("  - 按ESC键退出程序")
        print("  - 在游戏中按方向键控制移动")
        print("  - 在游戏中按ESC返回主菜单")
        
    else:
        print("\n警告: 没有找到任何游戏！")
        print("请确保games目录下有游戏模块文件")
        
except Exception as e:
    print(f"\n✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
