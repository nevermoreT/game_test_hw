# -*- coding: utf-8 -*-
"""
测试中文显示效果
"""
import pygame
import sys
import os
import io

# 设置标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("中文显示测试")
print("=" * 60)

# 初始化pygame
pygame.init()

# 测试字体路径
font_paths = [
    "C:/Windows/Fonts/msyh.ttc",      # 微软雅黑
    "C:/Windows/Fonts/simhei.ttf",    # 黑体
    "C:/Windows/Fonts/simsun.ttc",    # 宋体
]

print("\n[测试1] 检查中文字体文件...")
for font_path in font_paths:
    if os.path.exists(font_path):
        print(f"  ✓ 找到字体: {font_path}")
    else:
        print(f"  ✗ 未找到字体: {font_path}")

print("\n[测试2] 测试字体加载...")
test_texts = [
    "游戏中心",
    "贪吃蛇",
    "得分",
    "游戏结束",
    "按ESC返回主菜单",
    "按空格键重新开始"
]

font_loaded = False
for font_path in font_paths:
    if os.path.exists(font_path):
        try:
            # 创建不同大小的字体
            font_small = pygame.font.Font(font_path, 24)
            font_medium = pygame.font.Font(font_path, 36)
            font_large = pygame.font.Font(font_path, 72)
            
            print(f"  ✓ 成功加载字体: {font_path}")
            print(f"  ✓ 字体大小: 24, 36, 72")
            font_loaded = True
            break
        except Exception as e:
            print(f"  ✗ 加载字体失败: {e}")
            continue

if not font_loaded:
    print("  ✗ 无法加载中文字体，使用默认字体")
    font_small = pygame.font.Font(None, 24)
    font_medium = pygame.font.Font(None, 36)
    font_large = pygame.font.Font(None, 72)

print("\n[测试3] 测试中文文本渲染...")
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("中文显示测试")

# 测试渲染中文文本
y_offset = 50
for text in test_texts:
    try:
        text_surface = font_medium.render(text, True, (255, 255, 255))
        print(f"  ✓ 成功渲染: '{text}'")
        print(f"    文本尺寸: {text_surface.get_size()}")
    except Exception as e:
        print(f"  ✗ 渲染失败: '{text}' - {e}")

print("\n[测试4] 显示测试窗口...")
screen.fill((64, 64, 64))

# 绘制测试文本
y_offset = 100
for i, text in enumerate(test_texts):
    if i < 3:
        font = font_large
    else:
        font = font_medium
    
    try:
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 80
    except Exception as e:
        print(f"  绘制 '{text}' 失败: {e}")

pygame.display.flip()

print("\n测试窗口已打开，显示2秒后关闭...")
print("请检查窗口中的中文是否正常显示")
pygame.time.wait(2000)

pygame.quit()

print("\n" + "=" * 60)
print("中文显示测试完成!")
print("=" * 60)
print("\n如果窗口中的中文显示正常，说明字体配置成功！")
print("现在可以运行 'python main.py' 启动游戏平台")
