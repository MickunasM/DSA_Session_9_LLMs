##############################################################
# Data Structures and Algorithms — Session 09
# LLMs and How to Code With Them
#
# HOW THIS SESSION WORKS
# ----------------------
# In this session you will use an LLM (ChatGPT, Claude, Gemini,
# Copilot — whichever you prefer) to help you write code. 
# You do NOT need to connect to any API or pay for anything. 
##############################################################
# For each exercise you will:
#   1. Read the function's docstring carefully
#   2. Copy the suggested prompt (or write your own better one)
#   3. Paste the LLM's code under # YOUR CODE BELOW THIS
#   4. Run the doctests to verify the output is correct
#      (python -m doctest ses10.py -v)
#   5. If any tests fail, read the note on feeding failures back
#
# The goal is NOT to get answers — it is to practise using LLMs
# responsibly: clear prompting, then rigorous verification.
##############################################################


##############################################################
# PART 1 — Warm-up: Revisiting Session 6 (Dictionaries)
#
# In Session 6 you wrote these functions yourself from scratch.
# This time, ask an LLM to write them for you, then verify the
# output using the doctests that are already in the docstrings.
#
# PROMPT ENGINEERING TIP
# A vague prompt produces vague results. Compare:
#
#   BAD:  "Write a Python function that counts characters."
#
#   GOOD: "Write a Python function called count_characters(a)
#          that counts how many times each character appears
#          in the input string a. It should return a dictionary
#          whose keys are the characters and whose values are
#          their counts. For example, count_characters('aaaa')
#          should return {'a': 4}, and count_characters('test')
#          should return a dictionary where 't' maps to 2."
#
# The good prompt gives: the function name, the parameter name,
# the return type, and a concrete example. Use this structure
# for all exercises below.
##############################################################


def print_dict_values(a):
    """
    Prints the key-value pairs of the input dictionary a, sorted
    based on the key value.

    Parameters:
        a: dictionary

    Returns:
        the number of keys the input dictionary includes

    Examples:
    >>> print_dict_values({'Zoe': 'ICL', 'Mark': 'UCL'})
    Mark UCL
    Zoe ICL
    2
    >>> print_dict_values({'banana': 'yellow', 'apple': 'green', 'berry': 'blue'})
    apple green
    banana yellow
    berry blue
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 1a
    # Ask an LLM to write this function. 
    # Suggested prompt:
    # "Write a Python function called print_dict_values(a) that
    #  prints the key-value pairs of a dictionary, sorted by key,
    #  with a space between each key and value. It should return
    #  the number of keys in the dictionary. For example,
    #  print_dict_values({'Zoe': 'ICL', 'Mark': 'UCL'}) should
    #  print 'Mark UCL' then 'Zoe ICL' and return 2."
    #
    # Paste the LLM's code below, then run the doctests.
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


def count_characters(a):
    """
    Counts how many times different characters appear in the
    input string.

    Returns:
        dictionary whose:
            keys are the characters appearing in the input string a
            values are the counts of those characters

    Examples:
    >>> count_characters('aaaa')
    {'a': 4}
    >>> x = count_characters('test')
    >>> print(x['t'])
    2
    >>> x = count_characters('hello')
    >>> print(x['h'])
    1
    >>> x = count_characters('hello world')
    >>> print(x['l'])
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 1b
    # Write your own prompt for this function following the
    # structure from the tip above, then paste the LLM's code.
    #
    # YOUR PROMPT: (write it here as a comment before pasting)
    #
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


def divide(a, b):
    """
    Divides a by b; catches division by zero.

    Parameters:
        a, b: numbers

    Returns:
        a divided by b.
        If b is 0, prints 'No division by 0.' and returns None.

    Examples:
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    No division by 0.
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 1c — VERIFICATION FOCUS
    #
    # Ask an LLM to write this function, but use a VAGUE prompt
    # first, then a SPECIFIC prompt. Compare the two outputs.
    #
    # VAGUE prompt to try first:
    #   "Write a Python divide function."
    #
    # SPECIFIC prompt to try second:
    #   "Write a Python function called divide(a, b) that
    #    returns a divided by b as a float. If b is zero it
    #    should print the string 'No division by 0.' and return
    #    None. Use a try/except block to catch ZeroDivisionError."
    #
    # Question: did the vague prompt handle the zero case?
    # Paste your chosen solution below and verify with doctests.
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


def count_words(a):
    """
    Counts the occurrence of different words in the input string a.

    Parameters:
        a: string

    Returns:
        dictionary whose:
            keys are words
            values are the counts of those words

    Examples:
    >>> x = count_words('test sentence')
    >>> print(x['test'])
    1
    >>> x = count_words('it is what it is')
    >>> print(x['it'])
    2
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 1d — ASKING FOR ALTERNATIVES
    #
    # Ask an LLM to solve this, but add to your prompt:
    #   "...give me two different implementations: one using
    #    a plain dictionary, and one using collections.Counter."
    #
    # Both should pass the doctests. Which do you prefer and why?
    # Paste your preferred solution below.
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


##############################################################
# PART 2 — Revisiting Session 7 (Graphs and BFS)
#
# FEEDING FAILURES BACK TO THE LLM
# If the LLM's code fails a doctest, don't just re-prompt
# vaguely. Copy the exact error message and paste it back:
#
#   "Your code failed this test:
#    bfs_dists['Donald'] expected 4 but got 3.
#    Here is the failing test and your code: [paste both].
#    Please fix the function."
#
# This is the same loop a professional engineer uses.
##############################################################

# This import will only work if ses07_data_structures.py is in
# the same directory as this file (same as Session 7).
from ses07_data_structures import Graph, Queue


def create_bfs_graph():
    """
    Initialises the undirected graph from the Session 7 lecture.
    Uses the add_edge method.

    Returns: Graph object of the lecture graph.

    Examples:
    >>> ex_graph = create_bfs_graph()
    >>> [x in ex_graph.children_of('Jared') for x in ['John', 'Helena', 'Donald', 'Paul']]
    [False, False, True, True]
    >>> ex_graph = create_bfs_graph()
    >>> [x in ex_graph.children_of('Helena') for x in ['John', 'Helena', 'Donald', 'Paul']]
    [True, False, False, True]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 2a
    # The graph has the following edges (from the Session 7 slides):
    #   John -- Helena, John -- Chris,
    #   Helena -- Chris, Helena -- Paul,
    #   Chris -- Paul, Chris -- Vicki,
    #   Jared -- Vicki, Jared -- Donald, Jared -- Paul
    #
    # Ask an LLM to write this function. Include the edge list
    # above in your prompt and specify that Graph() uses
    # g.add_edge(node1, node2) to add undirected edges.
    #
    # Verify with the doctests — they check specific neighbours.
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


def bfs(graph, start):
    """
    Breadth-first search using the Queue data structure.

    Parameters:
        graph (Graph): the graph to search
        start: starting node

    Returns:
        dists: dictionary of shortest distances from start to all
               reachable nodes (key: node, value: distance)

    Examples:
    >>> ex_graph = create_bfs_graph()
    >>> bfs_dists = bfs(ex_graph, 'John')
    >>> [bfs_dists['Donald'], bfs_dists['Jared']]
    [4, 3]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 2b — GUIDED PROMPT WRITING
    #
    # Write a prompt that explains BFS in plain English and asks
    # the LLM to implement it. Your prompt should mention:
    #   - The Queue class with methods: enqueue(x), dequeue(),
    #     is_empty()
    #   - graph.children_of(v) returns adjacent nodes
    #   - The function should return a dists dictionary
    #   - Start node has distance 0; each neighbour's distance
    #     is one more than the current node's distance
    #
    # After pasting the LLM's code, check:
    #   python -m doctest ses10.py -v
    #
    # IMPORTANT: the doctest requires create_bfs_graph() to work
    # first (Exercise 2a), so complete that before testing this.
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


def bfs_track_path(graph, start):
    """
    BFS that also records the path taken to reach each node.

    Parameters:
        graph (Graph): the graph to search
        start: starting node

    Returns:
        dists: dictionary of shortest distances (as above)
        prev_nodes: dictionary where prev_nodes[v] is the node
                    from which v was first reached; None for start

    Examples:
    >>> ex_graph = create_bfs_graph()
    >>> bfs_dists, prev_nodes = bfs_track_path(ex_graph, 'John')
    >>> [prev_nodes['Donald'], prev_nodes['Helena'], prev_nodes['John']]
    ['Jared', 'John', None]
    >>> ex_graph = create_bfs_graph()
    >>> bfs_dists, bfs_paths = bfs_track_path(ex_graph, 'John')
    >>> [bfs_dists['Donald'], bfs_dists['Jared']]
    [4, 3]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 2c — ITERATIVE IMPROVEMENT
    #
    # Rather than writing a new prompt from scratch, paste your
    # working bfs() code into the LLM and say:
    #
    #   "Here is my working BFS function: [paste code].
    #    Please extend it to also return a second dictionary
    #    called prev_nodes where prev_nodes[v] stores the node
    #    from which v was first discovered. The starting node
    #    should map to None."
    #
    # This is a common real-world pattern: extend existing code
    # rather than rewriting from scratch.
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


def print_path(prev_nodes, v):
    """
    Prints the path from the starting node to v, using the
    prev_nodes dictionary returned by bfs_track_path.

    Example:
    >>> ex_graph = create_bfs_graph()
    >>> _, prev_nodes = bfs_track_path(ex_graph, 'John')
    >>> print_path(prev_nodes, 'Donald')
    John -> Helena -> Paul -> Jared -> Donald
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 2d
    # The algorithm:
    #   - Start at v, keep following prev_nodes[v] until None
    #   - Collect nodes into a list, reverse it
    #   - Join with ' -> ' and print
    #
    # Ask an LLM to implement this. Include the algorithm
    # description above word-for-word in your prompt.
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


##############################################################
# PART 3 — Revisiting Session 8 (Dijkstra's Algorithm)
#
# THE CARDINAL RULE
# From the lecture: never submit or use AI-written code without
# verifying it. The doctests below are your verification step.
# If the LLM returns code that does not pass all doctests,
# you must fix it — either by prompting again or editing the
# code yourself.
##############################################################

import ses08_graphs as gs


def lecture_graph():
    """
    Returns the Session 8 lecture directed graph as an adjacency
    list dictionary. Edge weights are integers.

    Examples:
    >>> adj_list = lecture_graph()
    >>> adj_list['d']['e']
    2
    >>> 'd' in adj_list['e']
    False
    >>> [adj_list[n][m] for n in 'abcde' for m in 'abcde' if m in adj_list[n]]
    [1, 5, 2, 5, 2, 6, 2]
    >>> [len(adj_list[n]) for n in 'abcde']
    [2, 2, 2, 1, 0]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 3a
    # The adjacency list is incomplete — it does not match the
    # doctests above. Ask an LLM to complete it.
    #
    # Suggested prompt:
    #   "I have a Python dictionary representing a directed
    #    weighted graph as an adjacency list. Node 'a' points
    #    to two nodes, 'b' and 'c', with weights 1 and 5. Node
    #    'b' points to 'c' with weight 2 and 'd' with weight 5.
    #    Node 'c' points to 'd' with weight 2 and 'e' with weight
    #    6. Node 'd' points to 'e' with weight 2. Node 'e' has no
    #    outgoing edges. Write this as a Python dictionary of
    #    dictionaries called distances, where distances[src][dst]
    #    gives the edge weight."
    #
    # Then verify: all four doctests must pass.
    # -------------------------------------------------------
    distances = {
        'a': {},
        'b': {'c': 2, 'd': 5},
        'c': {},
        'd': {},
        'e': {}
    }
    return distances


def dijkstra(graph, start):
    """
    Shortest distances using Dijkstra's algorithm.

    Polynomial-time implementation.
    Assumes a path exists from start to all other nodes.

    Parameters:
        graph: a Graph (or Digraph) object
        start: starting node

    Returns:
        dists: dictionary of shortest distances to all nodes
        prev_nodes: dictionary of the previous node on the
                    shortest path to each node (None for start)

    Examples:
    >>> graph = gs.Digraph(lecture_graph())
    >>> dists, prev_nodes = dijkstra(graph, 'a')
    >>> [dists['b'], dists['e'], dists['c'], dists['d']]
    [1, 7, 3, 5]
    >>> [prev_nodes['a'], prev_nodes['e'], prev_nodes['c'], prev_nodes['d']]
    [None, 'd', 'b', 'c']
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 3b — THE MAIN CHALLENGE
    #
    # The skeleton below is almost complete but has two bugs:
    #   1. prev_nodes is not initialised (set to ...)
    #   2. prev_nodes is never updated inside the loop
    #   3. The function does not return prev_nodes
    #
    # Ask an LLM to fix these bugs. Paste the skeleton and say:
    #
    #   "This Dijkstra implementation has three bugs: prev_nodes
    #    is not initialised, it is never updated when a new
    #    minimum-distance node is found, and it is not returned.
    #    Please fix all three issues. graph.children_of(src)
    #    returns a list of (destination, weight) tuples."
    #
    # Then paste the corrected code below and verify all
    # four doctests pass.
    #
    # SKELETON (do not delete — paste the LLM's fix below it):
    # ---------------------------------------------------------
    # X = set()
    # X.add(start)
    # prev_nodes = ...                      # BUG 1: fix this
    # A = dict()
    # for node in graph.get_nodes():
    #     A[node] = float('Inf')
    # A[start] = 0
    # while len(X) < len(graph.get_nodes()):
    #     min_edge = []
    #     min_dist = float('inf')
    #     for src in X:
    #         for dest, weight in graph.children_of(src):
    #             if dest not in X:
    #                 if A[src] + weight < min_dist:
    #                     min_edge = [src, dest, weight]
    #                     min_dist = A[src] + weight
    #     A[min_edge[1]] = A[min_edge[0]] + min_edge[2]
    #     X.add(min_edge[1])
    #     # BUG 2: update prev_nodes here
    # return A                              # BUG 3: also return prev_nodes
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


def print_path(prev_nodes, v):
    """
    Prints the shortest path from the start node to v using
    the prev_nodes dictionary returned by dijkstra().

    Example:
    >>> graph = gs.Digraph(lecture_graph())
    >>> _, prev_nodes = dijkstra(graph, 'a')
    >>> print_path(prev_nodes, 'e')
    a -> b -> c -> d -> e
    """
    # DON'T CHANGE ANYTHING ABOVE
    # -------------------------------------------------------
    # EXERCISE 3c
    # This is the same algorithm as print_path in Part 2.
    # Ask the LLM to reuse your Part 2 solution here.
    # The doctest gives you the expected output to verify against.
    # -------------------------------------------------------
    # YOUR CODE BELOW THIS


##############################################################
# PART 4 — Stretch: Writing a New Function With LLM Help
#
# Now that you have working BFS and Dijkstra implementations,
# use an LLM to extend one of them.
#
# Choose ONE of the following tasks and implement it:
#
# OPTION A — BFS: find ALL shortest paths (not just one)
#   Write a function all_shortest_paths(graph, start, end)
#   that returns a list of all shortest paths from start to end.
#   Each path is a list of node names.
#
# OPTION B — Dijkstra: handle disconnected graphs
#   The current dijkstra() crashes if any node is unreachable.
#   Write a safe version dijkstra_safe(graph, start) that
#   returns float('inf') for unreachable nodes instead of
#   crashing.
#
# OPTION C — Dijkstra: reconstruct the full path as a list
#   Write a function shortest_path_list(prev_nodes, v) that
#   returns the path as a Python list (not just prints it).
#   E.g. ['a', 'b', 'c', 'd', 'e'] for the lecture graph.
#
# PROMPT ENGINEERING TIPS FOR THIS EXERCISE:
#   - Start with the clarifying-questions trick:
#     "Before writing code, ask me up to 3 clarifying questions."
#   - Include the existing function signature and docstring
#     in your prompt so the LLM understands what already exists.
#   - Ask the LLM to also write two test cases.
#   - If it fails your tests, paste the failure message back.
##############################################################

# -------------------------------------------------------
# EXERCISE 4 — Write your chosen function here.
# Include:
#   1. Your prompt (as a comment)
#   2. The LLM's code (pasted below)
#   3. At least two test cases that you have verified pass
# -------------------------------------------------------

# YOUR PROMPT:
#

# YOUR CODE AND TESTS BELOW THIS


##############################################################
# REFLECTION QUESTIONS — answer as comments at the bottom
#
# Q1. Did a vague prompt ever produce code that passed all
#     tests first time? What was missing when it failed?
#
# Q2. Which exercise required the most back-and-forth with
#     the LLM? Why do you think that was?
#
# Q3. Were there any cases where the LLM's code passed all
#     the provided doctests but you still weren't confident
#     it was correct? What additional tests would you add?
#
# Q4. Based on today, describe one task in your future career
#     where you would use an LLM for coding help, and one
#     task where you would not. Justify both choices.
##############################################################

# Q1:
# Q2:
# Q3:
# Q4: