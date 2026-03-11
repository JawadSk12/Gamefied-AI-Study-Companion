# Points configuration

POINTS = {
    "ask_question": 5,
    "correct_answer": 10,
    "finish_quiz": 20
}


def add_points(current_points, action):

    if action in POINTS:
        current_points += POINTS[action]

    return current_points


def get_level(points):

    if points < 50:
        return "Beginner"

    elif points < 150:
        return "Intermediate"

    else:
        return "Advanced"


def get_badges(points):

    badges = []

    if points >= 50:
        badges.append("⭐ Learner")

    if points >= 150:
        badges.append("🏆 Quiz Master")

    if points >= 300:
        badges.append("🔥 AI Scholar")

    return badges