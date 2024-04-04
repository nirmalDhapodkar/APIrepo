def time_to_minutes(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    
    # Calculate the total minutes since midnight
    total_minutes = hours * 60 + minutes
    
    return total_minutes
    

def minutes_to_time(minutes):
    # Calculate hours and minutes
    hours = minutes // 60
    minutes = minutes % 60
    
    # Format the time string
    time_str = f"{hours:02}:{minutes:02}"  # :02 ensures zero-padding if needed
    
    return time_str