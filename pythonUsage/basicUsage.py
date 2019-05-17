#!/usr/bin/python3


#python3 中类的使用
class Foo:
    def bar(self):  # self 是特殊参数（必填）
        print('Bar1')

    def hello(self, name):
        print('I am ', name)

obj = Foo()  #根据Foo创建对象obj
obj.bar()
obj.hello('benlinhuo');


#python中数组遍历的方式
nums = [1, 2, 56, 12, 90];
#方式一
for index, num in enumerate(nums):
    print(index, num);

for idx in range(0, len(nums)):
    print(idx, nums[idx])

