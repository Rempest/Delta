#include <iostream>
#include <iomanip>
#include "State.h"
#include "Dynamics.h"
#include "PID.h"
#include "Planner.h"
#include "Distance.h"

int main() {
    try {
        State state;
        Dynamics dynamics(1.0, 0.1);
        PID pid(2.0, 0.0, 0.5);
        Planner planner(10.0);
        Sensors sensors(1.0);

        const double dt = 0.1;
        const int steps = 100;

        std::cout << std::fixed << std::setprecision(3);

        for (int i = 0; i < steps; i++) {
            double target_velocity;

            if (sensors.isObstacleClose()) {
                target_velocity = 0;
                std::cout << "STOP\n";
            } else {
                target_velocity = planner.computeTargetVelocity(state);
            }

            double thrust = pid.update(target_velocity, state.v, dt);
            state.a = dynamics.computeAcceleration(thrust, state.v);
            state.v += state.a * dt;
            state.x += state.v * dt;

            std::cout << "x: " << state.x
                      << " v: " << state.v
                      << " a: " << state.a << "\n";
        }

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
