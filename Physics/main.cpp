#include <iostream>
#include "State.h"
#include "Dynamics.h"
#include "PID.h"
#include "Planner.h"
#include "Sensors.h"

using namespace std;

int main() {

    State state;
    Dynamics dynamics;
    PID pid(2.0, 0.0, 0.5);
    Planner planner;
    Sensors sensors;

    double dt = 0.1;

    for (int i = 0; i < 100; i++) {

        double target_velocity;

        if (sensors.isObstacleClose()) {
            target_velocity = 0;
            cout << "STOP\n";
        } else {
            target_velocity = planner.computeTargetVelocity(state);
        }

        double thrust = pid.update(target_velocity, state.v, dt);

        state.a = dynamics.computeAcceleration(thrust, state.v);

        state.v += state.a * dt;
        state.x += state.v * dt;

        cout << "x: " << state.x
             << " v: " << state.v
             << " a: " << state.a
             << endl;
    }

    return 0;
}