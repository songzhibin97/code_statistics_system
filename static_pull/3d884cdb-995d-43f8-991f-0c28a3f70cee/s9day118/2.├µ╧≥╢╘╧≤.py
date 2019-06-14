# by luffycity.com

class Foo(object):

    def __getitem__(self, item):
        return 1

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

obj = Foo()
obj['k1']
obj['k1'] = 123
del obj['k1']