# calculator.py
# 命令行加法计算器
# 用法：python calculator.py 1 2
# 输出：3
#
# argparse 是 Python 自带的库，专门用来处理"命令行参数"，
# 不需要 pip install 任何东西。


import argparse

from math_utils import add


def main():
    # 1. 创建一个参数解析器
    parser = argparse.ArgumentParser(description="一个简单的加法计算器")

    # 2. 定义两个必填参数 a 和 b（type=int 表示把它们当成整数读入）
    parser.add_argument("a", type=int, help="第一个数")
    parser.add_argument("b", type=int, help="第二个数")

    # 3. 真正去读命令行传进来的参数
    args = parser.parse_args()

    # 4. 调用 math_utils 里的 add 函数计算结果
    result = add(args.a, args.b)

    # 5. 把结果打印到屏幕上
    print(result)


# 只有"直接运行这个文件"时才执行 main()
# 这样别人 import calculator 时不会意外触发命令行
if __name__ == "__main__":
    main()
