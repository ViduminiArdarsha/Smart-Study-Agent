
def parse_syllabus(text: str):
    topics = [line.strip() for line in text.split("\n") if line.strip()]
    return topics