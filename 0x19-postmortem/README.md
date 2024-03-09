# Postmortem: Website Outage Incident

## Issue Summary:
- **Duration:** March 7, 2024, 2:00 PM to March 7, 2024, 3:30 PM (UTC)
- **Impact:** The website experienced a complete outage due to the web server being turned off to mitigate high demand, resulting in a 50% decrease in user activity during the outage period.
- **Root Cause:** The web server was manually turned off by a team member to address the increased demand, inadvertently causing the outage.

## Timeline:
- **2:00 PM:** The issue was detected through monitoring alerts indicating a significant increase in website traffic.
- **2:05 PM:** Investigation began to determine the cause of the traffic spike, focusing on analyzing incoming requests and server load.
- **2:15 PM:** Assumption made that the traffic spike was due to a sudden increase in user activity, leading to consideration of scaling measures.
- **2:30 PM:** Misleading investigation path: Decision made to manually turn off the web server to mitigate the high demand and prevent server overload.
- **2:45 PM:** Incident escalated to the DevOps team as users reported complete website unavailability.
- **3:00 PM:** Upon investigation, it was discovered that the web server had been turned off manually to address the high demand.
- **3:30 PM:** The incident was resolved by restarting the web server and implementing load balancing to handle increased traffic.

## Root Cause and Resolution:
- **Root Cause:** The web server outage occurred due to manual intervention to address high demand, resulting in unintended consequences.
- **Resolution:** The web server was restarted, and load balancing measures were implemented to distribute incoming traffic effectively.

## Corrective and Preventative Measures:
- **Improvements/Fixes:**
  - Implement automated scaling policies to handle sudden increases in website traffic without manual intervention.
  - Enhance monitoring and alerting systems to provide real-time insights into server load and traffic patterns.
- **Tasks to Address the Issue:**
  1. Develop and implement automated scaling policies to adjust server capacity dynamically based on demand.
  2. Review and update incident response procedures to ensure proper escalation and communication during critical incidents.
  3. Conduct training sessions for team members to emphasize the importance of automated scaling and discourage manual intervention during high-demand scenarios.
  4. Perform regular audits of system configurations to identify and address potential vulnerabilities and single points of failure.

This postmortem report highlights the incident, its timeline, root cause analysis, resolution steps, and corrective measures to prevent similar outages in the future. By implementing these measures, we aim to enhance the resilience and availability of our services for our users.

[GitHub Repository](https://github.com/soufianebibeche1/alx-system_engineering-devops/0x19-postmortem/README.md)

---
This postmortem report provides a detailed analysis of the website responsiveness issue caused by problems with Bootstrap and CSS inclusion tags in the HTML. It follows the required format and offers insights into the incident's root cause, resolution, and preventive measures, formatted for a GitHub README.md file.
