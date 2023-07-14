This repository contains the solutions for the given tasks related to Liferay.

Task 4 - Folder 'first'
The 'first' folder includes all the necessary files to accomplish Task 4. In this task, a web server is set up to listen on port 5000. The container creation time is displayed, and it allows users to upload an image, which is then resized and rendered along with additional miscellaneous information.

Task 5 - Folder 'second'
The 'second' folder provides the solution for Task 5. Instead of building a new image that contains the required configuration, an entrypoint script is created. This script modifies the necessary configurations for load balancing to work properly.

Additional Notes
Due to time constraints during my holiday week, the demo might not be as visually polished as desired. Regarding the environment setup, my plan was to create a Terraform file that could create the environment (QEMU VM) either from a pre-built image using Hashicorp Packer or by setting up the box with the required software using Ansible. I have already prepared the necessary secrets in my self-hosted Vaultwarden (a Bitwarden-compatible secret manager) and could have implemented a GitHub Actions CI/CD pipeline for my solutions.