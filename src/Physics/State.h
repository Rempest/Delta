#pragma once

struct State {
    double x = 0;
    double v = 0;
    double a = 0;

    void reset() { x = 0; v = 0; a = 0; }
};
