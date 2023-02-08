from decimal import Decimal
import pytest
from .. import my_round


class Test_MyRound:
    @pytest.mark.parametrize(
        "val, dig, res",
        [
            ("0.4", 0, 0.0),
            ("0.5", 0, 1.0),
            ("0.6", 0, 1.0),
            ("0.5", 1, 0.5),
            ("0.44", 1, 0.4),
            ("0.45", 1, 0.5),
            ("0.54", 1, 0.5),
            ("0.55", 1, 0.6),
            ("0", 0, 0),
        ],
    )
    def test_Positive(self, val, dig, res):
        assert my_round.MyRound(Decimal(val), dig) == res

    @pytest.mark.parametrize(
        "val, dig, res",
        [
            ("-0.4", 0, 0.0),
            ("-0.5", 0, -1.0),
            ("-0.6", 0, -1.0),
            ("-0.5", 1, -0.5),
            ("-0.44", 1, -0.4),
            ("-0.45", 1, -0.5),
            ("-0.54", 1, -0.5),
            ("-0.55", 1, -0.6),
            ("-0", 0, 0),
        ],
    )
    def test_Negative(self, val, dig, res):
        assert my_round.MyRound(Decimal(val), dig) == res

    def test_RaiseTypeError_TakesDigitIsNegative(self):
        with pytest.raises(TypeError):
            my_round.MyRound(0.5, -1)
