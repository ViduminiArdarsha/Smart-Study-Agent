from datetime import datetime, timedelta

def create_study_plan(topics, exam_date):
    today = datetime.today()
    exam = datetime.strptime(exam_date, "%Y-%m-%d")

    total_days = (exam - today).days
    topics_per_day = max(1, len(topics) // total_days)

    plan = {}
    topic_index = 0

    for day in range(total_days):
        date = (today + timedelta(days=day)).strftime("%Y-%m-%d")

        daily_topics = topics[topic_index: topic_index + topics_per_day]
        topic_index += topics_per_day

        plan[date] = {
            "study": daily_topics,
            "revision": []
        }

        if topic_index >= len(topics):
            break

    return plan