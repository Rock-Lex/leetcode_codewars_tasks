/*
Type: Medium
189. Rotate Array
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
*/

package medium;

import java.util.*;

class Solution {
    public void rotate(int[] nums, int k) {
        if (k == nums.length || nums.length == 1) return;
        k = k % nums.length;

        int [] rotateArray = Arrays.copyOfRange(nums, nums.length - k, nums.length);
        int [] stayArray = Arrays.copyOfRange(nums, 0, nums.length - k);
        System.arraycopy(rotateArray, 0, nums, 0, rotateArray.length);
        System.arraycopy(stayArray, 0, nums, rotateArray.length, stayArray.length);
    }
}