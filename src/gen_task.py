import sys
from pathlib import Path
from src.gen_trace import PRIMITIVES
from src import primitives
import random
import os
import json

# sys.path.append(str(Path.cwd().parent))


RAW_RULES = [
    ["reverse"],
    ["shift_right"],
    ["shift_left"],
    ["rotate_right"],
    ["rotate_left"],
    ["swap_first_last"],
    ["prepend_zero"],
    ["append_zero"],
    ["pop_right"],
    ["pop_left"],
    ["multiply_2"],
    ["multiply_3"],
    ["add_1"],
    ["add_2"],
    ["add_3"],
    ["mod_2"],
    ["mod_3"],
    ["sort_ascending"],
    ["sort_descending"],
    ["subtract_next"],
    ["adjacent_sum"],
    ["mirror"],
    ["take_even_positions"],
    ["take_odd_positions"],
    ["reverse", "prepend_zero"],
    ["reverse", "append_zero"],
    ["reverse", "pop_right"],
    ["reverse", "pop_left"],
    ["reverse", "multiply_2"],
    ["reverse", "multiply_3"],
    ["reverse", "add_1"],
    ["reverse", "add_2"],
    ["reverse", "add_3"],
    ["reverse", "mod_2"],
    ["reverse", "mod_3"],
    ["reverse", "subtract_next"],
    ["reverse", "adjacent_sum"],
    ["reverse", "mirror"],
    ["reverse", "take_even_positions"],
    ["reverse", "take_odd_positions"],
    ["shift_right", "prepend_zero"],
    ["shift_right", "append_zero"],
    ["shift_right", "pop_right"],
    ["shift_right", "pop_left"],
    ["shift_right", "multiply_2"],
    ["shift_right", "multiply_3"],
    ["shift_right", "add_1"],
    ["shift_right", "add_2"],
    ["shift_right", "add_3"],
    ["shift_right", "mod_2"],
    ["shift_right", "mod_3"],
    ["shift_right", "subtract_next"],
    ["shift_right", "adjacent_sum"],
    ["shift_right", "mirror"],
    ["shift_right", "take_even_positions"],
    ["shift_right", "take_odd_positions"],
    ["shift_left", "prepend_zero"],
    ["shift_left", "append_zero"],
    ["shift_left", "pop_right"],
    ["shift_left", "pop_left"],
    ["shift_left", "multiply_2"],
    ["shift_left", "multiply_3"],
    ["shift_left", "add_1"],
    ["shift_left", "add_2"],
    ["shift_left", "add_3"],
    ["shift_left", "mod_2"],
    ["shift_left", "mod_3"],
    ["shift_left", "subtract_next"],
    ["shift_left", "adjacent_sum"],
    ["shift_left", "mirror"],
    ["shift_left", "take_even_positions"],
    ["shift_left", "take_odd_positions"],
]

RAW_OOD_RULES_V1 = [
    ["rotate_right", "prepend_zero"],
    ["rotate_right", "append_zero"],
    ["rotate_right", "pop_right"],
    ["rotate_right", "pop_left"],
    ["rotate_right", "multiply_2"],
    ["rotate_right", "multiply_3"],
    ["rotate_right", "add_1"],
    ["rotate_right", "add_2"],
    ["rotate_right", "add_3"],
    ["rotate_right", "mod_2"],
    ["rotate_right", "mod_3"],
    ["rotate_right", "subtract_next"],
    ["rotate_right", "adjacent_sum"],
    ["rotate_right", "mirror"],
    ["rotate_right", "take_even_positions"],
    ["rotate_right", "take_odd_positions"],
    #######
    ["rotate_left", "prepend_zero"],
    ["rotate_left", "append_zero"],
    ["rotate_left", "pop_right"],
    ["rotate_left", "pop_left"],
    ["rotate_left", "multiply_2"],
    ["rotate_left", "multiply_3"],
    ["rotate_left", "add_1"],
    ["rotate_left", "add_2"],
    ["rotate_left", "add_3"],
    ["rotate_left", "mod_2"],
    ["rotate_left", "mod_3"],
    ["rotate_left", "subtract_next"],
    ["rotate_left", "adjacent_sum"],
    ["rotate_left", "mirror"],
    ["rotate_left", "take_even_positions"],
    ["rotate_left", "take_odd_positions"],
    #######
    ["swap_first_last", "prepend_zero"],
    ["swap_first_last", "append_zero"],
    ["swap_first_last", "pop_right"],
    ["swap_first_last", "pop_left"],
    ["swap_first_last", "multiply_2"],
    ["swap_first_last", "multiply_3"],
    ["swap_first_last", "add_1"],
    ["swap_first_last", "add_2"],
    ["swap_first_last", "add_3"],
    ["swap_first_last", "mod_2"],
    ["swap_first_last", "mod_3"],
    ["swap_first_last", "subtract_next"],
    ["swap_first_last", "adjacent_sum"],
    ["swap_first_last", "mirror"],
    ["swap_first_last", "take_even_positions"],
    ["swap_first_last", "take_odd_positions"],
]

RULES = [
    {
        "id": f"{i:03d}",
        "primitives": rule,
    }
    for i, rule in enumerate(RAW_RULES)
]


# PRIMITIVE_CONFIG = {
#     "reverse": {},
#     "shift_left": {
#         # "length": lambda arr: random.randint(1, len(arr) - 2),
#         # "fill": lambda arr: 0,
#     },
#     "shift_right": {
#         # "length": lambda arr: random.randint(1, len(arr) - 2),
#         # "fill": lambda arr: 0,
#     },
#     "rotate_left": {
#         # "k": lambda arr: random.randint(1, len(arr) - 2),
#     },
#     "rotate_right": {
#         # "k": lambda arr: random.randint(1, len(arr) - 2),
#     },
#     "swap_first_last": {
#         # "i": lambda arr: random.randint(0, len(arr) - 1),
#         # "j": lambda arr: random.randint(0, len(arr) - 1),
#     },
#     "prepend_zero": {
#         # "length": lambda arr: random.randint(1, 4),
#     },
#     "append_zero": {
#         # "length": lambda arr: random.randint(1, 4),
#     },
#     "pop_left": {
#         # "length": lambda arr: random.randint(1, len(arr) - 2),
#     },
#     "pop_right": {
#         # "length": lambda arr: random.randint(1, len(arr) - 2),
#     },
#     "multiply_constant": {
#         # "c": lambda arr: random.randint(2, 3),
#     },
#     "add_constant": {
#         # "c": lambda arr: random.randint(1, 5),
#     },
#     "modulo": {
#         # "m": lambda arr: random.randint(2, 5),
#     },
#     "differences": {},
#     "pairwise_sum": {},
#     "mirror": {},
#     "sort_ascending": {},
#     "sort_descending": {},
#     "take_even_positions": {},
#     "take_odd_positions": {},
# }


# PRIMITIVES = {
#     "reverse": primitives.reverse,
#     "shift_right": primitives.shift_right,
#     "shift_left": primitives.shift_left,
#     "rotate_right": primitives.rotate_right,
#     "rotate_left": primitives.rotate_left,
#     "swap_first_last": primitives.swap_first_last,
#     "prepend_zero": primitives.prepend_zero,
#     "append_zero": primitives.append_zero,
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


def apply_primitive(arr, primitive_name):
    func = PRIMITIVES[primitive_name]
    # config = PRIMITIVE_CONFIG[primitive_name]

    # params = {name: sampler(arr) for name, sampler in config.items()}

    # return func(arr, **params)
    return func(arr)


def generator(rule):
    length = random.randint(5, 10)
    arr = primitives.random_arr(length)
    output = arr

    for primitive_name in rule["primitives"]:
        output = apply_primitive(output, primitive_name)

    return {"input": [arr], "output": [output]}


def generate_benchmark(
    version_name: str,
    seed: int,
    rules,
    num_examples: int,
    num_tasks_per_rule: int,
    dir: str,
):
    # os.makedirs(f"datasets/{dir}/{version_name}", exist_ok=True)
    os.makedirs(f"datasets/{dir}/{version_name}", exist_ok=True)
    for rule_idx, rule in enumerate(rules):
        for i in range(num_tasks_per_rule):
            examples = []
            task_seed = seed + rule_idx * num_tasks_per_rule + i
            random.seed(task_seed)
            for example_id in range(num_examples):
                # random.seed(2025 + i * num_examples + example_id + seed)
                examples.append(generator(rule))
            # print(examples)
            dataset = {"train": examples[:-1], "test": examples[-1:]}

            with open(
                # f"test/{dir}/{version_name}/{rule['id']}_{i}.json",
                f"datasets/{dir}/{version_name}/{rule['id']}_{i}.json",
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(
                    dataset,
                    f,
                    # indent=2,
                    ensure_ascii=False,
                )
