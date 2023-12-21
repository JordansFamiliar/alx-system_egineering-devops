POSTMORTEM

Issue Summary

The outage occurred from January 15, 2023, 03:45 AM to 07:30 AM (UTC), affecting the authentication service. Approximately 30% of users were unable to log in during this period.

Timeline

03:45 AM (UTC): The issue was detected at 03:45 AM (UTC) through automated monitoring alerts, triggered by a significant increase in failed authentication attempts.
Detection Method: An incident response team initiated an investigation, assuming initially a potential DDoS attack or elevated traffic.

Actions Taken

Misleading investigative paths included exploring a DDoS attack and investigating a database overload hypothesis.
The incident was escalated to the System Reliability Engineering (SRE) team for expert intervention.

Resolution

Root Cause:The misconfigured firewall rule unintentionally blocked legitimate authentication requests, disrupting the service.
Resolution: The firewall rule was promptly corrected, allowing normal service restoration by 07:30 AM (UTC).

Root Cause and Resolution

The resolution involved identifying and correcting the misconfiguration and conducting a comprehensive review of firewall configurations for other services.

Corrective and Preventative Measures

To enhance future incident response, monitoring for firewall configurations will be strengthened.
Automated testing for critical service components during routine maintenance will be implemented, along with improved documentation for firewall rule changes.

Specific Tasks

Implement real-time alerts for firewall misconfigurations.
Develop and deploy automated tests for critical service components.
Review and update documentation related to firewall rule changes.
Conduct a comprehensive review of all firewall rules.
Schedule regular training sessions for the operations team on best practices for firewall management.
