# -*- coding: utf-8 -*-
"""
快速运行测试 - 自动运行几秒后退出
"""
import pygame
import sys
import os
import time

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(__file__))

print("开始快速运行测试...")
print("游戏窗口将显示3秒后自动关闭")

try:
    from main import GameCenter
    
    # 创建并初始化游戏中心
    center = GameCenter(800, 600)
    center.init()
    
    print("游戏中心初始化成功")
    print("窗口已打开，正在测试...")
    
    # 运行3秒
    start_time = time.time()
    while time.time() - start_time < 3:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                center.running = False
                break
        
        # 绘制菜单
        mouse_pos = pygame.mouse.get_pos()
        center.draw_menu(center.screen, mouse_pos, False)
        
        # 更新显示
        pygame.display.flip()
        center.clock.tick(60)
    
    print("测试完成！")
    pygame.quit()
    
except Exception as e:
    print(f"运行出错: {e}")
    import traceback
    traceback.print_exc()
    pygame.quit()
