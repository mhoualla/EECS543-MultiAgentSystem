def analyze_decisions(decisions):
    vote_counts = {}
    for decision in decisions.values():
        for candidate in ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']:
            if candidate in decision:
                vote_counts[candidate] = vote_counts.get(candidate, 0) + 1
    return vote_counts
