def main() -> None:
    print("=== Game Analytics Dashboard ===")

    # sample data
    players = [
        {"name": "alice", "score": 2300, "achievements": [
            "first_kill", "level_10", "boss_slayer"],
            "region": "north", "active": True},
        {"name": "bob", "score": 1800, "achievements": [
            "first_kill", "level_5"], "region": "east", "active": True},
        {"name": "charlie", "score": 2150, "achievements": [
            "level_10", "boss_slayer", "collector"],
            "region": "central", "active": True},
        {"name": "diana", "score": 1500, "achievements": [
            "first_kill"], "region": "north", "active": False},
    ]
    # List Data
    print("\n=== List Comprehension Examples ===")

    # High scores
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print("High scoreres (>2000):", high_scorers)

    # Scorers doubled
    doubled_scorers = [p["score"] * 2 for p in players]

    print("Scores Doubled:", doubled_scorers)

    # Active players
    active_players = [p["name"] for p in players if p["active"]]
    print("Active players:", active_players)

    # List Dict Data

    print("\n=== Dict Comprehension Examples ===")

    # Player scoreres mapping
    player_score = {p["name"]: ["score"] for p in players}
    print("Players scores:", player_score)

    # Score Categories
    score_categories = {
        "high": len([p for p in players if p["score"] > 2000]),
        "medium": len([p for p in players if 1600 <= p["score"] <= 2000]),
        "low": len([p for p in players if p["score"] < 1600]),
    }
    print("Score categories:", score_categories)

    # Achievments counts per player
    achievements_counts = {p["name"]: len(p["achievements"]) for p in players}
    print("Achievement counts:", achievements_counts)

    # Print Out Comperhension Examples

    print("\n=== Set Comprehension Examples ===")

    # Unique Players
    unique_players = {p["name"] for p in players}
    print("Unique players:", unique_players)

    # Unique Achievements
    unique_achivs = {ach for p in players for ach in p["achievements"]}

    print("Unique achievements:", unique_achivs)

    # Active regions
    active_regions = {p["region"] for p in players if p["region"]}
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    total_unique_ach = len(unique_achivs)
    avg_score = sum(p["score"] for p in players) / total_players
    top_player = max(players, key=lambda p: p["score"])

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_ach)
    print("Average score:", avg_score)
    print(f"Top performer: {top_player['name']}"
          f" ({top_player['score']} points, "
          f"{len(top_player['achievements'])} achievements)")


if __name__ == "__main__":
    main()
