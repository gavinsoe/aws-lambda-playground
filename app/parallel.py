def parallel_1(event, context):
    print(f"event = {event}")
    print(f"context = {context}")

    x = [1,2,3]
    
    return x


def parallel_2(event, context):
    print(f"event = {event}")
    print(f"context = {context}")

    y = ['a', 'b', 'c']

    return y


def end(event, context):
    print(f"event = {event}")
    print(f"context = {context}")

    return event
