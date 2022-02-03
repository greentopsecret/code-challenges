package facebook;

import java.util.*;

class RevenueMilestones {
    int[] getMilestoneDays(int[] revenues, int[] milestones) {
        if (milestones.length == 0 || revenues.length == 0) {
            return new int[0];
        }

        int[] result = new int[milestones.length];
        Arrays.fill(result, -1);

        int[] aggregatedRevenues = new int[revenues.length];
        aggregatedRevenues[0] = revenues[0];
        for (int i = 1; i < revenues.length; i++) {
            aggregatedRevenues[i] = aggregatedRevenues[i - 1] + revenues[i];
        }

        for (int j = 0; j < milestones.length; j++) {
            int idx = Arrays.binarySearch(aggregatedRevenues, milestones[j]);
            if (idx >= 0 && aggregatedRevenues[idx] == milestones[j]) {
                idx++;
            }
            if (idx < 0) {
                idx = Math.abs(idx);
            }
            if (idx <= aggregatedRevenues.length) {
                result[j] = idx;
            }
        }

        return result;
    }

    int[] getMilestoneDaysPriorityQueue(int[] revenues, int[] milestones) {
        // https://leetcode.com/discuss/interview-question/1188322/Facebook-or-Recruiting-Portal-or-Revenue-Milestones/1112012

        int i = 0, j = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int x : milestones) {
            pq.add(new int[]{x, i});
            i++;
        }
        i = 0;
        int n = revenues.length, m = milestones.length;
        int[] res = new int[m];
        int sum = 0;
        while (i < n && !pq.isEmpty()) {
            sum += revenues[i];
            while (!pq.isEmpty() && sum >= pq.peek()[0]) {
                res[pq.poll()[1]] = i + 1;
            }
            i++;
        }
        while (!pq.isEmpty()) {
            res[pq.poll()[1]] = -1;
        }
        return res;
    }

    int[] getMilestoneDaysBruteforce(int[] revenues, int[] milestones) {
        if (milestones.length == 0 || revenues.length == 0) {
            return new int[0];
        }

        int[] result = new int[milestones.length];
        Arrays.fill(result, -1);

        int total = 0;
        for (int i = 0; i < revenues.length; i++) {
            total += revenues[i];
            for (int j = 0; j < milestones.length; j++) {
                if (total >= milestones[j] && result[j] == -1) {
                    result[j] = i + 1;
                }
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
        int[] revenues_1 = {100, 200, 300, 400, 500};
        int[] milestones_1 = {300, 800, 1000, 1400};
        int[] expected_1 = {2, 4, 4, 5};
        int[] output_1 = getMilestoneDays(revenues_1, milestones_1);
        check(expected_1, output_1);

        int[] revenues_2 = {700, 800, 600, 400, 600, 700};
        int[] milestones_2 = {3100, 2200, 800, 2100, 1000};
        int[] expected_2 = {5, 4, 2, 3, 2};
        check(expected_2, getMilestoneDays(revenues_2, milestones_2));

        int[] revenues_3 = {700, 800, 600, 400, 600, 700};
        int[] milestones_3 = {};
        int[] expected_3 = {};
        check(expected_3, getMilestoneDays(revenues_3, milestones_3));

        int[] revenues_4 = {};
        int[] milestones_4 = {100};
        int[] expected_4 = {};
        check(expected_4, getMilestoneDays(revenues_4, milestones_4));

        int[] revenues_5 = {700, 800, 600, 400, 600, 700};
        int[] milestones_5 = {3100, 2200, 800, 21000, 1000};
        int[] expected_5 = {5, 4, 2, -1, 2};
        check(expected_5, getMilestoneDays(revenues_5, milestones_5));
    }

    public static void main(String[] args) {
        new RevenueMilestones().run();
    }
}