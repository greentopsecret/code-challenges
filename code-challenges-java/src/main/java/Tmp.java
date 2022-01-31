public class Tmp {
    public boolean isNumberEven(Integer number) {
        return number % 2 == 0;
    }

    public static void main(String[] args) {
        for (long l = 79999000; l < 80000000; l++) {
            // convert cents-as-long to currency format
            String ls = String.format("%s.%02d", l / 100, l % 100);
            // convert string to float to currency
            String fs = String.format("%2.2f", Float.parseFloat(ls));
            if (!fs.equals(ls)) {
                System.out.println("Fail: float=" + fs + ", long=" + ls);
            }
        }
    }
}
