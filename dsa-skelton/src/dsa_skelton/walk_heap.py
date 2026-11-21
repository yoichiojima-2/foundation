import heapq

def walk_heap(items: list[int]) -> list[int]:
    """Push every item onto a min-heap, then pop until empty; return the pop order."""
    heap = []
    for item in items:
        heapq.heappush(heap, item)
    order = []
    while heap:
        order.append(heapq.heappop(heap))
    return order
