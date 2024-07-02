def activity_selection(start_times, finish_times):
    # Combine start and finish times into a list of tuples
    activities = list(zip(start_times, finish_times))
    
    # Sort activities based on finish times
    activities.sort(key=lambda x: x[1])
    
    # Initialize the result list with the first activity
    selected = [activities[0]]
    last_finish_time = activities[0][1]
    
    # Iterate through the remaining activities
    for activity in activities[1:]:
        start_time, finish_time = activity
        
        # If the current activity starts after the last selected activity finishes,
        # add it to the selected list
        if start_time >= last_finish_time:
            selected.append(activity)
            last_finish_time = finish_time
    
    return selected

# Example usage
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]

selected_activities = activity_selection(start_times, finish_times)

print("Selected activities:")
for activity in selected_activities:
    print(f"Start time: {activity[0]}, Finish time: {activity[1]}")