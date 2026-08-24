import enum

from src import primitives
from itertools import permutations

PRIMITIVES = {
    "reverse": primitives.reverse,
    "shift_right": primitives.shift_right,
    "shift_left": primitives.shift_left,
    "rotate_right": primitives.rotate_right,
    "rotate_left": primitives.rotate_left,
    "swap_first_last": primitives.swap_first_last,
    "prepend_zero": primitives.prepend_zero,
    "append_zero": primitives.append_zero,
    "pop_right": primitives.pop_right,
    "pop_left": primitives.pop_left,
    "multiply_2": primitives.multiply_2,
    "multiply_3": primitives.multiply_3,
    "add_1": primitives.add_1,
    "add_2": primitives.add_2,
    "add_3": primitives.add_3,
    "mod_2": primitives.mod_2,
    "mod_3": primitives.mod_3,
    "sort_ascending": primitives.sort_ascending,
    "sort_descending": primitives.sort_descending,
    "subtract_next": primitives.subtract_next,
    # "pairwise_sum": primitives.pairwise_sum,
    "adjacent_sum": primitives.adjacent_sum,
    "mirror": primitives.mirror,
    "take_even_positions": primitives.take_even_positions,
    "take_odd_positions": primitives.take_odd_positions,
}


primitive_names = list(PRIMITIVES.keys())


rules = []

for name in primitive_names:
    rules.append([name])

for rule in permutations(primitive_names, 2):
    rules.append(list(rule))


def apply_rule(arr, rule):
    result = arr

    for primitive_name in rule:
        func = PRIMITIVES[primitive_name]
        result = func(result)

    return result


def gen_trace(tasks):
    traces = []

    for task in tasks:
        task_trace = []

        for rule in rules:
            trace_parts = [f"Candidate rule: {rule}"]

            accepted = True

            for i, example in enumerate(task.examples):
                result = apply_rule(example.input_array, rule)
                match = result == example.output_array

                trace_parts.append(f"""
Example {i + 1}:
Input: {example.input_array}
Result: {result}
Expected: {example.output_array}
Match: {match}
    """)

                if not match:
                    trace_parts.append(
                        "The candidate rule is rejected because the result does not match the expected output."
                    )
                    accepted = False
                    break

            if accepted:
                trace_parts.append(
                    "The candidate rule is consistent with all examples."
                )

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


def gen_trace_all_rules(tasks):
    traces = []

    for task in tasks:
        task_trace = []
        remaining_rules = rules.copy()

        for example_idx, example in enumerate(task.examples):
            trace_parts = [f"Example {example_idx}: {example.input_array}"]

            for rule in remaining_rules.copy():
                result = apply_rule(example.input_array, rule)
                trace_parts.append(f"{rule}: {result}")

                if result != example.output_array:
                    remaining_rules.remove(rule)

            trace_parts.append(str(remaining_rules))
            task_trace.append(trace_parts)

        traces.append(task_trace)

    return traces
