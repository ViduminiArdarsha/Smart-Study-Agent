class StudyMemory:
    def __init__(self):
        self.topics = []
        self.completed = []
        self.schedule = {}
        self.revision_log = {}

    def add_topics(self, topics):
        self.topics = topics

    def mark_completed(self, topic):
        if topic not in self.completed:
            self.completed.append(topic)

    def get_remaining(self):
        return [t for t in self.topics if t not in self.completed]