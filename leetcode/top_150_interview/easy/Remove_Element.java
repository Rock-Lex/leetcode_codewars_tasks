/*
Type: Easy
27. Remove Element
https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
*/

package easy;

public class Remove_Element {
    static class Solution {
        public int removeElement(int[] nums, int val) {
            int index = 0;
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] != val) {
                    nums[index] = nums[i];
                    index++;
                }
            }
            return index;
        }
    }
    public static void main(String[] args) {
        int[] nums = new int[] {3,2,2,3};
//        int[] nums = new int[] {0,1,2,2,3,0,4,2};
//        int[] nums = new int[] {3,3};
        int val = 3;

        Solution solution = new Solution();
        System.out.println(solution.removeElement(nums, val));
    }
}
