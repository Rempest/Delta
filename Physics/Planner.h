#pragma once
#include "State.h"

class Planner {
public:
    double target_x = 10.0;

    double computeTargetVelocity(State& state) {
        double error = target_x - state.x;
        return error * 0.5;
    }
};