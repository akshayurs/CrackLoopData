**Data-structure design** problems hand you a spec — a class with named operations and a complexity budget for each — and ask you to build it from scratch. There is no single algorithm here; the skill is **composing existing primitives** (arrays, hash maps, linked lists, heaps) so that every required operation hits its target complexity at once.

The recurring trick is that no single structure does everything fast. A hash map gives O(1) lookup but no order. An array gives O(1) index access but O(n) insert/delete in the middle. A doubly linked list gives O(1) insert/delete anywhere but O(n) lookup. So you **glue two structures together**, using one to fix the other's weak spot — usually a hash map from key to a node/index, paired with a list or array that holds the ordering or bulk data.

A typical shape:

```
class Structure:
    map = key -> node            # O(1) find
    list = doubly linked list    # O(1) move-to-front / evict

    get(key):
        node = map[key]
        move node to front of list
        return node.value

    put(key, value):
        if key in map: update and move to front
        else: create node, add to front, map[key] = node
             if over capacity: evict list tail, remove from map
```

This is exactly LRU Cache's skeleton: hash map + doubly linked list, each covering the other's gap so `get` and `put` are both O(1).

Other common pairings: array + hash map (for O(1) random-access removal, as in Insert-Delete-GetRandom), two heaps (median tracking), hash map + buckets-of-doubly-linked-lists (LFU's frequency layer), or a hash map fronting an interval/bucket array (Time-Based Store, Hit Counter).
