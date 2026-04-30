#pragma once

class Dynamics {
public:
    double mass = 1.0;
    double drag_coeff = 0.1;

    double computeDrag(double v) {
        return drag_coeff * v * v;
    }

    double computeAcceleration(double thrust, double v) {
        double drag = computeDrag(v);
        double F = thrust - drag;
        return F / mass;
    }
};