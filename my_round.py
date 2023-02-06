from decimal import Decimal, getcontext


def MyRound(val: Decimal, digit: int) -> float:
    """四捨五入を行う

    Args:
        val (Decimal): 値
        digit (int): 桁位置(0を含む正の整数)

    Returns:
        float: 四捨五入後の値

    Example:
        MyRound(0.5, 0) -> 1.0\n
        MyRound(0.55, 1) -> 0.6

    Raises:
        digitに負の値を渡すとTypeErrorが送出される
    """

    if digit < 0:
        raise TypeError
    bias = 10 ** (digit + 1)
    ret = val * bias
    if (amount := ret % 10) >= 5:
        ret += 10 - amount
    else:
        ret -= amount
    return ret / bias


def main():
    getcontext().prec = 3  # 有効桁数の指定
    # print(0.81 + 0.04)  # 0.8500000000000001
    print(Decimal(0.81) + Decimal(0.04))  # 0.850
    print(MyRound(Decimal(0.81) + Decimal(0.04), 1))  # 0.9


if __name__ == "__main__":
    main()
