"""
游戏平台主程序
游戏中心首页，负责扫描和加载游戏模块，提供游戏选择界面
"""
import pygame
import sys
import os
import importlib.util
from pathlib import Path


class GameCenter:
    """游戏中心，负责管理和启动游戏"""
    
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.games = []
        self.screen = None
        self.clock = None
        self.running = True
        self.current_game = None
        
        # 颜色定义
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (128, 128, 128)
        self.DARK_GRAY = (64, 64, 64)
        self.BLUE = (0, 100, 200)
        self.LIGHT_BLUE = (100, 150, 255)
        self.HOVER_COLOR = (0, 120, 220)
        
        # 中文字体设置
        self.chinese_font = None
        self.chinese_font_title = None
        self.chinese_font_desc = None
        
        # 按钮配置
        self.button_width = 300
        self.button_height = 60
        self.button_spacing = 20
        self.start_y = 150
        
    def load_games(self):
        """
        扫描并加载games目录下的所有游戏模块
        
        Returns:
            list: 游戏实例列表
        """
        games = []
        games_dir = Path(__file__).parent / "games"
        
        if not games_dir.exists():
            print(f"警告: 游戏目录 {games_dir} 不存在")
            return games
        
        # 遍历games目录下的所有Python文件
        for file_path in games_dir.glob("*.py"):
            # 跳过__init__.py
            if file_path.name == "__init__.py":
                continue
            
            try:
                # 动态导入模块
                module_name = file_path.stem
                spec = importlib.util.spec_from_file_location(
                    f"games.{module_name}",
                    file_path
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # 查找GameBase的子类
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    # 检查是否是类且是GameBase的子类
                    if (isinstance(attr, type) and 
                        attr_name != "GameBase" and
                        hasattr(attr, "get_name")):
                        # 创建游戏实例
                        game_instance = attr(self.width, self.height)
                        games.append(game_instance)
                        print(f"已加载游戏: {game_instance.get_name()}")
                        
            except Exception as e:
                print(f"加载游戏模块 {file_path.name} 失败: {e}")
        
        return games
    
    def init(self):
        """初始化游戏中心"""
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("游戏中心")
        self.clock = pygame.time.Clock()
        
        # 初始化中文字体
        self.init_chinese_fonts()
        
        # 加载所有游戏
        self.games = self.load_games()
        
        if not self.games:
            print("警告: 没有找到任何游戏模块")
    
    def init_chinese_fonts(self):
        """初始化中文字体"""
        # Windows系统中文字体路径
        font_paths = [
            "C:/Windows/Fonts/msyh.ttc",      # 微软雅黑
            "C:/Windows/Fonts/simhei.ttf",    # 黑体
            "C:/Windows/Fonts/simsun.ttc",    # 宋体
            "C:/Windows/Fonts/msyhbd.ttc",    # 微软雅黑粗体
        ]
        
        # 尝试加载中文字体
        font_loaded = False
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    self.chinese_font = pygame.font.Font(font_path, 36)
                    self.chinese_font_title = pygame.font.Font(font_path, 72)
                    self.chinese_font_desc = pygame.font.Font(font_path, 24)
                    font_loaded = True
                    print(f"已加载中文字体: {font_path}")
                    break
                except Exception as e:
                    print(f"加载字体 {font_path} 失败: {e}")
                    continue
        
        # 如果加载失败，使用默认字体
        if not font_loaded:
            print("警告: 无法加载中文字体，使用默认字体（中文可能显示为乱码）")
            self.chinese_font = pygame.font.Font(None, 36)
            self.chinese_font_title = pygame.font.Font(None, 72)
            self.chinese_font_desc = pygame.font.Font(None, 24)
    
    def draw_button(self, screen, text, x, y, width, height, mouse_pos, clicked=False):
        """
        绘制按钮
        
        Args:
            screen: pygame屏幕对象
            text: 按钮文本
            x, y: 按钮位置
            width, height: 按钮尺寸
            mouse_pos: 鼠标位置
            clicked: 是否被点击
            
        Returns:
            bool: 按钮是否被点击
        """
        # 检查鼠标是否悬停在按钮上
        button_rect = pygame.Rect(x, y, width, height)
        is_hovered = button_rect.collidepoint(mouse_pos)
        
        # 选择颜色
        if clicked:
            color = self.HOVER_COLOR
        elif is_hovered:
            color = self.LIGHT_BLUE
        else:
            color = self.BLUE
        
        # 绘制按钮
        pygame.draw.rect(screen, color, button_rect, border_radius=10)
        pygame.draw.rect(screen, self.WHITE, button_rect, 2, border_radius=10)
        
        # 绘制按钮文本（使用中文字体）
        text_surface = self.chinese_font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        screen.blit(text_surface, text_rect)
        
        return is_hovered and clicked
    
    def draw_menu(self, screen, mouse_pos, clicked):
        """
        绘制游戏选择菜单
        
        Args:
            screen: pygame屏幕对象
            mouse_pos: 鼠标位置
            clicked: 是否点击
            
        Returns:
            int: 被点击的游戏索引，如果没有点击返回-1
        """
        screen.fill(self.DARK_GRAY)
        
        # 绘制标题（使用中文字体）
        title_text = self.chinese_font_title.render("游戏中心", True, self.WHITE)
        title_rect = title_text.get_rect(center=(self.width // 2, 80))
        screen.blit(title_text, title_rect)
        
        # 绘制游戏按钮
        selected_game = -1
        for i, game in enumerate(self.games):
            button_x = (self.width - self.button_width) // 2
            button_y = self.start_y + i * (self.button_height + self.button_spacing)
            
            # 检查是否点击
            if self.draw_button(
                screen, 
                game.get_name(), 
                button_x, 
                button_y, 
                self.button_width, 
                self.button_height,
                mouse_pos,
                clicked
            ):
                selected_game = i
            
            # 绘制游戏描述（使用中文字体）
            desc_text = self.chinese_font_desc.render(
                game.get_description(), 
                True, 
                self.GRAY
            )
            desc_rect = desc_text.get_rect(
                center=(self.width // 2, button_y + self.button_height + 15)
            )
            screen.blit(desc_text, desc_rect)
        
        # 绘制退出提示（使用中文字体）
        tip_text = self.chinese_font_desc.render("按ESC退出", True, self.GRAY)
        tip_rect = tip_text.get_rect(center=(self.width // 2, self.height - 30))
        screen.blit(tip_text, tip_rect)
        
        return selected_game
    
    def run_game(self, game_index):
        """
        运行指定的游戏
        
        Args:
            game_index: 游戏索引
        """
        if 0 <= game_index < len(self.games):
            game = self.games[game_index]
            print(f"启动游戏: {game.get_name()}")
            
            # 运行游戏
            game.run()
            
            print(f"游戏结束: {game.get_name()}")
    
    def handle_events(self):
        """处理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return None, False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return None, False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键点击
                    mouse_pos = pygame.mouse.get_pos()
                    selected_game = self.get_game_at_position(mouse_pos)
                    if selected_game >= 0:
                        return selected_game, True
        
        return None, False
    
    def get_game_at_position(self, pos):
        """
        获取指定位置的游戏索引
        
        Args:
            pos: 鼠标位置 (x, y)
            
        Returns:
            int: 游戏索引，如果没有返回-1
        """
        x, y = pos
        button_x = (self.width - self.button_width) // 2
        
        for i in range(len(self.games)):
            button_y = self.start_y + i * (self.button_height + self.button_spacing)
            button_rect = pygame.Rect(
                button_x, 
                button_y, 
                self.button_width, 
                self.button_height + 30  # 包括描述的高度
            )
            
            if button_rect.collidepoint(x, y):
                return i
        
        return -1
    
    def run(self):
        """运行游戏中心主循环"""
        self.init()
        
        while self.running:
            # 处理事件
            selected_game, clicked = self.handle_events()
            
            # 如果有游戏被点击，运行该游戏
            if selected_game is not None and selected_game >= 0 and clicked:
                self.run_game(selected_game)
                # 重新初始化pygame（游戏可能修改了状态）
                pygame.init()
                self.screen = pygame.display.set_mode((self.width, self.height))
                pygame.display.set_caption("游戏中心")
                self.clock = pygame.time.Clock()
            
            # 绘制菜单
            mouse_pos = pygame.mouse.get_pos()
            self.draw_menu(self.screen, mouse_pos, False)
            
            # 更新显示
            pygame.display.flip()
            
            # 控制帧率
            self.clock.tick(60)
        
        # 退出
        pygame.quit()
        sys.exit()


def main():
    """主函数"""
    game_center = GameCenter()
    game_center.run()


if __name__ == "__main__":
    main()
