#pragma once

class Sensors {
public:
    explicit Sensors(double threshold = 1.0)
        : threshold_(threshold), distance_(5.0) {}

    void setDistance(double d) { distance_ = d; }
    double getDistance() const { return distance_; }

    bool isObstacleClose() const {
        return distance_ < threshold_;
    }

private:
    double distance_;
    double threshold_;
};
