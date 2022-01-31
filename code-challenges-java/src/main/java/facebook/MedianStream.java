package facebook;

import java.io.*;
import java.util.*;
// Add any extra import statements you may need here


class MedianStream {

    // 2, 4, 7, 1, 5, 6
    // maxHeap: 2; minHeap: _                                   2
    // maxHeap: 2; minHeap: 4                                   3
    // maxHeap: 24; minHeap: 7                                  4
    // maxHeap: 124; minHeap: 7 -> maxHeap: 12; minHeap: 47     3
    // maxHeap: 12; minHeap: 457 -> maxHeap: 124; minHeap: 57   4
    // maxHeap: 124; minHeap: 567                               4


    int[] findMedian(int[] arr) {
        if (arr.length == 0) {
            return new int[0];
        }
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(arr.length / 2, Collections.reverseOrder());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(arr.length / 2);

        int[] result = new int[arr.length];

        result[0] = arr[0];
        maxHeap.add(arr[0]);

        for (int i = 1; i < arr.length; i++) {
            if (maxHeap.peek() >= arr[i]) {
                maxHeap.add(arr[i]);
            } else {
                minHeap.add(arr[i]);
            }

            if (minHeap.size() > maxHeap.size()) {
                maxHeap.add(minHeap.poll());
            } else if (maxHeap.size() > minHeap.size() + 1) {
                minHeap.add(maxHeap.poll());
            }

            if (maxHeap.size() > minHeap.size()) {
                result[i] = maxHeap.peek();
            } else {
                result[i] = Math.floorDiv(maxHeap.peek() + minHeap.peek(), 2);
            }
        }

        return result;
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
        int[] arr_1 = {5, 15, 1, 3};
        int[] expected_1 = {5, 10, 5, 4};
        int[] output_1 = findMedian(arr_1);
        check(expected_1, output_1);

        int[] arr_2 = {2, 4, 7, 1, 5, 3};
        int[] expected_2 = {2, 3, 4, 3, 4, 3};
        int[] output_2 = findMedian(arr_2);
        check(expected_2, output_2);

        int[] arr_3 = {2, 4, 7, 1, 5, 6};
        int[] expected_3 = {2, 3, 4, 3, 4, 4};
        int[] output_3 = findMedian(arr_3);
        check(expected_3, output_3);

        int[] arr_4 = {};
        int[] expected_4 = {};
        int[] output_4 = findMedian(arr_4);
        check(expected_4, output_4);

        // Add your own test cases here

    }

    public static void main(String[] args) {
        new MedianStream().run();
    }
}