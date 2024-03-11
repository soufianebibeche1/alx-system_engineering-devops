# Web Stack Debugging #4

## Description
This project focuses on debugging a web server setup featuring Nginx to handle high pressure and eliminate failed requests. The task involves identifying and resolving issues within the Nginx configuration to ensure the server can efficiently handle incoming requests.

## Requirements
- Ubuntu 14.04 LTS
- Puppet manifests must pass puppet-lint version 2.1.1 without errors
- Puppet manifests must run without errors
- Puppet manifests files must end with the extension .pp
- Puppet v3.4 will be used for checking
- Install puppet-lint:

	$ apt-get install -y ruby
	$ gem install puppet-lint -v 2.1.1

## File Structure

.
├── fix_nginx.sh
├── README.md
└── manifests
└── 0-the_sky_is_the_limit_not.pp


## Instructions
1. Clone this repository to your Ubuntu 14.04 LTS environment.
2. Ensure Puppet and puppet-lint are installed using the provided commands.
3. Review and debug the Nginx configuration in `0-the_sky_is_the_limit_not.pp`.
4. Execute puppet-lint to ensure compliance with standards: `puppet-lint --version 2.1.1 manifests/*.pp`
5. Apply the Puppet manifest using `puppet apply manifests/0-the_sky_is_the_limit_not.pp`.
6. Monitor the server's performance and ensure that failed requests are eliminated.

## Author
Sylvain Kalache, co-founder at Holberton School

This project is part of the curriculum for DevOps and SysAdmin tracks, focusing on scripting and debugging skills.
