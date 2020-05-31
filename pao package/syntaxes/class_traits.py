#! class Traits

class Trait:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def __get__(self, instance, owner):
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if self.minimum < value < self.maximum:
            instance.__dict__[self.key] = value
        else:
            raise ValueError("value not in range")

    def __set_name__(self, owner, name):
        self.key = name


class MyMeta(type):
    def __new__(cls, name, bases, namespace, otherarg):
        return super().__new__(cls, name, bases, namespace)

class MyClass(metaclass=MyMeta, otherarg=1):
    pass



# types.new_class("MyClass", (), dict(metaclass=MyMeta, otherarg=1))
# types.prepare_class("MyClass", (), dict(metaclass=MyMeta, otherarg=1))



class NewType(type):
    ''' create new type for our 
    mustacheLike language '''

    def __new__(cls, *args, **kwargs):
        if len(args) != 3:
            return super().__new__(cls, *args)
        name, bases, ns = args
        init = ns.get('__init_subclass__')
        if isinstance(init, types.FunctionType):
            ns['__init_subclass__'] = classmethod(init)
        self = super().__new__(cls, name, bases, ns)
        for k, v in self.__dict__.items():
            func = getattr(v, '__set_name__', None)
            if func is not None:
                func(self, k)
        super(self, self).__init_subclass__(**kwargs)
        return self

    def __init__(self, name, bases, ns, **kwargs):
        super().__init__(name, bases, ns)

class NewObject(object):
    @classmethod
    def __init_subclass__(cls):
        pass