import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class TmpTest {
    @Test
    void tmp() {
        Assertions.assertFalse(false);
    }

    @Test
    void givenEvenNumber_whenCheckingIsNumberEven_thenTrue() {
        Tmp obj = new Tmp();
        boolean result = obj.isNumberEven(8);

        Assertions.assertTrue(result);
    }

    @Test
    void givenOddNumber_whenCheckingIsNumberEven_thenFalse() {
        Tmp obj = new Tmp();
        boolean result = obj.isNumberEven(3);

        Assertions.assertFalse(result);
    }
}
