/*
Type: Easy
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

 */

package easy;

import java.util.Arrays;

public class MergeSortedArray {
    static class Solution {
        public void merge(int[] nums1, int m, int[] nums2, int n) {
//            int[] mergedNums = new int[n+m];
//            for (int i = 0, j = 0, k = 0; ;) {
//                if (i == mergedNums.length) {
//                    break;
//                }
//                if (j < m) {
//                    mergedNums[i] = nums1[j];
//                    j++;
//                } else if (k < n) {
//                    mergedNums[i] = nums2[k];
//                    k++;
//                }
//                i++;
//            }
            for (int i = m, j = 0; i < m+n; ++i) {
                nums1[i] = nums2[j];
                j++;
            }
            Arrays.sort(nums1);
            for (int i = 0; i < nums1.length; ++i) {
                if (i == 0) {
                    System.out.print("[");
                }
                System.out.print(nums1[i]);
                if (i == nums1.length - 1) {
                    System.out.print("]");
                } else {
                    System.out.print(",");
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] nums1 = new int[] {1,2,3,0,0,0};
        int m = 3;
        int[] nums2 = new int[] {2,5,6};
        int n = 3;

        Solution solution = new Solution();
        solution.merge(nums1, m, nums2, n);

    }
}

