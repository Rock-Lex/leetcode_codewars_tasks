/*
Type: Medium
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
*/

package medium;

import java.util.Hashtable;

class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length < 3) return nums.length;
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
