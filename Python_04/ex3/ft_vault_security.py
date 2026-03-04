def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file_secure_protocol = "../security_protocols.txt"
    file_name = "../classified_data.txt"
    file_secure_protocol_content = None
    file_content = None
    try:
        with open(file_name, 'r') as file_obj:
            file_content = file_obj.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            "ERROR: Storage vault not found. Run data generator first.")
    if file_content:
        print("Initiating secure vault access...\n",
              "Vault connection established with failsafe protocols\n", sep='')
        print("SECURE EXTRACTION:")
        print(file_content)
    try:
        with open(file_secure_protocol, 'r') as f:
            file_secure_protocol_content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            "ERROR: Storage vault not found. Run data generator first.")
    if file_secure_protocol_content:
        print("\nSECURE PRESERVATION:")
        print(file_secure_protocol_content)
        print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
