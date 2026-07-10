Instead of recursing, work outward from the courses that are already free to take. Count how many prerequisites each course still has left (its in-degree); any course with zero prerequisites can go into the schedule right now. Whenever a course is scheduled, "cross it off" for everything that depended on it, and any course whose count drops to zero joins the queue.

This is Kahn's algorithm. If we ever run out of zero-prerequisite courses before scheduling everyone, the remaining courses are stuck in a cycle.

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        for (auto& p : prerequisites) {
            graph[p[1]].push_back(p[0]);
            indegree[p[0]]++;
        }

        queue<int> q;
        for (int c = 0; c < numCourses; c++) if (indegree[c] == 0) q.push(c);

        vector<int> order;
        order.reserve(numCourses);
        while (!q.empty()) {
            int course = q.front(); q.pop();
            order.push_back(course);
            for (int next : graph[course]) {
                if (--indegree[next] == 0) q.push(next);
            }
        }

        return (int)order.size() == numCourses ? order : vector<int>{};
    }
};
```

## Why it works

A course only enters the queue once every one of its prerequisites has already been scheduled, so the emitted `order` always respects the dependency edges. Seeding the queue by scanning `0` to `numCourses - 1`, and always draining it FIFO, makes the resulting order deterministic for a given graph. If a cycle exists, the courses inside it never reach in-degree zero, so `order` ends up shorter than `numCourses` and we report failure with an empty vector.

## Complexity

- Time: O(V + E) — every course is enqueued once and every edge is relaxed once.
- Space: O(V + E) — the adjacency list, in-degree array, and queue.
