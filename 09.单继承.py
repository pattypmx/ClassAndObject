# 煎饼果子老师傅在煎饼果子界摸爬滚打几十年，拥有一身精湛的煎饼果子技术，并总结了一套"古法煎饼果子配方"。
# 可是老师傅年迈已久，希望把自己的配方传承下去，于是老师傅把配方传给他的徒弟大猫...
class Master(object):
    def __init__(self):
        self.peifang = "古法煎饼果子配方"

    def make(self):
        print("按照%s制作煎饼" % self.peifang)

shifu = Master()
# print(shifu.peifang)
# shifu.make()

# 定义Tudi类，继承了 Master，则Tudi是子类，Master是父类
class Tudi(Master):
    pass
# 子类可以继承父类所有的属性和方法，哪怕子类没有自己的属性和方法，也可以使用父类的属性和方法。
damao = Tudi()  # 创建子类实例对象
print(damao.peifang)    # 子类对象可以直接使用父类的属性
damao.make()
# 子类对象可以直接使用父类的属性

