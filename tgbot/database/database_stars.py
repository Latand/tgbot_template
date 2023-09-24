import json
import random


def get_activities(activities_type: str) -> str:
    with open("database/stars/activities_stars.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)
    msg: str = text[activities_type]
    if msg:
        return msg
    else:
        return "В ближайшее время нет мероприятий"


def get_faq(question_number: int) -> str:
    with open("database/stars/faq.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)["answers"]
    answer: str = text[f"option_{question_number + 1}"]
    if answer:
        return answer
    else:
        return "Думаем над ответом"


def get_schedule(schedule_type: int) -> str:
    with open("database/stars/schedule_stars.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)
    if schedule_type == 1:
        response: str = text["monthly"]
    elif schedule_type == 0:
        response: str = text["weekly"]
    else:
        response: str = "Error occurred"
    if response:
        return response
    else:
        return "Загляни чуть позже"


def get_scholarship() -> str:
    with open("database/stars/scholarship.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)
    answer = text["answer"]
    if answer:
        return answer
    else:
        return random.choice(text["jokes"])


def write_feedback(text: str) -> bool:
    try:
        with open("database/feedbacks/stars_feedbacks.json", "r", encoding="utf-8") as f:
            old: list = json.load(f)
        old.append(text)
        with open("database/feedbacks/stars_feedbacks.json", "w", encoding="utf-8") as f:
            json.dump(old, f, indent=4, ensure_ascii=False)
        return True
    except:
        return False
