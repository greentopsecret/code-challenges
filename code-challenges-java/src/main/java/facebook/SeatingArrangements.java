package facebook;

import java.util.*;

class SeatingArrangements {

    int minOverallAwkwardness(int[] arr) {
        if (arr.length < 2) {
            return 0;
        }

        Arrays.sort(arr);

        int diff = arr[1] - arr[0];
        for (int i = 2; i < arr.length; i++) {
            diff = Math.max(arr[i] - arr[i - 2], diff);
        }

        return diff;
    }

    int test_case_number = 1;

    void check(int expected, int output) {
        boolean result = (expected == output);
        char rightTick = '\u2713';
        char wrongTick = '\u2717';
        if (result) {
            System.out.println(rightTick + " Test #" + test_case_number);
        } else {
            System.out.print(wrongTick + " Test #" + test_case_number + ": Expected ");
            printInteger(expected);
            System.out.print(" Your output: ");
            printInteger(output);
            System.out.println();
        }
        test_case_number++;
    }

    void printInteger(int n) {
        System.out.print("[" + n + "]");
    }

    public void run() {
        int[] arr_1 = {5, 10, 6, 8};
        int expected_1 = 4;
        int output_1 = minOverallAwkwardness(arr_1);
        check(expected_1, output_1);

        int[] arr_2 = {1, 2, 5, 3, 7};
        check(4, minOverallAwkwardness(arr_2));

        int[] arr_3 = {1, 2};
        check(1, minOverallAwkwardness(arr_3));

        int[] arr_4 = {1};
        check(0, minOverallAwkwardness(arr_4));
    }

    public static void main(String[] args) {
        new SeatingArrangements().run();
    }
}
