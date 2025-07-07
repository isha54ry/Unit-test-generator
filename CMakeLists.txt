cmake_minimum_required(VERSION 3.14)
project(UnitTestGenerator)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} --coverage")

add_subdirectory(googletest)
enable_testing()

include_directories(models)

file(GLOB TEST_SOURCES "testgen/tests/*.cpp")
file(GLOB SRC_FILES "models/*.cc")

add_executable(test_runner ${TEST_SOURCES} ${SRC_FILES})

target_link_libraries(test_runner gtest gtest_main pthread)

add_test(NAME DepartmentTests COMMAND test_runner)
