def calculate_portfolio_return(holdings: list[dict]) -> float:
    total_return = 0.0
    for item in holdings:
        weight = float(item.get("current_weight", 0))
        item_return = float(item.get("return", 0))
        total_return += weight * item_return
    return total_return


def compare_with_benchmark(portfolio_return: float, benchmark_return: float) -> dict:
    return {
        "portfolio_return": portfolio_return,
        "benchmark_return": benchmark_return,
        "excess_return": portfolio_return - benchmark_return,
    }


def classify_decision(process_score: int, outcome_score: int) -> str:
    if process_score >= 18 and outcome_score >= 9:
        return "good_process_good_outcome"
    if process_score >= 18 and outcome_score < 9:
        return "good_process_bad_outcome"
    if process_score < 18 and outcome_score >= 9:
        return "bad_process_good_outcome"
    return "bad_process_bad_outcome"
