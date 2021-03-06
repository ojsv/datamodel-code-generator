# generated by datamodel-codegen:
#   filename:  subclass_enum.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ProcessingStatus(Enum):
    COMPLETED = 'COMPLETED'
    PENDING = 'PENDING'
    FAILED = 'FAILED'


class ProcessingTask(BaseModel):
    processing_status: Optional[ProcessingStatus] = Field(
        'COMPLETED', title='Status of the task'
    )
