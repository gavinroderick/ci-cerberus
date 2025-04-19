from dataclasses import dataclass

from githubparsers.models.job import Job
from githubparsers.models.step import Step


@dataclass
class Workflow:
    id: str
    name: str
    jobs: list[Job]
