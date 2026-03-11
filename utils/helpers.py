import json
import re


def clean_llm_text(text):
    """
    Cleans LLM response formatting
    """

    if not text:
        return ""

    text = text.strip()
    text = text.replace("\n\n", "\n")

    return text


def parse_json_response(response_text):
    """
    Extract JSON from LLM responses
    """

    try:
        return json.loads(response_text)

    except:

        match = re.search(r"\[.*\]", response_text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except:
                return []

        return []


def format_study_plan(plan_text):
    """
    Convert study plan into list format
    """

    if not plan_text:
        return []

    lines = plan_text.split("Day ")

    result = []

    for line in lines:
        line = line.strip()

        if line:
            result.append("Day " + line)

    return result


def calculate_accuracy(score, total):

    if total == 0:
        return 0

    return round((score / total) * 100, 2)


def calculate_progress(points, max_points=200):

    progress = points / max_points

    if progress > 1:
        progress = 1

    return progress