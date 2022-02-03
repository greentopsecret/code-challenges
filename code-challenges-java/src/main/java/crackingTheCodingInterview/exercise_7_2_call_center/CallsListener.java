package crackingTheCodingInterview.exercise_7_2_call_center;

import java.util.EventListener;

public interface CallsListener extends EventListener {
    public void onCallEnds(Call call);
}
