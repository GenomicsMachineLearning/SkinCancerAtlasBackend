import enum as enum

class ExpressionMeasure(str, enum.Enum):
    total = "total"
    non_zero_mean = "non_zero_mean"
    mean = "mean"
    median = "median"
    mad = "mad"
    std = "std"