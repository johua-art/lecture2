def guess_number(N):
    low = 0
    high = 1000
    count = 0
    
    while low <= high:
        count += 1
        mid = (low + high) // 2  # Use integer division for the midpoint
        
        if mid < N:
            low = mid + 1  # Narrow down to the upper half
        elif mid > N:
            high = mid - 1  # Narrow down to the lower half
        else:
            break  # Found the number

    print(f"count: {count}")
    print(f"answer: {N}")

