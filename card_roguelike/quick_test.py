# -*- coding: utf-8 -*-
"""
快速运行测试 - 自动运行几秒后退出
"""
import pygame
import sys
import os
import time
import io

# 设置标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(__file__))

print("开始快速运行测试...")
print("游戏窗口将显示3秒后自动关闭")

try:
    from main import Game
    
    # 创建游戏
    game = Game()
    
    print("游戏初始化成功")
    print("窗口已打开，正在测试...")
    
    # 运行3秒
    start_time = time.time()
    while time.time() - start_time < 3:
        game.handle_events()
        game.update()
        game.draw()
        game.ui.tick()
    
    print("测试完成！")
    pygame.quit()
    
except Exception as e:
    print(f"运行出错: {e}")
    import traceback
    traceback.print_exc()
    pygame.quit()
