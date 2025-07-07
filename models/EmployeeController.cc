#include "EmployeeController.h"
#include <iostream>

EmployeeController::EmployeeController() {}

void EmployeeController::addEmployee(const std::string& name) {
    std::cout << "Adding employee: " << name << std::endl;
}

void EmployeeController::removeEmployee(int id) {
    std::cout << "Removing employee with ID: " << id << std::endl;
}

void EmployeeController::updateEmployee(int id, const std::string& newName) {
    std::cout << "Updating employee " << id << " to name: " << newName << std::endl;
}

std::string EmployeeController::getEmployee(int id) {
    return "John Doe";
}