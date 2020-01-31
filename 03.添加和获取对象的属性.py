# 在类的外面使用的是对象名
# 在类的方法里面，用的是self
# 对象名和self就是同一个东西

#定义一个苹果类，颜色：红色，大小：大
class fruit():
    def eat(self):
        print("吃完啦")
apple = fruit()
apple.eat()

# 先要有对象，才可以给对象添加属性
apple.color = "red"
apple.size = "big"
# 获取对象身上的属性
print(apple.color, apple.size)

# 如何查看同一个类创建的多个对象是否是一个对象
# <__main__.fruit object at 0x10adb5d00>---16进制
# 保存到内存中，需要开辟内存空间，底层是2进制
print(apple)
print(id(apple))