package crackingTheCodingInterview.exercise_7_2_call_center;

public interface Employee {
    public Role getRole();

    public String getName();

    boolean canHandleCall(Call call);
}
