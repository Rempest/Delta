#pragma once

class Sensors {
public:
    double distance = 5.0;

    bool isObstacleClose() {
        return distance < 1.0;
    }
};