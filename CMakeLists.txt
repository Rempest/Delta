cmake_minimum_required(VERSION 3.15)
project(DeltaPrime VERSION 0.1.0 LANGUAGES CXX Python)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Build options
option(BUILD_PHYSICS_LIB "Build Physics library" ON)
option(BUILD_TESTS "Build tests" ON)
option(ENABLE_PYTHON_BINDINGS "Enable Python bindings" ON)

# Output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Add subdirectories
add_subdirectory(Physics)

if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()

# Install targets
install(TARGETS DeltaPhysics
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

# Print build info
message(STATUS "DeltaPrime Configuration:")
message(STATUS "  Physics Library: ${BUILD_PHYSICS_LIB}")
message(STATUS "  Tests: ${BUILD_TESTS}")
message(STATUS "  Python Bindings: ${ENABLE_PYTHON_BINDINGS}")
