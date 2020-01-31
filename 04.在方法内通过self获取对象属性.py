# 定义一个犬类，对象名为柯基，属性：名字小短腿，年龄2
class Dog(object):
    def run(self):  # self==调用这个对象方法的对象---keji==self
        print("腿短，但是跑的块")
    def info(self):
        print(self.name, self.age)

keji = Dog()
keji.run()

# 添加属性
keji.name = "小短腿"
keji.age = "2"

# 获取对象属性
# print(keji.name, keji.age)
# 使用对象名调用对象方法
keji.info()

# 在类的外面，使用的是对像名.对象属性
# 在类的实例方法内部，使用的是self.对象属性

