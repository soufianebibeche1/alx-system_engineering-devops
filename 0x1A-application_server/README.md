# Project: 0x1A. Application server

## Description
This project aims to enhance the existing web infrastructure by incorporating an application server to serve dynamic content alongside Nginx. The task involves integrating the application server with Nginx and configuring it to serve an Airbnb clone project.

## Concepts
- Web Server
- Server
- Web stack debugging

## Background Context
The web infrastructure is currently serving web pages via Nginx. The addition of an application server will enable serving dynamic content efficiently.

## Resources
- [Application server vs web server](https://intranet.alxswe.com/rltoken/B9fOBzIxX_t1289WAuRzJw)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.alxswe.com/rltoken/kpG6RwmwRJHzRmGUM_ERcA)
- [Running Gunicorn](https://intranet.alxswe.com/rltoken/2LF1j7xKJGYaUtD1HKgUeQ)
- [Be careful with the way Flask manages slash in route - strict_slashes](https://intranet.alxswe.com/rltoken/zTCSTQxrH2za4hxbkt8K3g)
- [Upstart documentation](https://intranet.alxswe.com/rltoken/cldrneY3Qr7LlDysygzRHw)

## Requirements
### General
- README.md file with project details.
- Python-related tasks should use python3.
- All config files must have comments.

### Bash Scripts
- Interpreted on Ubuntu 16.04 LTS.
- End files with a newline.
- Scripts must be executable.
- Pass Shellcheck without errors.
- First line: #!/usr/bin/env bash
- Second line: Description of the script's purpose.

### Servers
| Name           | Username | IP            | State   |
|----------------|----------|---------------|---------|
| 439916-web-01  | ubuntu   | 54.236.12.178 | running |
| 439916-web-02  | ubuntu   | 54.226.35.202 | running |
| 439916-lb-01   | ubuntu   | 54.236.46.80  | running |

## Project Timeline
- Start: Mar 11, 2024 3:00 AM
- End: Mar 15, 2024 3:00 AM
- Checker Release: Mar 13, 2024 5:24 PM
- Auto Review at Deadline
