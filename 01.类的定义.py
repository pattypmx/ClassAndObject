# 自定义类：苹果---水果类
# class： 表示这个类
# 01
class Fruit:
    pass    # 占位

# 02
class Fruit():
    pass

#03
# info 是一个实例方法，第一个参数一般是self，表示实例对象本身，
# 当然了可以将self换为其它的名字，其作用是一个变量 这个变量指向了实例对象
class Fruit(object):
    def est(self):
        print("多吃水果")


# 三种创建方式都是在python2.x的基础上产生的
# 03是后期3.x产生的
# 01 02叫做经典类，他们都是没有父类（基类）的
# 03叫做新式类
# object是所有类的父类

# 在python3中，无论那种类都是继承object
# 在python2.x中，01 02相同没有父类，03是有父类的
# 类名 的命名规则按照"大驼峰命名法"