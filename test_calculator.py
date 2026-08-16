# test_calculator.py
# 测试命令行工具：python calculator.py 1 2 应该输出 3
# 用 subprocess 模拟"在终端里运行命令"，
# 然后检查程序的输出对不对。


import subprocess
import sys
from pathlib import Path

# 拿到 calculator.py 的完整路径（不管在哪个目录运行测试都不会找错）
CALCULATOR = Path(__file__).parent / "calculator.py"


def run_cli(a, b):
    """模拟在终端运行：python calculator.py a b，返回运行结果"""
    result = subprocess.run(
        [sys.executable, str(CALCULATOR), str(a), str(b)],
        capture_output=True,   # 把输出"抓"回来，而不是打印到屏幕
        text=True,             # 让输出是字符串（而不是字节）
    )
    return result


def test_cli_1_plus_2():
    result = run_cli(1, 2)
    assert result.returncode == 0          # 程序正常退出
    assert result.stdout.strip() == "3"    # 屏幕上打印的是 3


def test_cli_10_plus_20():
    result = run_cli(10, 20)
    assert result.stdout.strip() == "30"
