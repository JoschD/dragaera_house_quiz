
# Questions data structure
import json
from pathlib import Path

from questions import get_answers
from cycle import TheCycle


DESCRIPTIONS = json.loads(Path('./houses.json').read_text())
COLOR_THEMES = json.loads(Path('./house_colors.json').read_text())

def calculate_results(answers: dict[str, int], weights: dict[str, int]) -> TheCycle:
    """Calculate house affinities and display results"""
    print("Calculating results... 🧮")
    print(f"User answers: {answers}")
    print(f"User weights: {weights}")
    results = {}
    house_answers: TheCycle = get_answers()

    for house_name, house_scores in house_answers.items():
        total_score = 0
        max_possible = 0
        min_possible = 0

        for question, answer in answers.items():
            house_score_for_that_choice = house_scores[question][answer]
            weight = weights[question]

            total_score += house_score_for_that_choice * weight

            # Calculate best and worst possible scores for this question
            max_possible += max(house_scores[question]) * weight
            min_possible += min(house_scores[question]) * weight

        # # Map [min_possible, max_possible] to [0, 100]
        # if max_possible == min_possible:
        #     # Edge case: house is neutral on everything
        #     percentage = 50.0
        # else:
        #     percentage = ((total_score - min_possible) / (max_possible - min_possible)) * 100
        percentage = (total_score / max_possible) * 100
        if percentage < 0:
            percentage = 0

        results[house_name] = percentage

    return TheCycle(**results)