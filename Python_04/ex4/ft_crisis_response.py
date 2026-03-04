def handl_crisis(file_name: str) -> None:
    try:
        with open(file_name, "r") as file:
            data: str = file.read()
            print(f"SUCCESS: Archive recovered - ``{data}``")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stabilized")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files = ["../lost_archive.txt",
             "../classified_vault.txt",
             "../standard_archive.txt"]
    print(f"CRISIS ALERT: Attempting access to '{files[0]}'...")
    handl_crisis(files[0])

    print(f"\nCRISIS ALERT: Attempting access to '{files[1]}'...")
    handl_crisis(files[1])

    print(f"\nROUTINE ACCESS: Attempting access to '{files[2]}'...")
    handl_crisis(files[2])

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
