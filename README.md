# Game Platform - 多游戏平台

一个基于Python和Pygame开发的插件式多游戏平台，支持动态加载和管理多个独立游戏模块。

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📖 项目简介

本项目实现了一个完整的游戏平台架构，采用插件式设计，每个游戏都是独立的模块。平台提供了统一的用户界面和游戏管理系统，支持自动发现和加载游戏模块。

### 核心特性

- ✅ **插件式架构**: 每个游戏独立模块，互不干扰
- ✅ **自动发现**: 自动扫描并加载games目录下的所有游戏
- ✅ **统一界面**: 提供一致的用户体验
- ✅ **中文支持**: 完整的中文界面和字体支持
- ✅ **易于扩展**: 添加新游戏无需修改核心代码

## 🎮 包含的游戏

### 1. 贪吃蛇（Snake）
- **类型**: 经典动作游戏
- **特色**: 方向键控制，吃食物得分
- **难度**: 简单

### 2. 卡牌Roguelike（Card Roguelike）
- **类型**: 策略卡牌战斗游戏
- **特色**: 回合制战斗，卡牌构筑，敌人AI
- **难度**: 中等

## 📁 项目结构

```
game_test_hw/
├── game_platform/               # 游戏平台主目录
│   ├── main.py                  # 游戏中心主程序
│   ├── game_base.py             # 游戏基类接口
│   ├── games/                   # 游戏模块目录
│   │   ├── snake_game.py        # 贪吃蛇游戏
│   │   └── card_roguelike_game.py # 卡牌Roguelike游戏
│   ├── README.md                # 平台说明文档
│   ├── GAME_MANUAL.md           # 完整游戏手册
│   ├── QUICK_START.md           # 快速入门指南
│   └── start.bat                # Windows启动脚本
│
├── card_roguelike/              # 卡牌Roguelike游戏独立目录
│   ├── main.py                  # 独立运行入口
│   ├── battle_system.py         # 战斗系统
│   ├── cards/                   # 卡牌模块
│   ├── characters/              # 角色模块
│   ├── enemies/                 # 敌人模块
│   ├── ui/                      # UI模块
│   └── README.md                # 游戏说明
│
├── .gitignore                   # Git忽略文件
└── README.md                    # 项目说明文档
```

## 🚀 快速开始

### 环境要求

- Python 3.6 或更高版本
- Pygame 2.0 或更高版本

### 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/nevermoreT/game_test_hw.git
   cd game_test_hw
   ```

2. **安装依赖**
   ```bash
   pip install pygame
   ```

3. **启动游戏平台**
   ```bash
   cd game_platform
   python main.py
   ```

   或在Windows上双击 `start.bat`

### 运行独立游戏

#### 贪吃蛇
```bash
cd game_platform
python main.py
# 在游戏中心选择"贪吃蛇"
```

#### 卡牌Roguelike
```bash
cd card_roguelike
python main.py
```

## 📚 文档

- [完整游戏手册](game_platform/GAME_MANUAL.md) - 详细的安装、操作和技巧说明
- [快速入门指南](game_platform/QUICK_START.md) - 快速上手必备
- [平台说明文档](game_platform/README.md) - 平台架构和扩展指南
- [卡牌游戏说明](card_roguelike/README.md) - 卡牌游戏详细说明

## 🎯 操作指南

### 游戏中心
- **鼠标左键**: 点击游戏按钮启动对应游戏
- **ESC键**: 退出游戏平台

### 贪吃蛇
- **方向键↑↓←→**: 控制蛇的移动方向
- **ESC键**: 返回游戏中心
- **空格键**: 游戏结束后重新开始

### 卡牌Roguelike
- **数字键1-9**: 使用手牌中对应的卡牌
- **E键**: 结束回合
- **ESC键**: 返回游戏中心
- **空格键**: 战斗结束后继续下一个敌人

## 🔧 开发指南

### 添加新游戏

1. 在 `game_platform/games/` 目录下创建新的Python文件
2. 继承 `GameBase` 类并实现必需的方法
3. 游戏中心会自动发现并加载新游戏

详细步骤请参考 [平台说明文档](game_platform/README.md)

### 扩展卡牌游戏

- 添加新卡牌: 在 `card_roguelike/cards/` 目录下创建新文件
- 添加新敌人: 在 `card_roguelike/enemies/` 目录下创建新文件
- 添加新角色: 在 `card_roguelike/characters/` 目录下创建新文件

详细指南请参考 [卡牌游戏说明](card_roguelike/README.md)

## 🛠️ 技术栈

- **语言**: Python 3.6+
- **图形库**: Pygame
- **架构**: 插件式架构
- **设计模式**: 工厂模式、策略模式

## 📊 项目统计

- **代码行数**: 3700+
- **文件数量**: 60+
- **游戏数量**: 2
- **卡牌数量**: 6+
- **敌人数量**: 3

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

感谢所有为本项目做出贡献的开发者和测试者！

特别感谢：
- Pygame 开发团队
- Python 社区
- 所有测试用户

## 📞 联系方式

- **项目主页**: https://github.com/nevermoreT/game_test_hw
- **问题反馈**: https://github.com/nevermoreT/game_test_hw/issues

## 📸 截图

### 游戏中心
![游戏中心](https://via.placeholder.com/800x600?text=Game+Center)

### 贪吃蛇
![贪吃蛇](https://via.placeholder.com/800x600?text=Snake+Game)

### 卡牌Roguelike
![卡牌Roguelike](https://via.placeholder.com/1200x800?text=Card+Roguelike+Game)

## 🔮 未来计划

- [ ] 地图系统
- [ ] 更多游戏（俄罗斯方块、打砖块等）
- [ ] 卡牌升级系统
- [ ] 遗物系统
- [ ] 更多角色职业
- [ ] 多人游戏模式
- [ ] 在线排行榜

---

**祝您游戏愉快！** 🎮
