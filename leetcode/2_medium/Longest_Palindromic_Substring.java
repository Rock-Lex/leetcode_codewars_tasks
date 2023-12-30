/*
Type: Medium
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Description:
Given a string s, return the longest
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
 */

package medium;

public class Longest_Palindromic_Substring {

    static class Solution {
        int maxLenght = 0;
        int lo = 0;
        public String longestPalindrome(String s) {
            char[] input = s.toCharArray();
            if(s.length() < 2) {
                return s;
            }

            for(int i = 0; i<input.length; ++i) {
                expandPalindrome(input, i, i);
                expandPalindrome(input, i, i+1);
            }
            return s.substring(lo, lo + maxLenght);
        }

        public void expandPalindrome(char[] s, int j, int k) {
            while(j >= 0 && k < s.length && s[j] == s[k]) {
                j--;
                k++;
            }
            if(maxLenght < k - j - 1) {
                maxLenght = k - j - 1;
                lo = j+1;
            }
        }
    }

    public static void main(String[] args){
//        String s = "babad";
        String s = "cbbd";

        Solution solution = new Solution();
        System.out.println(solution.longestPalindrome(s));
    }
}
