# 定义一个犬类，3个对象名为柯基1，2，3，属性：名字小短腿，年龄2
class Dog(object):
    # 定义相同属性
    def __init__(self, name, age, color="white"):
        # 添加属性
      self.name = name
      self.age = age
      self.color = color

    def run(self):  # self==调用这个对象方法的对象---keji==self
        print("腿短，但是跑的块")
    def info(self):
        print("姓名:%s" % self.name)
        print("年龄: %s" % self.age)
        print("年龄: %s" % self.color)
        print("*" * 10)

keji1 = Dog(name="柯基", age="1", color="yellow")
# 获取对象属性
# 使用对象名调用对象方法
keji1.info()

keji2 = Dog(name="哈士奇", age="2")
keji2.info()

keji3 = Dog(name="博美", age="3")
keji3.info()



