# Примеры п. 7.1
# 1. is_in_slot
# 2. is_timeout
# 3. is_overhead
# 4. is_out_of_bound
# 5. is_complete

# Примеры п. 7.2
def double_odds_or_reset(values: list):
    done = False
    for idx, item in enumerate(values):
        if item % 2 == 0:
            values[idx] = item * 2
        else:
            break
    if idx == len(values) - 1:
        done = True
    if done:
        return values
    else:
        return [0 for _ in range(len(values))]

def get_data(param):
    error_counter = 0
    max_attempts = 3
    found = False
    
    while True:
        if error_counter > max_attempts:
            return None
        
        response = request(param)
        
        success = get_status(response)
        
        if success:
            return fetch_result(response)
        else:
            error_counter += 1


# Пример п. 7.3
def index_array(items):
    for pointer, value in enumerate(items):
        ...

# Пример п. 7.4
def get_min_max_range(items):
    minimal = min(items)
    maximum = max(items)
    return range(minimal, maximum)

# Пример п. 7.5
-