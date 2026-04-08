from typing import List
import re

def parse_syllabus(text: str) -> List[str]:
    """
    Simple parser: splits syllabus into topics
    """
    topics = re.split(r'\n|,|-', text)
    topics = [t.strip() for t in topics if t.strip()]
    return topics