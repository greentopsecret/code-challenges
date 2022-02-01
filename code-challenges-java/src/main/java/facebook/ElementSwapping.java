package facebook;

import java.util.*;

class ElementSwapping {

    int[] findMinArray(int[] arr, int k) {
        if (arr.length == 0 || k == 0) {
            return arr;
        }

        int l = 0;
        while (k > 0) {
            int minIdx = l;
            int tmpK = k;
            for (int i = l + 1; i < arr.length && tmpK > 0; i++) {
                if (arr[i] < arr[i - 1]) {
                    minIdx = arr[i] < arr[minIdx] ? i : minIdx;
                }
                tmpK--;
            }
            if (minIdx == l) { // all elements that we can swap are in ascending order
                l++;
                continue;
            }
            int steps = Math.min(minIdx - l, k);
            swap(arr, minIdx, steps);
            k -= steps;
            l++;
        }

        return arr;
    }

    private void swap(int[] arr, int i, int steps) {
        for (; steps > 0 && i > 0; steps--, i--) {
            int tmp = arr[i];
            arr[i] = arr[i - 1];
            arr[i - 1] = tmp;
        }
    }


    // These are the tests we use to determine if the solution is correct.
    // You can add your own at the bottom.
    int test_case_number = 1;

    void check(int[] expected, int[] output) {
        int expected_size = expected.length;
        int output_size = output.length;
        boolean result = true;
        if (expected_size != output_size) {
            result = false;
        }
        for (int i = 0; i < Math.min(expected_size, output_size); i++) {
            result &= (output[i] == expected[i]);
        }
        char rightTick = '\u2713';
        char wrongTick = '\u2717';
        if (result) {
            System.out.println(rightTick + " Test #" + test_case_number);
        } else {
            System.out.print(wrongTick + " Test #" + test_case_number + ": Expected ");
            printIntegerArray(expected);
            System.out.print(" Your output: ");
            printIntegerArray(output);
            System.out.println();
        }
        test_case_number++;
    }

    void printIntegerArray(int[] arr) {
        int len = arr.length;
        System.out.print("[");
        for (int i = 0; i < len; i++) {
            if (i != 0) {
                System.out.print(", ");
            }
            System.out.print(arr[i]);
        }
        System.out.print("]");
    }

    public void run() {
        int k_1 = 2;
        int[] arr_1 = {5, 3, 1};
        int[] expected_1 = {1, 5, 3};
        int[] output_1 = findMinArray(arr_1, k_1);
        check(expected_1, output_1);

        int[] arr_2 = {8, 9, 11, 2, 1};
        int[] expected_2 = {2, 8, 9, 11, 1};
        check(expected_2, findMinArray(arr_2, 3));

        int[] arr_3 = {8, 9, 11, 2, 1};
        int[] expected_3 = {1, 8, 9, 11, 2};
        check(expected_3, findMinArray(arr_3, 4));

        int[] arr_4 = {8, 9, 11, 2, 1};
        int[] expected_4 = {1, 8, 2, 9, 11};
        check(expected_4, findMinArray(arr_4, 6));

        int[] arr_5 = {8, 9, 11, 2, 1};
        int[] expected_5 = {1, 8, 9, 2, 11};
        check(expected_5, findMinArray(arr_5, 5));

        int[] arr_6 = {9, 8, 11, 2, 1};
        int[] expected_6 = {1, 8, 9, 11, 2};
        check(expected_6, findMinArray(arr_6, 5));

        int[] arr_7 = {9, 8, 11, 2, 1};
        int[] expected_7 = {9, 8, 11, 2, 1};
        check(expected_7, findMinArray(arr_7, 0));

        int[] arr_8 = {};
        int[] expected_8 = {};
        check(expected_8, findMinArray(arr_8, 3));

        int[] arr_9 = {8, 9, 2, 11, 1};
        int[] expected_9 = {2, 8, 9, 1, 11};
        check(expected_9, findMinArray(arr_9, 3));

        int[] arr_10 = {9, 8, 11, 1};
        int[] expected_10 = {8, 9, 11, 1};
        check(expected_10, findMinArray(arr_10, 1));

        int[] arr_11 = {9, 11, 8, 1};
        int[] expected_11 = {9, 8, 11, 1};
        check(expected_11, findMinArray(arr_11, 1));

        int[] arr_12 = {1, 2, 3, 4};
        int[] expected_12 = {1, 2, 3, 4};
        check(expected_12, findMinArray(arr_12, 1));

        int[] arr_13 = {5, 6, 7, 8, 9, 4, 5, 6, 7, 3, 8, 9, 10, 11};
        int[] expected_13 = {3, 5, 6, 7, 8, 4, 9, 5, 6, 7, 8, 9, 10, 11};
        check(expected_13, findMinArray(arr_13, 10));
    }

    public static void main(String[] args) {
        new ElementSwapping().run();
    }
}