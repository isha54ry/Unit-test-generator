# CMake generated Testfile for 
# Source directory: C:/orgChartApi
# Build directory: C:/orgChartApi/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(DepartmentTests "C:/orgChartApi/build/test_runner.exe")
set_tests_properties(DepartmentTests PROPERTIES  _BACKTRACE_TRIPLES "C:/orgChartApi/CMakeLists.txt;25;add_test;C:/orgChartApi/CMakeLists.txt;0;")
subdirs("googletest")
