class Master(object):
    def make(self):
        print("古式制作方法")

class School(object):
    def make(self):
        print("现代制作方法")

class Student(Master,School):
    def make(self):
        print("我自己的制作方法")
    # 如果还需要调用父类的方法及属性
    # 使用父类名.对象方法名(self)
    def make_mater(self):
        Master.make(self)
    def make_school(self):
        School.make(self)

xuesheng = Student()
xuesheng.make()     # 调用子类的方法（默认重写了父类的同名方法）
xuesheng.make_school()  # 进入实例方法去调用父类School的方法
xuesheng.make_mater()   # 进入实例方法去调用父类Master的方法
