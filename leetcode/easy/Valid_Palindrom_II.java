package easy;
/*
Type: Easy
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Time Complexity :- BigO(N)
Space Complexity :- BigO(1)
 */

public class Valid_Palindrom_II {
    class Solution {
        public boolean validPalindrome(String s) {
            return isPalindrome(s, 0, s.length() - 1, false);
        }

        public boolean isPalindrome(final String s, int leftIndex, int rightIndex, final boolean isCharacterDeleted){
            while(leftIndex < rightIndex){
                if(s.charAt(leftIndex) != s.charAt(rightIndex)){
                    if(isCharacterDeleted){
                        return false;
                    }
                    // isPalindrome(s, leftIndex + 1, rightIndex, true) for cases like "ececabbacec"
                    // isPalindrome(s, leftIndex, rightIndex - 1, true) for cases like "abccbab"
                    return isPalindrome(s, leftIndex + 1, rightIndex, true) || isPalindrome(s, leftIndex, rightIndex - 1, true);
                }
                ++leftIndex;
                --rightIndex;
            }
            return true;
        }
    }


    public void main(String[] args){
//        String s = "babad";
        String s = "aba";
        Solution sol = new Solution();
        Boolean answear = sol.validPalindrome(s);
        System.out.println(answear);

    }
}
