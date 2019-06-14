
def func():
    pass


class Foo(object):

    def func(self):
        pass

# 执行方式一
# obj = Foo()
# obj.func() # 方法

# 执行方式二
# Foo.func(123) # 函数

from types import FunctionType,MethodType

# obj = Foo()
# print(isinstance(obj.func,FunctionType)) # False
# print(isinstance(obj.func,MethodType))   # True


print(isinstance(Foo.func,FunctionType)) # True
print(isinstance(Foo.func,MethodType))   # False
