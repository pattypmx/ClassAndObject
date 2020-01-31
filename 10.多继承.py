class Master(object):
    def __init__(self):
        self.peifang = "古法配方"

    def make(self):
        print("按照%s制作" % self.peifang)

    def Lei1(self):
        print("Master类")

shifu = Master()

class School(object):
    def __init__(self):
        self.speifang = "新的配方"
    def make(self):
        print("按照%s制作" % self.speifang)

    def Lei2(self):
        print("School类")
school = School()

# 多继承，继承了多个父类
class Student(Master,School):   # 多个父类且方法名相同，会先执行第一个；如果要执行School类，可以把School父类写在前面
    pass
damao= Student()
print(damao.peifang)
# 如果两个父类的方法名相同，子类会执行第一个父类的"方法"和"属性"
damao.make()
# 如果两个父类的方法名不相同，子类会分别执行
damao.Lei1()
damao.Lei2()