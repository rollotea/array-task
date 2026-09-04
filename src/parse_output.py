import re
import ast


def parse_output(raw_output):
    result = {
        "rules": [],
        "states": [],
        "final_answer": None,
        "format_valid": True,
    }

    # <think> ... </think> の中だけを取得
    think_match = re.search(r"<think>(.*?)</think>", raw_output, re.DOTALL)

    if think_match is None:
        result["format_valid"] = False
        return result

    think = think_match.group(1)

    # Stepごとの step番号、rule、state を取得
    step_pattern = re.compile(r"Step\s+(\d+)\s+\(([^)]+)\):\s*(\[[^\n]+\])")

    for match in step_pattern.finditer(think):

        step = int(match.group(1))
        rule = match.group(2).strip()
        state_str = match.group(3)
        print(step)

        try:
            state = ast.literal_eval(state_str)
        except (ValueError, SyntaxError):
            result["format_valid"] = False
            continue

        result["rules"].append({"step": step, "rule": rule})

        result["states"].append(state)

    # Final Answerを取得
    answer_match = re.search(r"Final Answer:\s*(\[[^\n]+\])", think)

    if answer_match:
        try:
            result["final_answer"] = ast.literal_eval(answer_match.group(1))
        except (ValueError, SyntaxError):
            result["format_valid"] = False
    else:
        result["format_valid"] = False

    return result
