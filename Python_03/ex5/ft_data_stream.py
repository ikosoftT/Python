from typing import Generator
import time


def game_event_stream(n: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie", "david", "eve"]
    actions = ["Killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        event = {
            "id": i,
            "player": players[i % len(players)],
            "level": (i * 7) % 20 + 1,
            "action": actions[i % len(actions)]
        }
        yield event


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:
    print('=== Game Data Stream Processor ===\n')
    total_events = 1000
    print(f"Processing {total_events} game  events...\n")

    start_time = time.time()

    high_level = 0
    treasure_events = 0
    level_up_events = 0
    total_processed = 0
    for event in game_event_stream(total_events):
        total_processed += 1
        if total_processed <= 3:
            print(f"Event {event['id']}: Player {event['player']}"
                  f"(level {event['level']}) {event['action']}")
        if event['level'] >= 10:
            high_level += 1
        if event['action'] == "found treasure":
            treasure_events += 1
        if event['action'] == "leveled up":
            level_up_events += 1
    end_time = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    tmp: int = 0
    for i in fibonacci(10):
        tmp += 1
        if tmp < 10:
            print(i, end=", ")
        else:
            print(i, end='')
    print("\nPrime numbers (first 5): ", end="")
    tmp = 0
    for i in primes(5):
        tmp += 1
        if tmp < 5:
            print(i, end=', ')
        else:
            print(i, end='')


if __name__ == "__main__":
    main()
