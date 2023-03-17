def shortest_job_first(processes):
    """
    Simulate Shortest Job First scheduling algorithm on a list of processes.

    Parameters:
    processes (list of tuple): A list of tuples representing the processes. Each tuple has the form (process_id, arrival_time, burst_time).

    Returns:
    A list of tuples representing the scheduling order. Each tuple has the form (process_id, start_time, end_time).
    """
    # Initialize the scheduling order and the current time.
    scheduling_order = []
    current_time = 0

    # Create a list to store the remaining burst time for each process.
    remaining_burst_time = [burst_time for (_, _, burst_time) in processes]

    # Create a list to store the last execution time for each process.
    last_execution_time = [0] * len(processes)

    # Loop until all processes have completed.
    while sum(remaining_burst_time) > 0:
        # Determine the index of the process with the shortest remaining burst time.
        shortest_index = min(i for i in range(len(processes)) if remaining_burst_time[i] > 0)

        # If the shortest process hasn't arrived yet, skip to its arrival time.
        if current_time < processes[shortest_index][1]:
            current_time = processes[shortest_index][1]

        # Update the scheduling order.
        scheduling_order.append((shortest_index, current_time, current_time + remaining_burst_time[shortest_index]))

        # Update the current time.
        current_time += remaining_burst_time[shortest_index]

        # Update the remaining burst time for the process.
        remaining_burst_time[shortest_index] = 0

        # Update the last execution time for the process.
        last_execution_time[shortest_index] = current_time

    return scheduling_order


processes = [
    (0, 0, 5),
    (1, 1, 3),
    (2, 2, 1),
    (3, 3, 2)
]

scheduling_order = shortest_job_first(processes)

for (process_id, start_time, end_time) in scheduling_order:
    print(f"Process {process_id} ran from {start_time} to {end_time}")



