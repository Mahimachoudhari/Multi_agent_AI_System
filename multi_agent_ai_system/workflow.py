from graphviz import Digraph


def create_workflow():
    dot = Digraph()

    dot.node("A", "User Input")
    dot.node("B", "Research Agent")
    dot.node("C", "Planner Agent")
    dot.node("D", "Writer Agent")
    dot.node("E", "Final Report")

    dot.edge("A", "B")
    dot.edge("B", "C")
    dot.edge("C", "D")
    dot.edge("D", "E")

    return dot