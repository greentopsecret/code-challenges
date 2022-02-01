package facebook;

import java.io.*;
import java.util.*;
// Add any extra import statements you may need here


class SlowSums {

    // Add any helper functions you may need here


    int getTotalTime(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(arr.length, Collections.reverseOrder());
        for (int i: arr) {
            maxHeap.add(i);
        }

        int penalty = 0;
        while (maxHeap.size() > 1) {
            int sum = maxHeap.poll() + maxHeap.poll();
            maxHeap.add(sum);
            penalty += sum;
        }

        return penalty;
    }












    // These are the tests we use to determine if the solution is correct.
    // You can add your own at the bottom.
    int test_case_number = 1;
    void check(int expected, int output) {
        boolean result = (expected == output);
        char rightTick = '\u2713';
        char wrongTick = '\u2717';
        if (result) {
            System.out.println(rightTick + " Test #" + test_case_number);
        }
        else {
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
        int[] arr_1 = {4, 2, 1, 3};
        int expected_1 = 26;
        int output_1 = getTotalTime(arr_1);
        check(expected_1, output_1);

        int[] arr_2 = {2, 3, 9, 8, 4};
        int expected_2 = 88;
        int output_2 = getTotalTime(arr_2);
        check(expected_2, output_2);

        int[] arr_3 = {};
        int expected_3 = 0;
        int output_3 = getTotalTime(arr_3);
        check(expected_3, output_3);

        int[] arr_4 = {50};
        int expected_4 = 0;
        int output_4 = getTotalTime(arr_4);
        check(expected_4, output_4);

        // Add your own test cases here
    }
    public static void main(String[] args) {
        new SlowSums().run();
    }
}
