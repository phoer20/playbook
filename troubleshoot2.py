def comptia_troubleshooting_playbook():
    """
    A simple CompTIA+ troubleshooting playbook.
    """

    print("Welcome to the CompTIA+ Troubleshooting Playbook!")
    problem_description = input("Describe the problem you are experiencing: ")

    # Basic troubleshooting steps (expand as needed)
    print("\nInitial Troubleshooting Steps:")
    print("1. Identify the problem: Is it hardware, software, network, or user-related?")
    print("2. Isolate the problem: Can you reproduce the issue? What steps lead to it?")
    print("3. Gather information: Check event logs, error messages, device manager.")

    # Example of conditional troubleshooting based on keyword detection
    if "network" in problem_description.lower():
        print("\nNetwork Troubleshooting:")
        print("- Check network cables and connections.")
        print("- Restart your network devices (router, modem).")
        print("- Verify network settings (IP address, subnet mask, DNS).")
        print("- Test network connectivity with ping and other network tools.")
    elif "hardware" in problem_description.lower():
        print("\nHardware Troubleshooting:")
        print("- Check device connections.")
        print("- Inspect cables and ports for damage.")
        print("- Try different ports/cables.")
        print("- Check for physical damage to hardware components.")
        print("- Listen for unusual noises.")
    elif "software" in problem_description.lower():
        print("\nSoftware Troubleshooting:")
        print("- Check for updates.")
        print("- Run antivirus scans.")
        print("- Check event logs for errors.")
        print("- Try system restore.")
        print("- Try reinstalling the software.")
    elif "user" in problem_description.lower():
        print("\nUser Troubleshooting:")
        print("- Verify user permissions and access rights.")
        print("- Check the user's knowledge and experience.")
        print("- Provide clear instructions.")
        print("- Try a different user account.")
    elif "internet" in problem_description.lower():
        print("\nInternet Troubleshooting:")
        print("- Check the internet connectivity by checking on another device.")
        print("- Check modem and router lights for issues.")
        print("- Restart the modem and router.")
        print("- Contact internet service provider if necessary.")
    else:
        print("\nGeneral Troubleshooting:")
        print("Try the following steps:")
        print("- Restart the computer or device.")
        print("- Check device manager for errors.")
        print("- Run system diagnostics tools.")


    # Further actions
    print("\nNext Steps:")
    print("1. If the problem persists, escalate to a senior technician.")
    print("2. Document all troubleshooting steps and outcomes.")
    print("3. Research similar issues online for solutions.")


if __name__ == "__main__":
    comptia_troubleshooting_playbook()
