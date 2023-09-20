package medium;/*
Type: Medium
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Description:
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 */

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class Longest_Palindromic_Substring {

    static class Solution {
        public String longestPalindrome(String s) {

            if (s.length() == 1)
            {
                return s;
            }

            List<String> answears = new ArrayList<>();

            for (int i = 0; i < s.length(); ++i) {
                char letter = s.charAt(i);
                int index = findFirstCharInString(s, letter, i+1);
                if (index != 0) {
                    String answ = "";
                    for (int j = i; j <= index; ++j)
                    {
                        answ += s.charAt(j);
                    }
                    answears.add(answ);
                }
            }

            if (answears.size() == 0) {
                return String.valueOf(s.charAt(0));
            }
            Collections.sort(answears);
            return answears.get(0);
        }

        public int findFirstCharInString(String s, char letter, int index) {
            for (int i = index; i < s.length(); ++i) {
                if (letter == s.charAt(i)) {
                    return i;
                }
            }
            return 0;
        }

        public boolean isPolindromic(String str) {
            int strLenght = str.length();
            if (strLenght == 1 || strLenght == 2 && str.charAt(0) == str.charAt(1)) {
                return true;
            } else if (strLenght % 2 == 0) {
                String leftStr = str.substring(0, strLenght/2);
                String rightStr = str.substring(strLenght/2, strLenght);
                System.out.println(leftStr + "::" + rightStr);
                return leftStr.equals(reverseString(rightStr));
            } else {
                String leftStr = str.substring(0, strLenght/2);
                String rightStr = str.substring(strLenght/2 + 1, strLenght);
                System.out.println(leftStr + "::" + rightStr);
                return leftStr.equals(reverseString(rightStr));
            }
        }

        public String reverseString(String str) {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append(str);
            return stringBuilder.reverse().toString();
        }


    }

    public static void main(String[] args){
//        String s = "babad";
        String s = "cbbd";

        Solution sol = new Solution();
//        String answear = sol.longestPalindrome(s);
        Boolean answear = sol.isPolindromic(s);
        System.out.println(answear);

    }

}
