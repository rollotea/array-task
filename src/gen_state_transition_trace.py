import enum

from src.gen_trace import PRIMITIVES
from src import primitives
from itertools import permutations

# PRIMITIVES = {
#     "reverse": primitives.reverse,
#     "shift_right": primitives.shift_right,
#     "shift_left": primitives.shift_left,
#     "rotate_right": primitives.rotate_right,
#     "rotate_left": primitives.rotate_left,
#     "swap": primitives.swap,
#     "prepend_zeros": primitives.prepend_zeros,
#     "append_zeros": primitives.append_zeros,
#     "pop_right": primitives.pop_right,
#     "pop_left": primitives.pop_left,
#     "multiply_constant": primitives.multiply_constant,
#     "add_constant": primitives.add_constant,
#     "modulo": primitives.modulo,
#     "sort_ascending": primitives.sort_ascending,
#     "sort_descending": primitives.sort_descending,
#     "differences": primitives.differences,
#     "pairwise_sum": primitives.pairwise_sum,
#     "mirror": primitives.mirror,
#     "take_even_positions": primitives.take_even_positions,
#     "take_odd_positions": primitives.take_odd_positions,
# }


primitive_names = list(PRIMITIVES.keys())


rules = []

for name in primitive_names:
    rules.append([name])

for rule in permutations(primitive_names, 2):
    rules.append(list(rule))


# def apply_rule(arr, rule):
#     result = arr

#     for primitive_name in rule:
#         func = PRIMITIVES[primitive_name]
#         result = func(result)

#     return result


def apply_rule(arr, rule, return_trace=False):
    result = arr.copy()
    trace = []

    for primitive_name in rule:
        func = PRIMITIVES[primitive_name]
        next_result = func(result)

        if return_trace:
            trace.append(
                {
                    "operation": primitive_name,
                    "input": result.copy(),
                    "output": next_result.copy(),
                }
            )

        result = next_result

    if return_trace:
        return result, trace

    return result


def gen_state_transition_trace(tasks):
    traces = []

    for task in tasks:
        task_trace = []

        for rule in rules:
            # trace_parts = [f"Candidate rule: {rule}"]
            trace_parts = []

            accepted = True

            for i, example in enumerate(task.examples + [task.test_case]):
                result, trace = apply_rule(example.input_array, rule, True)
                match = result == example.output_array

                if i + 1 == len(task.examples + [task.test_case]):
                    trace_parts.append(f"""
Query :
Input: {example.input_array}""")
                    for x_idx, x in enumerate(trace):
                        trace_parts.append(
                            f"Step {x_idx + 1} ({x['operation']}): {x['output']}"
                        )
                    trace_parts.append(f"Final Answer: {result}")

                else:

                    trace_parts.append(f"""
Example {i + 1}:
Input: {example.input_array}""")
                    for x_idx, x in enumerate(trace):
                        trace_parts.append(
                            f"Step {x_idx + 1} ({x['operation']}): {x['output']}"
                        )

                    trace_parts.append(f"Output: {result}")

                if not match:
                    trace_parts.append(
                        "The candidate rule is rejected because the result does not match the expected output."
                    )
                    accepted = False
                    break

            # if accepted:
            #     trace_parts.append(
            #         "The candidate rule is consistent with all examples."
            #     )

            task_trace.append(
                {
                    "task_id": task.task_id,
                    "rule": rule,
                    "trace": "\n".join(trace_parts),
                    "accepted": accepted,
                }
            )

        traces.append(task_trace)

    return traces


# def gen_state_transition_trace(tasks):
#     traces = []

#     for task in tasks:
#         rule = task.rule
#         task_trace = []

#         trace_parts = [f"Rule: {rule}"]

#         for i, example in enumerate(task.examples):
#             result, state_trace = apply_rule(
#                 example.input_array, rule, return_trace=True
#             )

#             # データ生成側で正解性を確認
#             assert result == example.output_array

#             trace_parts.append(f"\nExample {i + 1}:")

#             trace_parts.append(f"Input: {example.input_array}")

#             for step_idx, step in enumerate(state_trace):
#                 trace_parts.append(
#                     f"Step {step_idx + 1} ({step['operation']}): " f"{step['output']}"
#                 )

#             trace_parts.append(f"Output: {result}")

#         task_trace.append(
#             {
#                 "task_id": task.task_id,
#                 "rule": rule,
#                 "trace": "\n".join(trace_parts),
#             }
#         )

#         traces.append(task_trace)

#     return traces
