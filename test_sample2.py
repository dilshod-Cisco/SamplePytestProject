import pytest


# @pytest.fixture(scope='module')
# def setup():
#     print("********** This is the fixture Only for 2nd module to run first **********")
#     yield setup
#     print("********** This is the TEARDOWN steps after each file **********")


def num_square2(num):
    print("Sample step function2 is running.")
    return num * num


def num_sum2(numbers: list):
    print("num_sum2 function is running.")
    return sum(numbers)


@pytest.mark.regression
def test_scenario12(my_cool_fixture):
    print("Running Scenario 1.")
    num = 8
    nums = [1, 5, 4]
    assert num_square2(num) == 64
    assert num_sum2(nums) == 10
    assert num_sum2(nums) > 5
    assert "llo" in "hello"
    assert not num_sum2(nums) > 10
    assert not "ELLO" in "hello", "Your message here in Case Assert returns False"
    # assert element.is_enabled(), "Element is disabled"


@pytest.mark.regression
def test_scenario22(my_cool_fixture):
    try:
        print("Running Scenario 22.")
        num = 10
        assert num_square2(num) == 100
    except AssertionError as err:
        print("Test Scenario test_scenario22 Failed.")
        pytest.fail("Scenario 22 FAILED!!")


# @pytest.mark.skip
@pytest.mark.smoke
def test_scenario32(my_cool_fixture):
    try:
        print("Running Scenario 32.")
        num = 5
        assert num_square2(num) >= 24
    except AssertionError as err:
        print("Test Scenario test_scenario3 Failed.")
        pytest.fail("Scenario 32 FAILED!!")
