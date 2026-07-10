You are given two arrays of **distinct** integers, `nums1` and `nums2`, where every value in `nums1` also appears in `nums2`. For each value `x` in `nums1`, find its **next greater element** in `nums2`: the first value strictly greater than `x` that lies to the right of `x`'s position in `nums2`.

Return an array `ans` of the same length as `nums1`, where `ans[i]` is the next greater element for `nums1[i]`, or `-1` if no such element exists. The answer follows the order of `nums1`.

## Examples

```text
Input:  nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
```

```text
Input:  nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [3, -1]
```

```text
Input:  nums1 = [1], nums2 = [1, 2, 3]
Output: [2]
```

## Constraints

- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are distinct.
- Every element of nums1 also appears in nums2.

## Follow-up

Can you compute every answer in O(nums1.length + nums2.length) time?
