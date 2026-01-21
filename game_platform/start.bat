@echo off
chcp 65001 >nul
echo ========================================
echo 游戏平台启动器
echo ========================================
echo.
echo 正在启动游戏平台...
echo.
python main.py
if errorlevel 1 (
    echo.
    echo 程序运行出错，请检查错误信息
    pause
)
