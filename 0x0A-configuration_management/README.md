# Configuration Management with Puppet

This repository demonstrates the use of Puppet for configuration management. The tasks performed include creating a file, installing a package, and executing a command.

## Task 0: Create a File

### Puppet Code: [0-create_a_file.pp](./0-create_a_file.pp)

This Puppet manifest creates a file in `/tmp` with specific permissions, owner, group, and content. It serves as an introduction to Puppet file management.

```bash
puppet apply 0-create_a_file.pp
```

## Task 1: Install a Package

### Puppet Code: [1-install_a_package.pp](./1-install_a_package.pp)

This Puppet code installs the Flask package from pip3, ensuring it's version 2.1.0. It also handles potential compatibility issues with the Werkzeug library.

```bash
puppet apply 1-install_a_package.pp
```
## Task 2: Execute a Command

### Puppet Code: [2-execute_a_command.pp](./2-execute_a_command.pp)

This Puppet manifest demonstrates using the `exec` resource to execute a command (`pkill`) to terminate a process named 'killmenow'.

```bash
puppet apply 2-execute_a_command.pp
```
# Key Concepts

## Puppet Resources

Puppet uses resources (e.g., `file`, `package`, `exec`) to manage different aspects of the system.

## Manifests

Puppet manifests are files containing Puppet code. They describe the desired state of the system.

## Exec Resource

The `exec` resource allows the execution of arbitrary commands on the system.

## Dependency Management

Puppet handles dependencies between resources, ensuring they are applied in the correct order.

## Puppet Apply

The `puppet apply` command is used to apply Puppet manifests and enforce the desired system state.

## Version Management

Puppet can manage the versions of packages, ensuring specific versions are installed.

