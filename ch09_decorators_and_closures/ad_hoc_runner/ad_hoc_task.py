from dataclasses import dataclass
from typing import Callable
from dateutil.parser import parse as parse_date
from datetime import datetime


@dataclass(frozen=True)
class AdHocTask:
    name: str
    job: Callable
    obsolete_date: str

    def __post_init__(self):
        self.__validate_obsolete_date()

    def __validate_obsolete_date(self):
        parse_date(self.obsolete_date)

    def __call__(self):
        if not self.is_active:
            raise ValueError(f'Obsolete task will not run. {self}')
        self.job()

    def __repr__(self):
        cls = type(self).__name__
        dt = parse_date(self.obsolete_date)
        return f'<{cls}> {self.name} | {self.job.__name__} | obsolete after {dt:%Y-%m-%d}'

    @property
    def is_active(self):
        return parse_date(self.obsolete_date).date() >= datetime.now().date()
