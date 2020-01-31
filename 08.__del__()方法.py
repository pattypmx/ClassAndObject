class Hero(object):
    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name, age, hp):
        self.name = name
        self.age  = age
        self.hp = hp

    def __str__(self):
        return "姓名:%s 年龄:%d 血量:%d" %(self.name, self.age, self.hp)

    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("删除")

yase = Hero("亚瑟", 18, 500)
yase1 = yase
yase2 = yase
# 当使用del() 删除变量指向的对象时，则会减少对象的引用计数。如果对象的引用计数不为1，
# 那么会让这个对象的引用计数减1，当对象的引用计数为0的时候，则对象才会被真正删除
del yase
del yase1
del yase2
input("停在这边")
# del yase1
# del yase2