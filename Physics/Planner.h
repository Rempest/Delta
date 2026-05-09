#pragma once
#include "State.h"

class Planner {
public:
    explicit Planner(double target_x = 10.0, double gain = 0.5)
        : target_x_(target_x), gain_(gain) {}

    double computeTargetVelocity(const State& state) const {
        return (target_x_ - state.x) * gain_;
    }

    void setTarget(double x) { target_x_ = x; }

private:
    double target_x_;
    double gain_;
};