"""
战斗UI界面
"""
import pygame
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui.font_manager import FontManager
from battle_system import BattleState


class BattleUI:
    """战斗UI界面"""
    
    def __init__(self, width=1200, height=800):
        """
        初始化战斗UI
        
        Args:
            width: 窗口宽度
            height: 窗口高度
        """
        self.width = width
        self.height = height
        self.font_manager = FontManager()
        
        # 颜色定义
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 100, 200)
        self.GRAY = (128, 128, 128)
        self.DARK_GRAY = (64, 64, 64)
        self.LIGHT_GRAY = (200, 200, 200)
        self.YELLOW = (255, 255, 0)
        self.ORANGE = (255, 165, 0)
        
        # 卡牌颜色
        self.CARD_ATTACK = (200, 50, 50)
        self.CARD_SKILL = (50, 100, 200)
        self.CARD_ABILITY = (150, 50, 150)
        self.CARD_CURSE = (100, 100, 100)
    
    def init(self):
        """初始化pygame"""
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("卡牌Roguelike")
        self.clock = pygame.time.Clock()
    
    def draw_battle(self, battle_system):
        """
        绘制战斗界面

        Args:
            battle_system: 战斗系统对象
        """
        self.screen.fill(self.DARK_GRAY)

        # 获取战斗状态
        status = battle_system.get_battle_status()

        # 绘制各个区域
        self._draw_player_info(status, battle_system.player.name)
        self._draw_enemy_info(status, battle_system.enemy.name)
        self._draw_hand_cards(battle_system.player)
        self._draw_deck_info(status)
        self._draw_battle_log(status)
        self._draw_action_buttons(status)
        self._draw_battle_state(status)
    
    def _draw_player_info(self, status, player_name):
        """绘制玩家信息"""
        x, y = 50, 50
        width, height = 250, 150

        # 背景框
        pygame.draw.rect(self.screen, (50, 50, 50), (x, y, width, height), border_radius=10)
        pygame.draw.rect(self.screen, self.WHITE, (x, y, width, height), 2, border_radius=10)

        # 名称
        font = self.font_manager.get_large_font()
        name_text = font.render(f"{player_name}", True, self.WHITE)
        self.screen.blit(name_text, (x + 10, y + 10))
        
        # 生命值
        font = self.font_manager.get_medium_font()
        hp_text = font.render(f"HP: {status['player_hp']}/{status['player_max_hp']}", True, self.RED)
        self.screen.blit(hp_text, (x + 10, y + 50))
        
        # 能量
        energy_text = font.render(f"能量: {status['player_energy']}/{status['player_max_energy']}", True, self.YELLOW)
        self.screen.blit(energy_text, (x + 10, y + 80))
        
        # 护甲
        armor_text = font.render(f"护甲: {status['player_armor']}", True, self.BLUE)
        self.screen.blit(armor_text, (x + 10, y + 110))
    
    def _draw_enemy_info(self, status, enemy_name):
        """绘制敌人信息"""
        x, y = 900, 50
        width, height = 250, 150

        # 背景框
        pygame.draw.rect(self.screen, (50, 50, 50), (x, y, width, height), border_radius=10)
        pygame.draw.rect(self.screen, self.WHITE, (x, y, width, height), 2, border_radius=10)

        # 名称
        font = self.font_manager.get_large_font()
        name_text = font.render(f"{enemy_name}", True, self.WHITE)
        self.screen.blit(name_text, (x + 10, y + 10))
        
        # 生命值
        font = self.font_manager.get_medium_font()
        hp_text = font.render(f"HP: {status['enemy_hp']}/{status['enemy_max_hp']}", True, self.RED)
        self.screen.blit(hp_text, (x + 10, y + 50))
        
        # 护甲
        armor_text = font.render(f"护甲: {status['enemy_armor']}", True, self.BLUE)
        self.screen.blit(armor_text, (x + 10, y + 80))
        
        # 意图
        font = self.font_manager.get_small_font()
        intent_text = font.render(status['enemy_intent'], True, self.ORANGE)
        # 多行显示
        lines = status['enemy_intent'].split(' ')
        for i, line in enumerate(lines):
            line_text = font.render(line, True, self.ORANGE)
            self.screen.blit(line_text, (x + 10, y + 110 + i * 20))
    
    def _draw_hand_cards(self, player):
        """绘制手牌"""
        card_width = 120
        card_height = 160
        spacing = 130
        start_x = 50
        y = 550
        
        font = self.font_manager.get_card_font()
        
        for i, card in enumerate(player.hand):
            x = start_x + i * spacing
            
            # 根据卡牌类型选择颜色
            if card.card_type.value == "攻击":
                color = self.CARD_ATTACK
            elif card.card_type.value == "技能":
                color = self.CARD_SKILL
            elif card.card_type.value == "能力":
                color = self.CARD_ABILITY
            else:
                color = self.CARD_CURSE
            
            # 卡牌背景
            pygame.draw.rect(self.screen, color, (x, y, card_width, card_height), border_radius=8)
            pygame.draw.rect(self.screen, self.WHITE, (x, y, card_width, card_height), 2, border_radius=8)
            
            # 卡牌名称
            name_text = font.render(card.name, True, self.WHITE)
            name_rect = name_text.get_rect(center=(x + card_width // 2, y + 30))
            self.screen.blit(name_text, name_rect)
            
            # 能量消耗
            cost_text = font.render(str(card.cost), True, self.YELLOW)
            pygame.draw.circle(self.screen, self.BLACK, (x + 20, y + 20), 15)
            cost_rect = cost_text.get_rect(center=(x + 20, y + 20))
            self.screen.blit(cost_text, cost_rect)
            
            # 卡牌类型
            type_text = font.render(card.card_type.value, True, self.LIGHT_GRAY)
            type_rect = type_text.get_rect(center=(x + card_width // 2, y + 60))
            self.screen.blit(type_text, type_rect)
            
            # 卡牌描述
            desc_font = self.font_manager.get_small_font()
            desc_lines = self._wrap_text(card.description, desc_font, card_width - 20)
            for j, line in enumerate(desc_lines):
                line_text = desc_font.render(line, True, self.WHITE)
                line_rect = line_text.get_rect(center=(x + card_width // 2, y + 90 + j * 18))
                self.screen.blit(line_text, line_rect)
            
            # 卡牌编号
            num_text = font.render(str(i + 1), True, self.YELLOW)
            num_rect = num_text.get_rect(center=(x + card_width // 2, y + card_height - 20))
            self.screen.blit(num_text, num_rect)
    
    def _wrap_text(self, text, font, max_width):
        """文本换行"""
        words = list(text)
        lines = []
        current_line = ""
        
        for char in words:
            test_line = current_line + char
            if font.size(test_line)[0] > max_width:
                lines.append(current_line)
                current_line = char
            else:
                current_line = test_line
        
        if current_line:
            lines.append(current_line)
        
        return lines
    
    def _draw_deck_info(self, status):
        """绘制牌库信息"""
        x, y = 900, 550
        width, height = 250, 200
        
        # 背景框
        pygame.draw.rect(self.screen, (50, 50, 50), (x, y, width, height), border_radius=10)
        pygame.draw.rect(self.screen, self.WHITE, (x, y, width, height), 2, border_radius=10)
        
        font = self.font_manager.get_medium_font()
        
        # 牌库
        deck_text = font.render(f"牌库: {status['deck_size']}张", True, self.WHITE)
        self.screen.blit(deck_text, (x + 10, y + 10))
        
        # 弃牌堆
        discard_text = font.render(f"弃牌: {status['discard_size']}张", True, self.WHITE)
        self.screen.blit(discard_text, (x + 10, y + 50))
        
        # 手牌数
        hand_text = font.render(f"手牌: {status['hand_size']}张", True, self.WHITE)
        self.screen.blit(hand_text, (x + 10, y + 90))
        
        # 回合数
        turn_text = font.render(f"回合: {status['turn']}", True, self.YELLOW)
        self.screen.blit(turn_text, (x + 10, y + 130))
    
    def _draw_battle_log(self, status):
        """绘制战斗日志"""
        x, y = 50, 220
        width, height = 830, 300
        
        # 背景框
        pygame.draw.rect(self.screen, (30, 30, 30), (x, y, width, height), border_radius=10)
        pygame.draw.rect(self.screen, self.GRAY, (x, y, width, height), 2, border_radius=10)
        
        font = self.font_manager.get_small_font()
        
        # 显示最近的日志
        log_y = y + 10
        for log in status['log'][-10:]:  # 只显示最近10条
            log_text = font.render(log, True, self.WHITE)
            self.screen.blit(log_text, (x + 10, log_y))
            log_y += 25
    
    def _draw_action_buttons(self, status):
        """绘制操作按钮"""
        button_width = 150
        button_height = 50
        spacing = 20
        start_x = 900
        y = 760
        
        font = self.font_manager.get_medium_font()
        
        # 结束回合按钮
        end_turn_rect = pygame.Rect(start_x, y, button_width, button_height)
        pygame.draw.rect(self.screen, self.RED, end_turn_rect, border_radius=8)
        pygame.draw.rect(self.screen, self.WHITE, end_turn_rect, 2, border_radius=8)
        
        end_turn_text = font.render("结束回合", True, self.WHITE)
        end_turn_text_rect = end_turn_text.get_rect(center=end_turn_rect.center)
        self.screen.blit(end_turn_text, end_turn_text_rect)
        
        # 查看牌库按钮
        view_deck_rect = pygame.Rect(start_x + button_width + spacing, y, button_width, button_height)
        pygame.draw.rect(self.screen, self.BLUE, view_deck_rect, border_radius=8)
        pygame.draw.rect(self.screen, self.WHITE, view_deck_rect, 2, border_radius=8)
        
        view_deck_text = font.render("查看牌库", True, self.WHITE)
        view_deck_text_rect = view_deck_text.get_rect(center=view_deck_rect.center)
        self.screen.blit(view_deck_text, view_deck_text_rect)
    
    def _draw_battle_state(self, status):
        """绘制战斗状态"""
        font = self.font_manager.get_title_font()
        
        if status['state'] == "胜利":
            text = font.render("战斗胜利！", True, self.GREEN)
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(text, text_rect)
        elif status['state'] == "失败":
            text = font.render("战斗失败...", True, self.RED)
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(text, text_rect)
    
    def flip(self):
        """更新显示"""
        pygame.display.flip()
    
    def tick(self, fps=60):
        """控制帧率"""
        self.clock.tick(fps)
