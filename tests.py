from bull_and_cow_python.game import format_response, respond_to_guess


def test_response():
    guess = "1234"
    truth = "4271"
    expected = ("C", "B", ".", "C")
    got = respond_to_guess(guess, truth)
    assert got == expected


def test_format_response():
    response = ("C", "B", ".", "C")
    expected = "1 bull, 2 cows"
    got = format_response(response)
    assert got == expected
