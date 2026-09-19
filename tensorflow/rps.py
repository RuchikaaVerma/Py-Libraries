def player(prev_play, opponent_history=[], history_counts={}):
    """
    A Rock-Paper-Scissors player that uses pattern recognition to predict
    the opponent's next move and counter it.

    Strategy:
    - Track opponent's move history
    - Look for repeated sequences of length 1, 2, 3, 4, and 5
    - Choose the counter to the most frequently occurring next move
      given the recent history pattern
    - Fall back to countering the opponent's most common move overall
    """

    # Map each move to what beats it
    beats = {"R": "P", "P": "S", "S": "R"}

    # Reset state on a new match (prev_play is empty string for game 1)
    if not prev_play:
        opponent_history.clear()
        history_counts.clear()

    else:
        opponent_history.append(prev_play)

        # Update n-gram counts for lengths 1..5
        for n in range(1, 6):
            if len(opponent_history) >= n:
                key = tuple(opponent_history[-n:])
                history_counts[key] = history_counts.get(key, 0) + 1

    # Need at least a few moves before pattern matching is useful
    if len(opponent_history) < 5:
        return "R"

    # Try to find a strong pattern match, from longest to shortest
    best_prediction = None
    best_count = 0

    for n in range(5, 0, -1):
        if len(opponent_history) < n:
            continue

        recent = tuple(opponent_history[-n:])

        # Look at all recorded sequences of length n+1 that START with 'recent'
        candidates = {}
        for seq, count in history_counts.items():
            if len(seq) == n + 1 and seq[:n] == recent:
                next_move = seq[-1]
                candidates[next_move] = candidates.get(next_move, 0) + count

        if candidates:
            predicted = max(candidates, key=candidates.get)
            total = sum(candidates.values())
            if candidates[predicted] > best_count:
                best_count = candidates[predicted]
                best_prediction = predicted

    if best_prediction:
        return beats[best_prediction]

    # Fallback: counter the opponent's overall most common move
    counts = {"R": 0, "P": 0, "S": 0}
    for m in opponent_history:
        counts[m] += 1
    most_common = max(counts, key=counts.get)
    return beats[most_common]