import pytest
from pytest_mock import MockerFixture

import bank


@pytest.mark.parametrize('attempts, expected_queue_length', [
    (['7'], 7),
    (['10'], 10),
    (['-12', '5'], 5),
    (['-4', '-17', '1'], 1),
    (['1.5', '2'], 2),
    (['9.25', '22.5', 14], 14),
    (['hello', '8'], 8),
    (['hello', 'goodbye', '3'], 3),
    (['hello', '-6', 'goodbye', '6.25', '-5.5', '-1', '12'], 12),
])
def test_get_queue_length(mocker: MockerFixture, attempts: list[str], expected_queue_length: int) -> None:
    mocker.patch('builtins.input', side_effect=attempts)
    queue_length = bank.get_queue_length()
    assert queue_length == expected_queue_length, f"THe sequence of attempts {attempts} should result in queue length {expected_queue_length}"
