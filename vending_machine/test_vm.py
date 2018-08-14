from vm import *


def test_insert_coin_and_check():
    assert "잔액은 0원입니다" == run("잔액")
    assert "100원을 넣었습니다" == run("동전 100")
    assert "잔액은 100원입니다" == run("잔액")
    assert "100원을 넣었습니다" == run("동전 100")
    assert "잔액은 200원입니다" == run("잔액")
