cmake_minimum_required(VERSION 3.15)
project(DeltaPhysics)

set(CMAKE_CXX_STANDARD 17)

add_library(DeltaPhysics INTERFACE)

target_include_directories(DeltaPhysics INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}
)

add_executable(DeltaPhysics_run Main.cpp)
