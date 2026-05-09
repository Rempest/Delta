#pragma once
#include <stdexcept>
#include <algorithm>

class PID {
public:
    PID(double kp, double ki, double kd, double max_integral = 10.0)
        : kp_(kp), ki_(ki), kd_(kd),
          max_integral_(max_integral),
          prev_error_(0), integral_(0) {}

    double update(double target, double current, double dt) {
        if (dt <= 0)
            throw std::invalid_argument("dt must be positive");

        double error = target - current;

        integral_ += error * dt;
        // Anti-windup: ограничиваем интеграл
        integral_ = std::clamp(integral_, -max_integral_, max_integral_);

        double derivative = (error - prev_error_) / dt;
        prev_error_ = error;

        return kp_ * error + ki_ * integral_ + kd_ * derivative;
    }

    void reset() {
        prev_error_ = 0;
        integral_ = 0;
    }

private:
    double kp_, ki_, kd_;
    double max_integral_;
    double prev_error_;
    double integral_;
};