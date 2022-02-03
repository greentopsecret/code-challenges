package crackingTheCodingInterview.exercise_7_2_call_center;

public class Call {

    CallsListener callCenter;
    private Integer id;
    private Employee employee;

    public Call(Integer id) {
        this.id = id;
    }

    public Integer getId() {
        return id;
    }

    public void endCall() {
        this.callCenter.onCallEnds(this);
    }

    void setCallsListener(CallCenter callCenter) {
        this.callCenter = callCenter;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

    public Employee getEmployee() {
        return this.employee;
    }
}
