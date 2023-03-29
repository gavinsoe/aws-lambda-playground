def step_1(event, context):
    print(f"event = {event}")
    print(f"context = {context}")

    output = {
        "name": "test-output-1",
        "dictionary object": {"key 1": "value 1", "key 2": "value 2"},
    }

    return output


def step_2(event, context):
    print(f"event = {event}")
    print(f"context = {context}")

    output = {
        "name": "test-output-2",
        "dictionary object": {"key 1": "value 1", "key 2": "value 2"},
    }

    return output


def step_3(event, context):
    print(f"event = {event}")
    print(f"context = {context}")

    output = {
        "name": "test-output-3",
        "dictionary object": {"key 1": "value 1", "key 2": "value 2"},
    }

    return output
