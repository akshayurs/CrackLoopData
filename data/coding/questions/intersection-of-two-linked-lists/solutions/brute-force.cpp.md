The same idea in C++: for every node of `listA`, walk the whole of `listB` comparing raw pointers. Two pointers are equal only when they point at the same node, which is exactly the identity check this problem needs.

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        for (ListNode* nodeA = headA; nodeA != nullptr; nodeA = nodeA->next) {
            for (ListNode* nodeB = headB; nodeB != nullptr; nodeB = nodeB->next) {
                if (nodeA == nodeB) {
                    return nodeA;
                }
            }
        }
        return nullptr;
    }
};
```

## Why it works

The outer loop visits every node of `listA` exactly once; for each one, the inner loop checks every node of `listB` for pointer equality. If the two lists ever share a node, that node will eventually be compared against itself and the pointers will match — and because sharing one node means sharing the entire tail, the first match found is the intersection point closest to both heads.

## Complexity

- Time: O(m * n) — every node of `listA` is compared against every node of `listB`.
- Space: O(1) — only the two loop pointers.
