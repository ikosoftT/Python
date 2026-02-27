
def main() -> None:

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}

    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}

    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    allUnique = alice.union(bob, charlie)

    total = len(allUnique)

    Common = alice.intersection(bob, charlie)

    RareAlice = alice.difference(bob, charlie)
    RareBob = bob.difference(alice, charlie)
    RareCharlie = charlie.difference(bob, alice)

    RareItems = RareAlice.union(RareBob, RareCharlie)

    AliceAndBobCommon = alice.intersection(bob)

    AliceUnique = alice.difference(bob)

    BobUnique = bob.difference(alice)

    print("=== Achievement Tracker System ===\n")

    print(f"Player alice achievments: {alice}")
    print(f"Player bob achievments: {bob}")
    print(f"Player charlie achievments: {charlie}\n")

    print("=== Achievement Analytics ===")

    print(f"All unique achievements: {allUnique}")

    print(f"Total unique achievements: {total}\n")

    print(f"Common to all players: {Common}")

    print(f"Rare achievements (1 player): {RareItems}\n")

    print(f"Alice vs Bob common: {AliceAndBobCommon}")

    print(f"Alice unique: {AliceUnique}")

    print(f"Bob unique: {BobUnique}")


if __name__ == "__main__":
    main()
