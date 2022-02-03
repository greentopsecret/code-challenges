package crackingTheCodingInterview.exercise_7_2_call_center;

public class Director extends AbstractEmployee {
    private String name;

    public Director(String name) {
        super(name);
    }

    @Override
    public Role getRole() {
        return Role.DIRECTOR;
    }
}
