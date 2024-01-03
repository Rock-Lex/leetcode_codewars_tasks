/*
Type: Easy
169. Majority Element
https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
*/

import java.util.Arrays;


class Solution {
        public int majorityElement(int[] nums) {
            Arrays.sort(nums);
            return nums[nums.length/2];
        }
}