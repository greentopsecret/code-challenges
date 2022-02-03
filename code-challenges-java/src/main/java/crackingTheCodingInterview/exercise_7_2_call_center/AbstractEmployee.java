package crackingTheCodingInterview.exercise_7_2_call_center;

import java.util.Random;

abstract public class AbstractEmployee implements Employee {
    private String name;

    public AbstractEmployee(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public boolean canHandleCall(Call call) {
        boolean result = (new Random()).nextInt(2) == 1;
        if (!result) {
            System.out.printf("Call %d: %s (%s) cannot answer the call\n", call.getId(), this.getName(), this.getRole());
        }
        return result;
    }
}
