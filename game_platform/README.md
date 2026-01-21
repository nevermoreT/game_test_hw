# Python/Pygame 多游戏平台

一个基于Python和Pygame开发的插件式多游戏平台，支持动态加载游戏模块。

## 项目结构

```
game_platform/
├── main.py                      # 游戏中心主程序
├── game_base.py                 # 游戏基类接口
├── games/                       # 游戏模块目录
│   ├── __init__.py
│   ├── snake_game.py            # 贪吃蛇游戏模块
│   └── card_roguelike_game.py   # 卡牌Roguelike游戏模块
├── card_roguelike/              # 卡牌Roguelike游戏目录（可选）
│   ├── main.py
│   ├── battle_system.py
│   ├── cards/
│   ├── characters/
│   ├── enemies/
│   └── ui/
└── README.md                    # 项目说明文档
```

## 功能特性

### 1. 游戏中心首页
- 动态扫描并展示所有可用游戏
- 每个游戏显示为可点击按钮
- 显示游戏名称和描述
- 支持返回主菜单功能

### 2. 插件式架构
- 采用"插件模式"设计
- 每个游戏是独立模块
- 新游戏添加无需修改核心代码
- 自动发现和加载games目录下的游戏模块

### 3. 已实现游戏

#### 贪吃蛇（Snake）
- 方向键控制移动
- 吃到食物得分
- 撞墙或撞自己游戏结束
- 按ESC返回主菜单
- 按空格键重新开始

#### 卡牌Roguelike（Card Roguelike）
- 策略性卡牌战斗游戏
- 使用数字键1-9使用卡牌
- 按E键结束回合
- 战士职业：高生命值，擅长攻击和护甲
- 多种敌人：地精战士、地精射手、史莱姆
- 按ESC返回主菜单
- 按空格键战斗结束后继续

## 运行要求

- Python 3.6+
- Pygame

## 安装依赖

```bash
pip install pygame
```

## 运行程序

```bash
cd game_platform
python main.py
```

## 操作说明

### 游戏中心
- **鼠标左键**: 点击游戏按钮启动对应游戏
- **ESC键**: 退出程序

### 贪吃蛇游戏
- **方向键↑↓←→**: 控制蛇的移动方向
- **ESC键**: 返回游戏中心
- **空格键**: 游戏结束后重新开始

### 卡牌Roguelike游戏
- **数字键1-9**: 使用对应的卡牌
- **E键**: 结束回合
- **ESC键**: 返回游戏中心
- **空格键**: 战斗结束后继续下一个敌人

## 添加新游戏

### 步骤1: 创建游戏模块

在 `games/` 目录下创建新的Python文件（例如 `my_game.py`）

### 步骤2: 继承GameBase类

```python
from game_base import GameBase
import pygame

class MyGame(GameBase):
    def get_name(self):
        return "我的游戏"
    
    def get_description(self):
        return "游戏描述"
    
    def init(self):
        """初始化游戏资源和状态"""
        pass
    
    def handle_events(self, events):
        """处理游戏事件"""
        pass
    
    def update(self):
        """更新游戏逻辑"""
        pass
    
    def draw(self, screen):
        """绘制游戏画面"""
        pass
    
    def cleanup(self):
        """清理游戏资源"""
        pass
    
    def should_return_to_menu(self):
        """检查是否应该返回主菜单"""
        return False
```

### 步骤3: 实现游戏逻辑

实现所有必需的方法，完成游戏功能。

### 步骤4: 自动加载

游戏中心会自动发现并加载 `games/` 目录下的所有游戏模块，无需修改任何配置。

## 技术架构

### 游戏基类 (GameBase)
定义了游戏插件的标准接口：
- `get_name()`: 获取游戏名称
- `get_description()`: 获取游戏描述
- `init()`: 初始化游戏
- `handle_events()`: 处理事件
- `update()`: 更新逻辑
- `draw()`: 绘制画面
- `cleanup()`: 清理资源
- `should_return_to_menu()`: 返回菜单判断

### 游戏中心 (GameCenter)
- 扫描games目录
- 动态加载游戏模块
- 提供游戏选择界面
- 管理游戏生命周期

## 扩展性

该平台具有良好的扩展性：
- 添加新游戏只需创建新的游戏模块
- 不需要修改主程序代码
- 支持任意数量的游戏
- 每个游戏完全独立

## 未来可以添加的游戏

- 俄罗斯方块
- 打砖块
- 2048
- 扫雷
- 井字棋
- 贪吃蛇变种
- 更多卡牌Roguelike内容
- 等等...

## 许可证

MIT License
