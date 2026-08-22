
# AutoDevOps

AutoDevOps is a Python-based Infrastructure as Code (IaC) automation tool that helps validate infrastructure configurations, generate Terraform and Ansible files, manage generated output, and provide basic infrastructure execution support through a CLI.

## Features

- YAML configuration loading
- Infrastructure configuration validation
- Configuration summary
- Terraform code generation
- Ansible code generation
- Terraform validation and planning
- Ansible connectivity and syntax checking
- Generated output management
- Project health check
- Structured execution results
- Logging
- Automated testing
- Command-line interface using Typer

## Project Structure


AutoDevOps/
├── cli/
│   ├── __init__.py
│   └── cli.py
│
├── parser/
│   ├── __init__.py
│   ├── yaml_parser.py
│   └── config_loader.py
│
├── schemas/
│   ├── __init__.py
│   └── validator.py
│
├── generators/
│   ├── __init__.py
│   ├── terraform_generator.py
│   └── ansible_generator.py
│
├── executor/
│   ├── __init__.py
│   ├── command_runner.py
│   ├── execution_result.py
│   ├── terraform_executor.py
│   └── ansible_executor.py
│
├── output/
│   └── output_manager.py
│
├── logs/
│   ├── deployment_manager.py
│   └── logger.py
│
├── examples/
│   └── sample.yaml
│
├── tests/
│   ├── test_validator.py
│   ├── test_generators.py
│   ├── test_executor.py
│   ├── test_logger.py
│   ├── test_cli.py
│   ├── test_deployment_manager.py
│   ├── test_execution_result.py
│   ├── test_config_loader.py
│   ├── test_output_manager.py
│   └── test_health_check.py
│
├── main.py
├── requirements.txt
└── README.md


## Technologies Used

- Python
- Typer
- PyYAML
- Jinja2
- Pydantic
- JSON Schema
- Terraform
- Ansible
- Pytest

## Configuration

Infrastructure configuration is provided using YAML files.

Example:

resources:
  - name: web-server
    type: web_server
    provider: aws

  - name: database
    type: database
    provider: aws

The sample configuration is available at:

examples/sample.yaml

## Workflow

YAML Configuration
        ↓
Configuration Loader
        ↓
Validation
        ↓
Configuration Summary
        ↓
Terraform / Ansible Generator
        ↓
Generated Output
        ↓
Terraform / Ansible Executor
        ↓
Execution Result
        ↓
Logging

Output Management

Generated infrastructure files are stored inside:

output/
├── terraform/
└── ansible/

The "OutputManager" provides functionality to:

- Create target directories
- List generated files
- Clear generated files

## Execution Handling

The project uses "CommandRunner" to execute infrastructure commands.

Every command produces an "ExecutionResult" containing:

- Return code
- Standard output
- Standard error
- Success status

This makes command execution easier to handle and maintain.

## Logging

AutoDevOps includes a logging system for important operations such as:

- Configuration validation
- IaC generation
- Terraform operations
- Ansible operations
- Deployment-related errors

## Project Goals

The main goals of AutoDevOps are:

1. Simplify infrastructure configuration.
2. Automate Infrastructure as Code generation.
3. Support Terraform and Ansible workflows.
4. Provide validation before execution.
5. Provide a simple command-line interface.
6. Make infrastructure automation easier to maintain.

## Version

AutoDevOps v1.0.0

## Author

### Aman Sharma



