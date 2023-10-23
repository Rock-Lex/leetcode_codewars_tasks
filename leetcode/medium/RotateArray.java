/*
Type: Medium
189. Rotate Array
https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
*/


package medium;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.*;

public class RotateArray {
//    Beats 100% of users with Java!
    static class Solution {
        public void rotate(int[] nums, int k) {
            if (k == nums.length || nums.length == 1) return;
            k = k % nums.length;

            int [] rotateArray = Arrays.copyOfRange(nums, nums.length - k, nums.length);
            int [] stayArray = Arrays.copyOfRange(nums, 0, nums.length - k);
            System.arraycopy(rotateArray, 0, nums, 0, rotateArray.length);
            System.arraycopy(stayArray, 0, nums, rotateArray.length, stayArray.length);

            printArray(rotateArray);
            printArray(stayArray);
            printArray(nums);
        }

        private void printArray(int[] array) {
            for (int i = 0; i < array.length; ++i) {
                if (i == 0) {
                    System.out.print("[");
                }
                System.out.print(array[i]);
                if (i == array.length - 1) {
                    System.out.print("]");
                } else {
                    System.out.print(",");
                }
            }
        }
    }

//    Time Limit Exceeded ...
    static class BadSolution {
        public void rotate(int[] nums, int k) {
            if (k == nums.length || nums.length == 1) return;
            k = k % nums.length;
            for (int i = 0; i < k; ++i) {
                nums = rotateArray(nums);
            }
            printArray(nums);
        }

        private int[] rotateArray(int[] nums) {
            int temp = 0;
            for (int i = 0; i < nums.length; ++i) {
                if (i == 0) {
                    int tempInternal = nums[nums.length - 1];
                    temp = nums[i+1];
                    nums[i+1] = nums[i];
                    nums[i] = tempInternal;
                }
                else if (i+1 != nums.length) {
                    int tempInternal = nums[i+1];
                    nums[i+1] = temp;
                    temp = tempInternal;
                }
            }
            return nums;
        }

        private void printArray(int[] array) {
            for (int i = 0; i < array.length; ++i) {
                if (i == 0) {
                    System.out.print("[");
                }
                System.out.print(array[i]);
                if (i == array.length - 1) {
                    System.out.print("]");
                } else {
                    System.out.print(",");
                }
            }
        }
    }

    public static void main(String[] args) {
//        int[] nums = new int[] {1,2,3,4,5,6,7};
//        int[] nums = new int[] {1};
//        int[] nums = new int[] {1,2};
        int[] nums = new int[] {1,2,3,4,5};
        int k = 3;

        Solution solution = new Solution();
        solution.rotate(nums, k);

//        BadSolution badSolution = new BadSolution();
//        badSolution.rotate(nums, k);
    }
}
