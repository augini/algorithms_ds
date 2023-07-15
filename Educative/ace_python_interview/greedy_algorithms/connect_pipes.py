import heapq


def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """
    heapq.heapify(pipes)

    # initialize the result
    cost = 0

    while len(pipes) > 1:
        # Extract shortest two pipes from the priority queue
        first = heapq.heappop(pipes)
        second = heapq.heappop(pipes)

        # Connect the pipe: update cost
        # and insert the new pipe to pipes queue
        cost += first + second
        heapq.heappush(pipes, first + second)

    return cost
