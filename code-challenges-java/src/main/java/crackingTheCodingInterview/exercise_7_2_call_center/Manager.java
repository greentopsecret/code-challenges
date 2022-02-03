package crackingTheCodingInterview.exercise_7_2_call_center;

public class Manager extends AbstractEmployee {
    private String name;

    public Manager(String name) {
        super(name);
    }

    @Override
    public Role getRole() {
        return Role.MANAGER;
    }
}
