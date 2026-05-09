#pragma once
#include <stdexcept>

class Dynamics {
public:
    explicit Dynamics(double mass = 1.0, double drag_coeff = 0.1) {
        if (mass <= 0)
            throw std::invalid_argument("Mass must be positive");
        mass_ = mass;
        drag_coeff_ = drag_coeff;
    }

    double computeDrag(double v) const {
        return drag_coeff_ * v * v;
    }

    double computeAcceleration(double thrust, double v) const {
        return (thrust - computeDrag(v)) / mass_;
    }

private:
    double mass_;
    double drag_coeff_;
};