import ast
from dataclasses import dataclass
from pathlib import Path
import re
import json
import polars as pl


@dataclass
class ArrayPair:
    input_array: list[int]
    output_array: list[int]


@dataclass
class Trace:
    task_id: str
    trace: str


@dataclass
class ArrayTask:
    task_id: str
    examples: list[ArrayPair]
    test_case: ArrayPair
    trace: str | None = None


class ArrayTaskLoader:
    def load(self, path: Path) -> ArrayTask:
        with open(path, "r") as f:
            data = json.load(f)

        examples = [
            ArrayPair(
                input_array=example["input"][0], output_array=example["output"][0]
            )
            for example in data["train"]
        ]

        test_case = ArrayPair(
            input_array=data["test"][0]["input"][0],
            output_array=data["test"][0]["output"][0],
        )

        return ArrayTask(task_id=path.stem, examples=examples, test_case=test_case)


class TraceLoader:
    def load(self, path: Path) -> Trace:
        with open(path, "r") as f:
            data = json.load(f)

        return Trace(task_id=data["task_id"], trace=data["trace"])


class PromptBuilder:
    def __init__(self, cot: bool = False):
        self.cot = cot

    def build(self, task: ArrayTask) -> str:
        lines = []
        instruction = """
Infer the transformation rule from examples.
Output the final array.
        """
        # lines = [
        #     "You are given examples of transformations on colored grids.",
        #     "Infer the transformation rule and apply it to the query grid.\n",
        # ]
        lines.append(instruction)

        for i, ex in enumerate(task.examples, 1):
            lines.append(f"Example {i}\n")
            lines.append("Input:")
            lines.append(str(ex.input_array))
            lines.append("\nOutput:")
            lines.append(str(ex.output_array))
            lines.append("")

        lines.append("Query\n")
        lines.append("Input:")
        lines.append(str(task.test_case.input_array))
        lines.append("\nOutput:")

        return "\\n".join(lines)


def extract_answer(text):
    if text is None:
        return "NOT_FOUND"

    matches = re.findall(r"\[[^\[\]]*\]", text)
    arrays = []
    for match in matches:
        try:
            value = ast.literal_eval(match)

            if isinstance(value, list):
                arrays.append(value)

        except (ValueError, SyntaxError):
            pass

    if arrays == []:
        return "NOT_FOUND"

    return str(arrays[-1])
