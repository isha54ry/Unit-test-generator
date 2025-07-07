#include "DepartmentController.h"
#include <iostream>

DepartmentController::DepartmentController() {}

void DepartmentController::createDepartment(const std::string& name) {
    std::cout << "Creating department: " << name << std::endl;
}

void DepartmentController::deleteDepartment(int id) {
    std::cout << "Deleting department with ID: " << id << std::endl;
}

void DepartmentController::getDepartment(int id) {
    std::cout << "Fetching department with ID: " << id << std::endl;
}

void DepartmentController::updateDepartment(int id, const std::string& name) {
    std::cout << "Updating department " << id << " to name: " << name << std::endl;
}

std::vector<std::string> DepartmentController::listDepartments() {
    return {"HR", "Engineering", "Marketing"};
}
