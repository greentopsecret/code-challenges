package crackingTheCodingInterview.exercise_7_2_call_center;

public class Responder extends AbstractEmployee {
    private String name;

    public Responder(String name) {
        super(name);
    }

    @Override
    public Role getRole() {
        return Role.RESPONDER;
    }
}
