from src.performance_tracker import (
    calculate_portfolio_return,
    classify_decision,
    compare_with_benchmark,
)


def test_calculate_portfolio_return():
    holdings = [
        {"current_weight": 0.5, "return": 0.1},
        {"current_weight": 0.5, "return": -0.02},
    ]
    assert calculate_portfolio_return(holdings) == 0.04


def test_compare_with_benchmark():
    result = compare_with_benchmark(0.08, 0.05)
    assert result["excess_return"] == 0.03


def test_classify_decision():
    assert classify_decision(20, 10) == "good_process_good_outcome"
    assert classify_decision(20, 5) == "good_process_bad_outcome"
    assert classify_decision(10, 10) == "bad_process_good_outcome"
    assert classify_decision(10, 5) == "bad_process_bad_outcome"
