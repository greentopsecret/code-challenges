package crackingTheCodingInterview.chapter8;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class SolutionsTest {
    @Test
    public void permutations_8_7() {
        assertEquals(List.of(), Permutations_8_7.solution(""));
        assertEquals(List.of("a"), Permutations_8_7.solution("a"));
        assertEquals(List.of("ab", "ba"), Permutations_8_7.solution("ab"));
        assertEquals(List.of("abc", "bac", "bac", "bca", "cab", "cba"), Permutations_8_7.solution("abc"));
    }
}
