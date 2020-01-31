class Master(object):
    def __init__(self):
        self.peifang = "古法配方"

    def make(self):
        print("按照%s制作" % self.peifang)

class School(object):
    def __init__(self):
        self.speifang = "新的配方"

    def make(self):
        print("按照%s制作" % self.speifang)

class Student(Master,School):
    # 子类继承父类，子类重写父类的方法
    # 重写：子类继承父类，做自己特有的事
    def __init__(self):
        self.peifang = "我自己的配方"
    def make(self):
        print("按照%s制作" % self.peifang)

# 如果子类的方法名和父类的相同（子类已重写父类方法），默认使用子类方法
# 子类和父类有同名属性，则默认使用子类的
damao = Student()
print(damao.peifang)
damao.make()