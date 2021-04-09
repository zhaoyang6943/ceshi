
# 计算器-功能
class Calculator:

    # 相加
    def add(self,a,b):
        return a+b

    # 相除
    def div(self,a,b):
        return a/b

if __name__ == '__main__':

    print(Calculator().add(1.11111, 2.00000000))
    print(Calculator().add(-0.11111, -2.00000000))