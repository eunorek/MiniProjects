from vm import *

def test_inition_change_should_be_zero():
    Jim = VendingMachine()
    assert "잔돈은 0 원입니다" == Jim.run("호에에에에에에엑")

# def test_insert_coin_and_check():
#     assert "the change is: 0 won" == run("change")
#     assert "inserted 100 won" == run("coin 100")
#     assert "the change is: 100 won" == run("change")
#     assert "inserted 100 won" == run("coin 100")
#     assert "the change is: 200 won" == run("잔액")
