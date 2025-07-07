cd build
ctest
lcov --capture --directory . --output-file coverage.info
lcov --remove coverage.info '/usr/*' --output-file coverage_filtered.info
genhtml coverage_filtered.info --output-directory ../testgen/coverage
echo "Coverage report generated"