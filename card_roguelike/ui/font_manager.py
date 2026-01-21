"""
字体管理器
"""
import pygame
import os


class FontManager:
    """字体管理器"""
    
    def __init__(self):
        """初始化字体管理器"""
        self.fonts = {}
        self.chinese_font_path = self._find_chinese_font()
    
    def _find_chinese_font(self):
        """查找中文字体"""
        font_paths = [
            "C:/Windows/Fonts/msyh.ttc",      # 微软雅黑
            "C:/Windows/Fonts/simhei.ttf",    # 黑体
            "C:/Windows/Fonts/simsun.ttc",    # 宋体
            "C:/Windows/Fonts/msyhbd.ttc",    # 微软雅黑粗体
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                return font_path
        
        return None
    
    def get_font(self, size, bold=False):
        """
        获取字体
        
        Args:
            size: 字体大小
            bold: 是否粗体
        """
        key = (size, bold)
        if key not in self.fonts:
            if self.chinese_font_path:
                self.fonts[key] = pygame.font.Font(self.chinese_font_path, size)
            else:
                self.fonts[key] = pygame.font.Font(None, size)
        
        return self.fonts[key]
    
    def get_title_font(self):
        """获取标题字体"""
        return self.get_font(48)
    
    def get_large_font(self):
        """获取大字体"""
        return self.get_font(36)
    
    def get_medium_font(self):
        """获取中等字体"""
        return self.get_font(28)
    
    def get_small_font(self):
        """获取小字体"""
        return self.get_font(20)
    
    def get_card_font(self):
        """获取卡牌字体"""
        return self.get_font(24)
