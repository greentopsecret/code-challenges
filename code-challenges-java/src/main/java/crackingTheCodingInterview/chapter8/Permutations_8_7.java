package crackingTheCodingInterview.chapter8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Permutations_8_7 {
    public static List<String> solution(String str) {
        List<String> result = new ArrayList<>();
        if (str.length() == 0) {
            return result;
        }
        if (str.length() == 1) {
            result.add(str);
            return result;
        }

        String ch = str.substring(str.length() - 1);
        str = str.substring(0, str.length() - 1);
        for (String comb : solution(str)) {
            result.add(comb + ch);
            result.add(ch + comb);
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(Permutations_8_7.solution("ab"));
    }
}
