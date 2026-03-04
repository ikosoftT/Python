import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    arch_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input(
        "Input Stream active. Enter status report: ")
    success_msg = "Communication channels verified"

    sys.stdout.write(
        f"\n[STANDARD] Archive status from {arch_id}: {status_report}\n")
    sys.stderr.write(f"[ALERT] System diagnostic: {success_msg}\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    try:
        main()
    except (Exception, KeyboardInterrupt) as e:
        print(f"ERROR: {e}")
