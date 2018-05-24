def get_fib(position):
    if(position == 0 or position == 1):
        return position
    else:
        return get_fib(position-1) + get_fib(position-2)
    
# Test cases
print(get_fib(4))
print(get_fib(5))
print(get_fib(6))
