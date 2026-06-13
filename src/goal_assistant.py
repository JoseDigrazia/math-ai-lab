def suggest_tactic(goal, hypotheses):
    if " = " in goal:
        for h in hypotheses:
            if "=" in h:
                return "rw [h]"

    return "No suggestion"


goal = "a + c = b + c"

hypotheses = [
    "a = b"
]

print("Goal:", goal)
print("Suggestion:", suggest_tactic(goal, hypotheses))