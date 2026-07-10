A different way to see the same graph: a course with zero remaining prerequisites is safe to take right now. Take it, then "remove" it — which lowers the prerequisite count of every course that depended on it — and repeat. If this process can eventually take every course, there was no cycle; if it stalls with courses left over, those remaining courses are stuck in a cycle.

This is Kahn's algorithm for topological sorting. Track each course's in-degree (how many prerequisites it still needs), seed a queue with the courses that need none, and process the queue while decrementing in-degrees of dependents.

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        for (auto& p : prerequisites) {
            graph[p[1]].push_back(p[0]);
            indegree[p[0]]++;
        }

        queue<int> q;
        for (int c = 0; c < numCourses; c++) {
            if (indegree[c] == 0) q.push(c);
        }

        int taken = 0;
        while (!q.empty()) {
            int course = q.front();
            q.pop();
            taken++;
            for (int dependent : graph[course]) {
                if (--indegree[dependent] == 0) q.push(dependent);
            }
        }

        return taken == numCourses;
    }
};
```

## Why it works

A course only enters the queue once every one of its prerequisites has already been taken, so the order courses are popped in is always a valid schedule. If the graph is acyclic, this process empties the queue only after every course has been taken. If a cycle exists, every course in it perpetually needs at least one prerequisite that never finishes, so it is never enqueued — leaving `taken < numCourses`.

## Complexity

- Time: O(V + E) — every course is enqueued once and every edge relaxes one in-degree.
- Space: O(V + E) — the adjacency list, in-degree array, and queue.
