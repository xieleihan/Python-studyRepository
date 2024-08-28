"""
    异常返回值
"""

def exception_return():
    try:
        # raise Exception('抛出异常')
        return 1
    except Exception as e:
        return 2
    finally:
        return 3
print(exception_return())