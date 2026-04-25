def detect_rule_update_need(review: dict) -> dict:
    """Detect whether a rule update proposal should be drafted.

    This function does not modify active rules. It only returns signals that
    Meta Analyst can convert into a rule change proposal.
    """
    signals = []

    if review.get("rule_violation_count", 0) >= 2:
        signals.append("repeated_rule_violation")

    if review.get("scenario_failure_count", 0) >= 2:
        signals.append("scenario_failure_repeated")

    if review.get("bad_process_good_outcome_count", 0) >= 2:
        signals.append("lucky_success_detected")

    if review.get("good_process_bad_outcome_count", 0) >= 2:
        signals.append("environment_changed_or_rule_too_strict")

    return {
        "rule_update_needed": len(signals) > 0,
        "signals": signals,
    }
