def generate_data(event, context):
    print(f"event = {event}")
    print(f"context = {context}")
    
    data = range(100)
    
    return list(data)

def process_element(event, context):
    print(f"event = {event}")
    print(f"context = {context}")
    
    return f"{event} - processed"

def get_result(event, context):
    print(f"event = {event}")
    print(f"context = {context}")
    
    return event