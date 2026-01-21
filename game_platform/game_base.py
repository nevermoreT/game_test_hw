"""
游戏基类接口
所有游戏模块都需要继承此类并实现相应方法
"""
from abc import ABC, abstractmethod


class GameBase(ABC):
    """游戏基类，定义游戏插件的标准接口"""
    
    def __init__(self, width=800, height=600):
        """
        初始化游戏
        
        Args:
            width: 游戏窗口宽度
            height: 游戏窗口高度
        """
        self.width = width
        self.height = height
        self.screen = None
        self.clock = None
        
    @abstractmethod
    def get_name(self):
        """
        获取游戏名称
        
        Returns:
            str: 游戏名称
        """
        pass
    
    @abstractmethod
    def get_description(self):
        """
        获取游戏描述
        
        Returns:
            str: 游戏描述
        """
        pass
    
    @abstractmethod
    def init(self):
        """初始化游戏资源和状态"""
        pass
    
    @abstractmethod
    def handle_events(self, events):
        """
        处理游戏事件
        
        Args:
            events: pygame事件列表
        """
        pass
    
    @abstractmethod
    def update(self):
        """更新游戏逻辑"""
        pass
    
    @abstractmethod
    def draw(self, screen):
        """
        绘制游戏画面
        
        Args:
            screen: pygame屏幕对象
        """
        pass
    
    @abstractmethod
    def cleanup(self):
        """清理游戏资源"""
        pass
    
    def should_return_to_menu(self):
        """
        检查是否应该返回主菜单
        
        Returns:
            bool: 如果返回True，则退出游戏返回主菜单
        """
        return False
