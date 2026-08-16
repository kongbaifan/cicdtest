# test_math_utils.py
# 这是"测试代码"：检查 math_utils.py 里的函数算得对不对
# 文件名以 test_ 开头，pytest 会自动发现它


from math_utils import add


def test_add_normal():
    """正常情况：1 + 2 应该等于 3"""
    assert add(1, 2) == 3


def test_add_negative():
    """边界情况：-1 + 1 应该等于 0"""
    assert add(-1, 1) == 0
