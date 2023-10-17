/*
Type: Easy
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
*/

package easy;

import java.util.Hashtable;

public class Remove_Duplicates_Sorted_Array {
    static class Solution {
        public int removeDuplicates(int[] nums) {
            int j = 1;
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] != nums[i - 1]) {
                    nums[j] = nums[i];
                    j++;
                }
            }
            return j;
        }
    }

//    This solution is not as efficient as the first one
    static class Solution2 {
        public int removeDuplicates(int[] nums) {
            Hashtable<Integer, Integer> num_hashtable = new Hashtable<>();
            int index = 0;
            for (int i = 0; i < nums.length; ++i) {
                if (num_hashtable.get(nums[i]) == null) {
                    num_hashtable.put(nums[i], i);
                    nums[index] = nums[i];
                    index++;
                }
            }
            return index;
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[] {1,1,2};

        Solution solution = new Solution();
        System.out.println(solution.removeDuplicates(nums));
    }

}
