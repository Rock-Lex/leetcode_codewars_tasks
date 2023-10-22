/*
Type: Medium
189. Rotate Array
https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
*/

package medium;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class RotateArray {
    static class Solution {
        public void rotate(int[] nums, int k) {
            for (int i = nums.length - k, index = 0; i < nums.length; ++i) {
                int temp = nums[i];
                nums[i] = nums[index];
                nums[index] = temp;
                index++;
            }
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

    public static void main(String[] args) {
        int[] nums = new int[] {1,2,3,4,5,6,7,8,9};
        int k = 3;

        Solution solution = new Solution();
        solution.rotate(nums, k);
    }
}
