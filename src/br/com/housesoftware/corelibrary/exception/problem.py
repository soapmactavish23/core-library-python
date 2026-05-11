from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List


@dataclass
class ProblemObject:
    name: str
    user_message: str


@dataclass
class Problem:
    status: int
    detail: str
    user_message: str

    type: Optional[str] = None
    title: Optional[str] = None

    timestamp: datetime = field(default_factory=datetime.utcnow)

    objects: Optional[List[ProblemObject]] = None

    def to_dict(self):
        data = {
            "status": self.status,
            "type": self.type,
            "title": self.title,
            "detail": self.detail,
            "userMessage": self.user_message,
            "timestamp": self.timestamp.isoformat(),
        }

        if self.objects:
            data["objects"] = [
                {
                    "name": obj.name,
                    "userMessage": obj.user_message
                }
                for obj in self.objects
            ]

        return {k: v for k, v in data.items() if v is not None}