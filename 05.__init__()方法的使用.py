# 定义一个犬类，3个对象名为柯基1，2，3，属性：名字小短腿，年龄2
class Dog(object):
    # 在python中，__开头__结尾的方法，称之为魔法方法
    # 魔法方法是python下的object提供的
    # 在特殊情况下被python执行（python可以监听到使用自己的类创建一个对象）
    # 在自定义类中实现（重写）魔法方法
    # 在走进init方法时，对象已经被创建
    # 定义相同属性
    def __init__(self):
        # 添加属性
      self.name = "小短腿"
      self.age = "2"

    def run(self):  # self==调用这个对象方法的对象---keji==self
        print("腿短，但是跑的块")
    def info(self):
        print("姓名:%s" % self.name)
        print("年龄: %s" % self.age)
        print("*" * 10)
keji1 = Dog()
keji1.run()
# 获取对象属性
# 使用对象名调用对象方法
keji1.info()
keji2 = Dog()
keji2.run()
keji2.info()

keji3 = Dog()
keji3.run()
keji3.info()



