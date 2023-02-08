from decimal import Decimal


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
    ret = int(val * bias)
    amount = ret % 10
    if (ret >= 0 and amount >= 5) or (ret < 0 and amount > 5):
        ret += 10 - amount
    else:
        ret -= amount
    return ret / bias
