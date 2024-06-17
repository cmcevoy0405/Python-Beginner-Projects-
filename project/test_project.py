from project import deposit, bet_number, get_bet

def main():
    test_deposit()
    test_get_bet()
    test_bet_number()



def test_deposit():
    inputs = ["10", "20", "50"]
    expected_balance = sum(map(int, inputs))

    def mock_input(prompt):
        return inputs.pop(0) if inputs else "0"


    assert deposit(mock_input) == expected_balance

def test_bet_number():
    inputs = ["2", "4", "abc"]
    expected_outputs = [2, 3, 1]

    def mock_input(prompt):
        return inputs.pop(0)

    for expected_output in expected_outputs:
        assert bet_number(mock_input) == expected_output

def test_get_bet():
    inputs = ["10", "200", "50", "abc", "30"]
    expected_outputs = [{1: 10, 2: 10}, {1: 50, 2: 50, 3: 50}, {1: 30, 2: 30}]

    def mock_input(prompt):
        return inputs.pop(0)

    for expected_output in expected_outputs:
        assert get_bet(3, mock_input) == expected_output

if __name__ == "__main__":
    main()

