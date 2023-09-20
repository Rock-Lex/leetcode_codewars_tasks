package easy;/*
Type: Easy
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/
*/

public class Valid_Palindrom {
    static class Solution {
        public boolean isPalindrome(String str) {
            str = str.replaceAll("[\\s\\W_]","");
            System.out.println(str);
            int strLenght = str.length();
            if (strLenght == 1 || strLenght == 2 && str.charAt(0) == str.charAt(1)) {
                return true;
            } else if (strLenght % 2 == 0) {
                String leftStr = str.substring(0, strLenght/2);
                String rightStr = str.substring(strLenght/2, strLenght);
                return leftStr.equalsIgnoreCase(reverseString(rightStr));
            } else {
                String leftStr = str.substring(0, strLenght/2);
                String rightStr = str.substring(strLenght/2 + 1, strLenght);
                return leftStr.equalsIgnoreCase(reverseString(rightStr));
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
//        String s = "cbbd";
//        String s = "A man, a plan, a canal: Panama";
        String s = "ab_a";

        Valid_Palindrom.Solution sol = new Valid_Palindrom.Solution();
//        String answear = sol.longestPalindrome(s);
        Boolean answear = sol.isPalindrome(s);
        System.out.println(answear);

    }
}
