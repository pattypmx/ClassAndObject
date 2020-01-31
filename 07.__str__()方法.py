# 定义一个犬类，3个对象名为柯基1，2，3，属性：名字小短腿，年龄2
class Dog(object):
    # 定义相同属性
    def __init__(self, name, age, color="white"):
        # 添加属性
      self.name = name
      self.age = age
      self.color = color

    # def info(self):
    #     print("姓名:%s" % self.name)
    #     print("年龄: %s" % self.age)
    #     print("年龄: %s" % self.color)
    #     print("*" * 10)
    
    # 使用父类已有的魔法方法
    # 不可以添加形参
    # 会返回一个字符串
    # 追踪对象属性信息变化
    def __str__(self):
        return "姓名：%s 年龄：%d 颜色：%s" % (self.name, self.age, self.color)

    """
               这个方法是一个魔法方法 (Magic Method) ，用来显示信息
               该方法需要 return 一个数据，并且只有self一个参数，当在类的外部 print(对象) 则打印这个数据
           """
keji1 = Dog(name="柯基", age=1, color="yellow")
# 默认情况下，打印的是对象的16进制地址
# 在类中实现了__str__方法，如果打印对象名，会输出__str__方法中的返回值
print(keji1)


