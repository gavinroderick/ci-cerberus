from dataclasses import dataclass

from actionsparser.models.job import Job
from actionsparser.models.step import Step


@dataclass
class Workflow:
    id: str
    name: str
    jobs: list[Job]
