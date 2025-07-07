#include "ProjectController.h"
#include <iostream>

ProjectController::ProjectController() {}

void ProjectController::createProject(const std::string& title) {
    std::cout << "Creating project: " << title << std::endl;
}

void ProjectController::assignProject(int employeeId, int projectId) {
    std::cout << "Assigning project " << projectId << " to employee " << employeeId << std::endl;
}

void ProjectController::deleteProject(int projectId) {
    std::cout << "Deleting project with ID: " << projectId << std::endl;
}

void ProjectController::updateProject(int projectId, const std::string& title) {
    std::cout << "Updating project " << projectId << " to title: " << title << std::endl;
}

std::vector<std::string> ProjectController::listProjects() {
    return {"Website Redesign", "Mobile App", "Database Optimization"};
}
