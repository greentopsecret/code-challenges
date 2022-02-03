package crackingTheCodingInterview.exercise_7_2_call_center;

import java.util.LinkedList;
import java.util.Queue;

public class CallCenter implements CallsListener {
    private final Queue<Employee> availableResponders;
    private final Queue<Employee> availableManagers;
    private final Queue<Employee> availableDirectors;

    private Queue<Call> callQueue;

    public CallCenter() {
        availableResponders = new LinkedList<>();
        availableManagers = new LinkedList<>();
        availableDirectors = new LinkedList<>();
        callQueue = new LinkedList<>();
    }

    public void add(Employee e) {
        makeAvailable(e);
    }

    public void dispatchCall(Call call) {
        Employee employee = allocate(call);
        call.setCallsListener(this);

        if (employee == null) {
            System.out.printf("Call %d: No employee can respond to a call. Put call on hold.\n", call.getId());
            callQueue.add(call);
            return;
        }

        System.out.printf("Call %d: %s (%s) is responsible for a call.\n", call.getId(), employee.getName(), employee.getRole());
        call.setEmployee(employee);
    }

    public void onCallEnds(Call call) {
        System.out.printf("Call %d: end\n", call.getId());
        Employee employee = call.getEmployee();
        if (employee != null) {
            makeAvailable(employee);
            System.out.printf("Call %d: %s (%s) is available for new calls\n", call.getId(), employee.getName(), employee.getRole());
            if (callQueue.size() > 0) {
                dispatchCall(callQueue.poll());
            }
        } else {
            System.out.printf("Call %d: Call is finished without being responded\n", call.getId());
        }
    }

    private void makeAvailable(Employee e) {
        if (e instanceof Responder) {
            availableResponders.add(e);
        } else if (e instanceof Manager) {
            availableManagers.add(e);
        } else {
            availableDirectors.add(e);
        }
    }

    private Employee allocate(Call call) {
        if (availableResponders.size() > 0) {
            Employee employee = availableResponders.poll();
            if (employee.canHandleCall(call)) {
                return employee;
            }
            availableResponders.add(employee);
        }
        if (availableManagers.size() > 0) {
            Employee manager = availableManagers.poll();
            if (manager.canHandleCall(call)) {
                return manager;
            }
            availableResponders.add(manager);
        }

        if (availableDirectors.size() > 0) {
            return availableDirectors.poll();
        }

        return null;
    }

    public static void main(String[] args) {
        Employee employee1 = new Responder("Responder #1");
        Employee employee2 = new Responder("Responder #2");
        Employee employee3 = new Responder("Responder #3");
        Employee manager1 = new Manager("Manager #1");
        Employee manager2 = new Manager("Manager #2");
        Employee director = new Director("Director");

        CallCenter callCenter = new CallCenter();
        callCenter.add(employee1);
        callCenter.add(employee2);
        callCenter.add(employee3);
        callCenter.add(manager1);
        callCenter.add(manager2);
        callCenter.add(director);

        Call call1 = new Call(1);
        Call call2 = new Call(2);
        Call call3 = new Call(3);
        Call call4 = new Call(4);
        Call call5 = new Call(5);
        Call call6 = new Call(6);
        Call call7 = new Call(7);
        Call call8 = new Call(8);
        Call call9 = new Call(9);
        Call call10 = new Call(10);
        Call call11 = new Call(11);
        Call call12 = new Call(12);
        Call call13 = new Call(13);
        Call call14 = new Call(14);

        callCenter.dispatchCall(call1);
        callCenter.dispatchCall(call2);
        callCenter.dispatchCall(call3);
        callCenter.dispatchCall(call4);
        callCenter.dispatchCall(call5);
        callCenter.dispatchCall(call6);
        callCenter.dispatchCall(call7);
        callCenter.dispatchCall(call8);
        callCenter.dispatchCall(call9);

        call4.endCall();
        callCenter.dispatchCall(call10);
        call5.endCall();
        callCenter.dispatchCall(call11);
        callCenter.dispatchCall(call12);
        call6.endCall();
        call7.endCall();
        callCenter.dispatchCall(call13);
        callCenter.dispatchCall(call14);
    }
}
