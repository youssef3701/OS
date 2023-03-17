def round_robin(processes, quantum):
    """
    Simulate Round Robin scheduling algorithm on a list of processes.

    Parameters:
    processes (list of tuple): A list of tuples representing the processes. Each tuple has the form (process_id, arrival_time, burst_time).
    quantum (int): The time quantum.

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

    # Create a queue to store the processes that have arrived but not yet completed.
    queue = []

    # Loop until all processes have completed.
    while sum(remaining_burst_time) > 0:
        # Add any processes that have arrived since the last iteration to the queue.
        for i, (_, arrival_time, _) in enumerate(processes):
            if arrival_time <= current_time and remaining_burst_time[i] > 0 and i not in queue:
                queue.append(i)

        if len(queue) == 0:
            # If the queue is empty, skip to the next arrival time.
            current_time = min(arrival_time for (_, arrival_time, _) in processes if arrival_time > current_time)
        else:
            # Get the next process from the queue.
            process_id = queue.pop(0)

            # Determine how much time the process will execute in this iteration.
            execution_time = min(quantum, remaining_burst_time[process_id])

            # Update the scheduling order.
            scheduling_order.append((process_id, current_time, current_time + execution_time))

            # Update the current time.
            current_time += execution_time

            # Update the remaining burst time for the process.
            remaining_burst_time[process_id] -= execution_time

            # Update the last execution time for the process.
            last_execution_time[process_id] = current_time

            # Add the process back to the queue if it still has remaining burst time.
            if remaining_burst_time[process_id] > 0:
                queue.append(process_id)

    return scheduling_order


processes = [
    (0, 0, 5),
    (1, 1, 3),
    (2, 2, 1),
    (3, 3, 2)
]
quantum = 2

scheduling_order = round_robin(processes, quantum)

for (process_id, start_time, end_time) in scheduling_order:
    print(f"Process {process_id} ran from {start_time} to {end_time}")
