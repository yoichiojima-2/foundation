def walk_stack(items: list[int]) -> list[int]:
    """Push every item onto a stack, then pop until empty; return the pop order."""
    stack = []
    for item in items:
        stack.append(item)
    res = []
    while stack:
        res.append(stack.pop())
    return res
