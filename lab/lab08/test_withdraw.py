# lab08_all.py
import pytest

# ------------------------------
# PHẦN CODE CHÍNH
# ------------------------------

def verify_pin(input_pin: str, correct_pin: str = "1234") -> bool:
    """Hàm kiểm tra mã PIN"""
    return input_pin == correct_pin


def withdraw(balance: int, amount: int) -> int:
    """Hàm rút tiền"""
    if amount <= 0:
        raise ValueError("Số tiền rút phải lớn hơn 0")
    if amount > balance:
        raise ValueError("Số dư không đủ để rút")
    return balance - amount


# ------------------------------
# PHẦN TEST PYTEST
# ------------------------------

def test_verify_pin_correct():
    assert verify_pin("1234") is True


def test_verify_pin_incorrect():
    assert verify_pin("0000") is False


def test_withdraw_success():
    assert withdraw(1000, 200) == 800


def test_withdraw_zero_amount():
    with pytest.raises(ValueError, match="Số tiền rút phải lớn hơn 0"):
        withdraw(1000, 0)


def test_withdraw_exceed_balance():
    with pytest.raises(ValueError, match="Số dư không đủ để rút"):
        withdraw(500, 600)


# Để có thể chạy trực tiếp: python lab08_all.py
if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
