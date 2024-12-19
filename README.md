# Sample Python/Django Project

## Overview

This project transforms the thesis project management system at Tribhuvan University into a dynamic web application using Django, enhancing collaboration and efficiency for all teachers and students.

## Current System

The current thesis project management process involves:

- Emailing and updating spreadsheets for thesis topics.
- Manual email exchanges for topic selection and supervisor approvals.
- Submitting signed supervision agreements via Learnline.

## Pain Points

The current system has several key pain points:

1. **Inefficient Workflow**: Manual processes are repetitive and error-prone.
2. **Supervisor Capacity Blind Spot**: Students often face disappointments due to hidden limitations in supervisor capacity.
3. **Form Errors and Delays**: Frequent errors in standard forms require time-consuming corrections.
4. **Manual Data Management**: Redundant updates and double data entry create unnecessary complexity.

## Key Functionalities

1. **Enhanced Efficiency**: Centralized workflows and automation reduce manual tasks and errors.
2. **Improved Communication**: A shared platform fosters transparent communication among all stakeholders.
3. **Accessibility**: The web-based application can be accessed from anywhere, anytime, on various devices.
4. **Data Integrity**: Secure data storage and access controls protect student and project information.

## Demo

https://github.com/user-attachments/assets/dc44dc16-8f2f-48dc-8d5e-23eb85cad44e

## 🚀 Getting Started

### Open Using Daytona

1. Install Daytona using the [guide](https://www.daytona.io/docs/installation/installation/).
2. Create the workspace:
   ```
   daytona create https://github.com/SusheelThapa/Project-Management
   ```
3. Start the application:
   ```
   python manage.py runserver
   ```

## Usage

Access the site at `http://127.0.0.1:8000` to explore project.
For interactive function, check out [here](#recommended-workflow).

## Credentials

For demonstration purposes, a list of credentials for accessing the system as different user roles (Coordinator, Supervisor, Student) is available in the [credentials file](CREDENTIALS.md).

## Recommended Workflow

1. **Coordinator Role**:

   - **Log in as Coordinator**: Access the system to oversee all project submissions. This role has the authority to review and make decisions on each project.
   - **Manage Projects**: Approve projects that meet the guidelines and reject those that don't, simulating real-world administrative decision-making.

2. **Supervisor Role**:

   - **Log in as Supervisor**: Enter the platform to manage your project contributions and view updates on the current status of all projects.
   - **Add New Projects**: Submit new project proposals, detailing requirements and expectations, which will be subject to Coordinator approval.
   - **Track Project Approvals**: Monitor the effects of Coordinator decisions on your submitted projects, which helps in planning future submissions and feedback.

3. **Student Role**:
   - **Log in as Student**: Engage with the system to explore and participate in available projects.
   - **Participate in Groups**: Create or join a group to collaborate on projects. This simulates team management and project application processes.
   - **Apply for Projects**: Once part of a group, apply for Coordinator-approved projects, allowing you to experience the application process and await selections.

## Contributing

Interested in contributing? Fork the project on GitHub, make your changes, and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
