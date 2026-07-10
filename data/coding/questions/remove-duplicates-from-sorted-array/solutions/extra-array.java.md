The most direct reading of the problem: collect the distinct values, then write them back to the front of the array. Because the input is sorted, a value is new exactly when it differs from the last value you kept, so a single scan builds the unique list.

Copy those values back over the first slots of `nums` and return the count. It costs a second array, but it maps cleanly onto the problem statement.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int removeDuplicates(int[] nums) {
        List<Integer> unique = new ArrayList<>();
        for (int n : nums) {
            if (unique.isEmpty() || unique.get(unique.size() - 1) != n) {
                unique.add(n);
            }
        }
        for (int i = 0; i < unique.size(); i++) {
            nums[i] = unique.get(i);
        }
        return unique.size();
    }
}
```

## Why it works

Duplicates in a sorted array are always adjacent, so comparing each element to the last one added is enough to filter repeats — `unique` ends up holding every distinct value in its original order. Writing those values back over `nums[0..k)` leaves the front of the array in the required state, and `k` is simply the count of distinct values.

## Complexity

- Time: O(n) — one pass to build the list, one pass to copy it back.
- Space: O(n) — the auxiliary list can hold up to n values.
