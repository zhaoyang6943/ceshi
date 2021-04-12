import decimal


# 对结果处理去除多余的0
# def remove_exponent(num):
#     return num.to_integral() if num == num.to_integral() else num.normalize()


# 计算器-功能(俺的计算器只能计算10位数字之内的加减乘除！)
class Calculator:

    # 相加
    def add(self, a, b):
        # decimal.getcontext().prec = 10  # 10位限制
        # c = decimal.Decimal(a)+decimal.Decimal(b)
        # d = remove_exponent(c)

        return a + b

    # 相除
    def div(self, a, b):
        # print(type(a/b))
        try:
            return a / b
        except ZeroDivisionError:
            return "0 cannot be divided"


if __name__ == '__main__':
    # print(Calculator().add(1.11111, 2.00000000))
    # print(Calculator().add(-0.11111, -2.00000000))
    # print(Calculator().add(1, 4))
    # print(Calculator().add(10, 4000000))
    # print(Calculator().add(0.01, 0.09))

    print(Calculator().div(0.00000000001, 0.00000000009))
    print(Calculator().div(0.00000000001, 0.00000000009))
    print(Calculator().div(-10, 99))
    print(Calculator().div(-9, -99999))
    print(Calculator().div(-0.9, -0.1))
    print(Calculator().div(-0.0009, -0.0001))
