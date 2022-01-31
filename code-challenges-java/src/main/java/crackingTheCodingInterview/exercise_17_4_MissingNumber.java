package crackingTheCodingInterview;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class exercise_17_4_MissingNumber {

    private static int solution(List<Integer> numbers) {
        return solution(numbers, 0);
    }

    private static int solution(List<Integer> numbers, int position) {
        if (numbers.size() == 0) {
            return 0;
        }
        List<Integer> zeros = new ArrayList<>(numbers.size() / 2);
        List<Integer> ones = new ArrayList<>(numbers.size() / 2);

        for (int number : numbers) {
            if ((number & (1 << position)) == 0) {
                zeros.add(number);
            } else {
                ones.add(number);
            }
        }

        if (zeros.size() <= ones.size()) {
            int v = solution(zeros, position + 1);
            return (v << 1) | 0;
        } else {
            int v = solution(ones, position + 1);
            return (v << 1) | 1;
        }
    }


    public static void main(String[] args) {
        System.out.println(solution(Arrays.asList(2, 7, 0, 3, 4, 5, 1)) == 6 ? "OK" : "KO");
        System.out.println(solution(Arrays.asList(2, 7, 0, 3, 4, 6, 1)) == 5 ? "OK" : "KO");
        System.out.println(solution(Arrays.asList(0, 1, 4, 3)) == 2 ? "OK" : "KO");
        System.out.println(solution(Arrays.asList(0, 1, 4, 2)) == 3 ? "OK" : "KO");
    }
}
