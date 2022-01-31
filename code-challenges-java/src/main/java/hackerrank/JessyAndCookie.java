package hackerrank;

import java.util.*;

class JessyAndCookie {

    public static int solution(int k, List<Integer> cookies) {
        if (cookies.size() == 0) {
            return -1;
        }

        int cnt = 0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(cookies);
        while (minHeap.size() >= 2 && minHeap.peek() < k) {
            int v1 = minHeap.poll();
            int v2 = minHeap.poll();
            minHeap.add(v1 + 2 * v2);
            cnt++;
        }

        return minHeap.peek() >= k ? cnt : -1;
    }

    public static void main(String[] args) {
        int actual_result;
        int expected_result;

        expected_result = 4;
        actual_result = JessyAndCookie.solution(9, Arrays.asList(2, 7, 3, 6, 4, 6));
        System.out.println(actual_result == expected_result ? "OK" : "KO");

        expected_result = 2;
        actual_result = JessyAndCookie.solution(7, Arrays.asList(1, 2, 3, 9, 10, 12));
        System.out.println(actual_result == expected_result ? "OK" : "KO");
    }
}