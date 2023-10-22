/*
Type: Easy
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 */

package easy;

import java.util.Enumeration;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;

public class Longest_Palindrome {
//    still a bad solution
    static class Solution {
        public int longestPalindrome(String s) {
            int oddCount = 0;
            Map<Character, Integer> map = new HashMap<>();
            for (char ch : s.toCharArray()) {
                map.put(ch, map.getOrDefault(ch, 0) + 1);
                if (map.get(ch) % 2 == 1)
                    oddCount++;
                else
                    oddCount--;
            }
            if (oddCount > 1)
                return s.length() - oddCount + 1;
            return s.length();
        }
    }

//    Bad solution. But it works
    static class SecondSolution {
        public int longestPalindrome(String s) {
            Hashtable<String, Integer> num_chars = new Hashtable<String, Integer>();
            for (int i = 0; i < s.length(); ++i) {
                String charStr = String.valueOf(s.charAt(i));
                if (num_chars.get(charStr) == null) {
                    num_chars.put(charStr, 1);
                } else {
                    int num = num_chars.get(charStr);
                    num_chars.put(charStr, ++num);
                }
            }
            Enumeration<String> keys = num_chars.keys();
            int answear = 0;
            Boolean isUneven = false;
            while (keys.hasMoreElements()) {
                String key = keys.nextElement();
                int value = num_chars.get(key);
                if (value % 2 != 0) {
                    isUneven = true;
                    answear += value - 1;
                } else {
                    answear += value;
                }
            }
            if (isUneven) {
                return answear + 1;
            }
            else return answear;
        }
    }

    public static void main(String[] args){
//        String s = "abccccdd";
//        String s = "a";
//        String s = "ccc";
        String s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
        Longest_Palindrome.Solution solution = new Longest_Palindrome.Solution();

        System.out.println(solution.longestPalindrome(s));
    }
}
