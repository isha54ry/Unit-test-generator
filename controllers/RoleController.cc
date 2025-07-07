#include "RoleController.h"
#include <iostream>

RoleController::RoleController() {}

void RoleController::createRole(const std::string& role) {
    std::cout << "Creating role: " << role << std::endl;
}

void RoleController::deleteRole(int id) {
    std::cout << "Deleting role with ID: " << id << std::endl;
}

void RoleController::updateRole(int id, const std::string& role) {
    std::cout << "Updating role " << id << " to: " << role << std::endl;
}