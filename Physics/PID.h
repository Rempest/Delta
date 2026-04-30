#pragma once

class PID {
private:
    double kp, ki, kd;
    double prev_error = 0;
    double integral = 0;

public:
    PID(double p, double i, double d)
        : kp(p), ki(i), kd(d) {}

    double update(double target, double current, double dt) {
        double error = target - current;

        integral += error * dt;
        double derivative = (error - prev_error) / dt;

        prev_error = error;

        return kp * error + ki * integral + kd * derivative;
    }
};