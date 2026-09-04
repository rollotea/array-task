import re
import ast

# def parse_output(raw_output):
#     result = {
#         "rules": [],
#         "states": [],
#         "rule_and_state": [],
#         "final_answer": None,
#         "format_valid": True,
#     }

#     # <think> ... </think> の中だけを取得
#     think_match = re.search(r"<think>(.*?)</think>", raw_output, re.DOTALL)

#     if think_match is None:
#         result["format_valid"] = False
#         return result

#     think = think_match.group(1)

#     # Stepごとの step番号、rule、state を取得
#     step_pattern = re.compile(r"Step\s+(\d+)\s+\(([^)]+)\):\s*(\[[^\n]+\])")

#     for match in step_pattern.finditer(think):

#         step = int(match.group(1))
#         rule = match.group(2).strip()
#         state_str = match.group(3)

#         try:
#             state = ast.literal_eval(state_str)
#         except (ValueError, SyntaxError):
#             result["format_valid"] = False
#             continue

#         result["rules"].append({"step": step, "rule": rule})

#         result["states"].append(state)

#     # Final Answerを取得
#     answer_match = re.search(r"Final Answer:\s*(\[[^\n]+\])", think)

#     if answer_match:
#         try:
#             result["final_answer"] = ast.literal_eval(answer_match.group(1))
#         except (ValueError, SyntaxError):
#             result["format_valid"] = False
#     else:
#         result["format_valid"] = False

#     return result


def parse_output(raw_output):
    result = {
        "examples": [],
        "query": None,
        "final_answer": None,
        "format_valid": True,
    }

    think_match = re.search(r"<think>(.*?)</think>", raw_output, re.DOTALL)

    if not think_match:
        result["format_valid"] = False
        return result

    think = think_match.group(1)

    # Example 1 ～ Example 5 をそれぞれ1ブロックとして取得
    example_pattern = r"(Example\s+\d+:.*?)(?=Example\s+\d+:|Query\s*:|$)"
    example_blocks = re.findall(example_pattern, think, re.DOTALL)

    for block in example_blocks:
        # Example番号
        example_match = re.search(r"Example\s+(\d+):", block)
        example_id = int(example_match.group(1))

        # Input
        input_match = re.search(r"Input:\s*(\[.*?\])", block, re.DOTALL)

        # Output
        output_match = re.search(r"Output:\s*(\[.*?\])", block, re.DOTALL)

        # Step
        steps = re.findall(r"Step\s+\d+\s+\((.*?)\):\s*(\[.*?\])", block, re.DOTALL)

        result["examples"].append(
            {
                "id": example_id,
                "input": input_match.group(1) if input_match else None,
                "steps": [{"rule": rule, "state": state} for rule, state in steps],
                "output": output_match.group(1) if output_match else None,
            }
        )

    # Queryブロック
    query_match = re.search(r"Query\s*:\s*(.*?)(?=</think>|$)", think, re.DOTALL)

    if query_match:
        query = query_match.group(1)

        input_match = re.search(r"Input:\s*(\[.*?\])", query, re.DOTALL)

        steps = re.findall(r"Step\s+\d+\s+\((.*?)\):\s*(\[.*?\])", query, re.DOTALL)

        final_match = re.search(r"Final Answer:\s*(\[.*?\])", query, re.DOTALL)

        result["query"] = {
            "input": input_match.group(1) if input_match else None,
            "steps": [{"rule": rule, "state": state} for rule, state in steps],
        }

        result["final_answer"] = final_match.group(1) if final_match else None

    return result
