import enum as enum

class ExpressionMeasure(str, enum.Enum):
    mean = "mean"
    median = "median"
    mad = "mad"
    std = "std"