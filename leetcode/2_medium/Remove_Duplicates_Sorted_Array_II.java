/*
Type: Medium
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
*/

package medium;

import java.util.Hashtable;

public class Remove_Duplicates_Sorted_Array_II {
    static class Solution {
        public int removeDuplicates(int[] nums) {
            if (nums.length < 3) return nums.length;
            int i = 0, j = 0;
            while (i < nums.length) {
                nums[j++] = nums[i++];
                if (i < nums.length && nums[i] == nums[j-1])
                    nums[j++] = nums[i++];
                while (i < nums.length && nums[i] == nums[j-1]) i++;
            }
            return j;
        }
    }
    static class SecondSolution {
        public int removeDuplicates(int[] nums) {
            Hashtable<Integer, Integer> num_hashtable = new Hashtable<>();
            int index = 0;
            for (int i = 0; i < nums.length; ++i) {
                if (num_hashtable.get(nums[i]) == null) {
                    num_hashtable.put(nums[i], 1);
                    nums[index] = nums[i];
                    index++;
                } else if (num_hashtable.get(nums[i]) < 2) {
                    num_hashtable.put(nums[i], num_hashtable.get(nums[i]) + 1);
                    nums[index] = nums[i];
                    index++;
                }
            }
            return index;
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[] {1,1,1,2,2,3};

        Solution solution = new Solution();
        System.out.println(solution.removeDuplicates(nums));
    }
}
