/*
Type: Easy
169. Majority Element
https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
*/

package easy;

import medium.Remove_Duplicates_Sorted_Array_II;

import java.util.Arrays;
import java.util.Hashtable;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Majority_Element {
    class Solution {
        public int majorityElement(int[] nums) {
            Arrays.sort(nums);
            int n = nums.length;
            return nums[n/2];
        }
    }
    class SecondSolution {
        public int majorityElement(int[] nums) {
            Hashtable<Integer, Integer> numsFrequency = new Hashtable<>();

            for (int num : nums) {
                if (numsFrequency.get(num) == null) {
                    numsFrequency.put(num, 1);
                }
                else {
                    numsFrequency.put(num, numsFrequency.get(num) + 1);
                }
                if (numsFrequency.get(num) > nums.length / 2) {
                    return num;
                }
            }
            return 0;
        }
    }


    @Test
    void testFirstSolutionMajorityElement() {
        int[] nums = new int[] {3,2,3};
        int expect = 3;

        Solution solution = new Solution();
        SecondSolution secondSolution = new SecondSolution();

        assertEquals(expect, solution.majorityElement(nums));
        assertEquals(expect, secondSolution.majorityElement(nums));
    }
}