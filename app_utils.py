
# Questions data structure
import json
from pathlib import Path

QUESTIONS = json.loads(Path('./questions.json').read_text())
HOUSE_ANSWERS = json.loads(Path('./answers.json').read_text())
DESCRIPTIONS = json.loads(Path('./houses.json').read_text())
COLOR_THEMES = json.loads(Path('./house_colors.json').read_text())

def calculate_results(answers, weights):
    """Calculate house affinities and display results"""
    print("Calculating results... 🧮")
    print(f"User answers: {answers}")
    print(f"User weights: {weights}")
    results = {}

    for house_name, house_scores in HOUSE_ANSWERS.items():
        total_score = 0
        max_possible = 0
        min_possible = 0

        for q_idx in range(len(QUESTIONS)):
            user_choice_idx = answers[q_idx]  # Which choice user picked (0, 1, or 2)
            house_score_for_that_choice = house_scores[q_idx][user_choice_idx]
            weight = weights[q_idx]

            total_score += house_score_for_that_choice * weight

            # Calculate best and worst possible scores for this question
            max_possible += max(house_scores[q_idx]) * weight
            min_possible += min(house_scores[q_idx]) * weight

        # Map [min_possible, max_possible] to [0, 100]
        if max_possible == min_possible:
            # Edge case: house is neutral on everything
            percentage = 50.0
        else:
            percentage = ((total_score - min_possible) / (max_possible - min_possible)) * 100

        results[house_name] = percentage

    return results