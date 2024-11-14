# prompt: create a compTIA+ troubleshooting playbook

import pandas as pd

# Create a Pandas DataFrame to represent the troubleshooting playbook.
# Columns represent troubleshooting steps, and rows represent specific issues.

data = {
    'Issue': [
        'No Internet Connectivity',
        'Slow Internet Speed',
        'Computer Won\'t Boot',
        'Blue Screen of Death (BSOD)',
        'Printer Not Working',
        'Software Not Installing',
        'Hardware Malfunction'
    ],
    'Step 1': [
        'Check physical connections (cables, modem, router).',
        'Run a speed test.',
        'Check power supply and connections.',
        'Check event viewer for error messages.',
        'Check printer power and connections.',
        'Check system requirements.',
        'Inspect hardware for visible damage.'
    ],
    'Step 2': [
        'Restart modem and router.',
        'Check for network congestion.',
        'Try booting from a different media (USB/DVD).',
        'Identify the stop code and search for solutions.',
        'Check printer drivers and software.',
        'Run a disk cleanup.',
        'Try a different hardware component.'
    ],
    'Step 3': [
        'Check DNS settings.',
        'Check firewall settings.',
        'Check BIOS/UEFI settings.',
        'Check for hardware conflicts in Device Manager.',
        'Check printer settings and configuration.',
        'Check for sufficient disk space.',
        'If possible, replace the faulty hardware.'
    ],
    'Step 4': [
        'Contact your ISP.',
        'Try a different browser or device.',
        'Reinstall the operating system.',
        'Update drivers and BIOS.',
        'Run the printer troubleshooter.',
        'Reinstall or repair the software.',
        'Consult a hardware repair specialist.'
    ]
}


playbook = pd.DataFrame(data)

# Function to search the playbook for a given issue
def troubleshoot_issue(issue):
    if issue in playbook['Issue'].values:
        return playbook[playbook['Issue'] == issue]
    else:
        return "Issue not found in the playbook."

# Example usage:
print(troubleshoot_issue('No Internet Connectivity'))
