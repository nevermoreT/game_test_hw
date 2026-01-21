"""
贪吃蛇游戏模块
"""
import pygame
import random
import sys
from game_base import GameBase


class SnakeGame(GameBase):
    """贪吃蛇游戏实现"""
    
    def __init__(self, width=800, height=600):
        super().__init__(width, height)
        
        # 游戏配置
        self.grid_size = 20  # 网格大小
        self.grid_width = width // self.grid_size
        self.grid_height = height // self.grid_size
        
        # 颜色定义
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (128, 128, 128)
        
        # 游戏状态
        self.snake = []
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
        self.food = None
        self.score = 0
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.return_to_menu = False
        
        # 中文字体
        self.chinese_font = None
        self.chinese_font_small = None
        self.chinese_font_large = None
        self.chinese_font_medium = None
        
    def get_name(self):
        return "贪吃蛇"
    
    def get_description(self):
        return "经典的贪吃蛇游戏，方向键控制移动，吃到食物得分"
    
    def init(self):
        """初始化游戏"""
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("贪吃蛇 - 按ESC返回主菜单")
        self.clock = pygame.time.Clock()
        
        # 初始化中文字体
        self.init_chinese_fonts()
        
        # 初始化蛇（从中间开始）
        start_x = self.grid_width // 2
        start_y = self.grid_height // 2
        self.snake = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y)
        ]
        
        # 生成第一个食物
        self.spawn_food()
        
        self.game_over = False
        self.score = 0
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
        self.return_to_menu = False
    
    def init_chinese_fonts(self):
        """初始化中文字体"""
        import os
        
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
                    self.chinese_font_small = pygame.font.Font(font_path, 24)
                    self.chinese_font_large = pygame.font.Font(font_path, 72)
                    self.chinese_font_medium = pygame.font.Font(font_path, 48)
                    font_loaded = True
                    break
                except Exception as e:
                    continue
        
        # 如果加载失败，使用默认字体
        if not font_loaded:
            self.chinese_font = pygame.font.Font(None, 36)
            self.chinese_font_small = pygame.font.Font(None, 24)
            self.chinese_font_large = pygame.font.Font(None, 72)
            self.chinese_font_medium = pygame.font.Font(None, 48)
    
    def spawn_food(self):
        """在随机位置生成食物"""
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break
    
    def handle_events(self, events):
        """处理游戏事件"""
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.return_to_menu = True
                elif event.key == pygame.K_SPACE and self.game_over:
                    # 游戏结束后按空格重新开始
                    self.init()
                else:
                    # 方向控制
                    if event.key == pygame.K_UP and self.direction != "DOWN":
                        self.next_direction = "UP"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.next_direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.next_direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.next_direction = "RIGHT"
    
    def update(self):
        """更新游戏逻辑"""
        if self.game_over or self.return_to_menu:
            return
        
        # 更新方向
        self.direction = self.next_direction
        
        # 计算新的蛇头位置
        head_x, head_y = self.snake[0]
        
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        else:  # RIGHT
            new_head = (head_x + 1, head_y)
        
        # 检查碰撞
        new_head_x, new_head_y = new_head
        
        # 撞墙检测
        if (new_head_x < 0 or new_head_x >= self.grid_width or
            new_head_y < 0 or new_head_y >= self.grid_height):
            self.game_over = True
            return
        
        # 撞自己检测
        if new_head in self.snake:
            self.game_over = True
            return
        
        # 移动蛇
        self.snake.insert(0, new_head)
        
        # 检查是否吃到食物
        if new_head == self.food:
            self.score += 10
            self.spawn_food()
        else:
            # 没吃到食物，移除蛇尾
            self.snake.pop()
    
    def draw(self, screen):
        """绘制游戏画面"""
        screen.fill(self.BLACK)
        
        # 绘制食物
        if self.food:
            food_rect = pygame.Rect(
                self.food[0] * self.grid_size,
                self.food[1] * self.grid_size,
                self.grid_size - 2,
                self.grid_size - 2
            )
            pygame.draw.rect(screen, self.RED, food_rect)
        
        # 绘制蛇
        for i, (x, y) in enumerate(self.snake):
            rect = pygame.Rect(
                x * self.grid_size,
                y * self.grid_size,
                self.grid_size - 2,
                self.grid_size - 2
            )
            # 蛇头用不同颜色
            if i == 0:
                pygame.draw.rect(screen, self.GREEN, rect)
            else:
                pygame.draw.rect(screen, self.BLUE, rect)
        
        # 绘制分数（使用中文字体）
        score_text = self.chinese_font.render(f"得分: {self.score}", True, self.WHITE)
        screen.blit(score_text, (10, 10))
        
        # 绘制提示（使用中文字体）
        tip_text = self.chinese_font_small.render("按ESC返回主菜单", True, self.GRAY)
        screen.blit(tip_text, (self.width - 200, 10))
        
        # 游戏结束显示
        if self.game_over:
            overlay = pygame.Surface((self.width, self.height))
            overlay.set_alpha(128)
            overlay.fill(self.BLACK)
            screen.blit(overlay, (0, 0))
            
            # 使用中文字体
            game_over_text = self.chinese_font_large.render("游戏结束!", True, self.RED)
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
            screen.blit(game_over_text, text_rect)
            
            final_score_text = self.chinese_font_medium.render(f"最终得分: {self.score}", True, self.WHITE)
            score_rect = final_score_text.get_rect(center=(self.width // 2, self.height // 2 + 20))
            screen.blit(final_score_text, score_rect)
            
            restart_text = self.chinese_font.render("按空格键重新开始", True, self.WHITE)
            restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 80))
            screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def cleanup(self):
        """清理游戏资源"""
        pass
    
    def should_return_to_menu(self):
        """检查是否应该返回主菜单"""
        return self.return_to_menu
    
    def run(self):
        """运行游戏主循环"""
        self.init()
        
        while True:
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
            self.clock.tick(10)  # 10 FPS
        
        # 清理资源
        self.cleanup()
