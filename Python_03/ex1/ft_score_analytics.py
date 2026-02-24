import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
    else:
        scores_list = []
        i = 1
        while i < len(sys.argv):
            try:
                conv = int(sys.argv[i])
            except ValueError as e:
                print(e)
            scores_list += [conv]
            i += 1
        print(f"Scores processed:{scores_list}")
        print(f"Total players: {i - 1}")
        print(f"Total Score: {sum(scores_list)}")
        print(f"Average score: {sum(scores_list) / i - 1:.1f}")
        print(f"High score: {max(scores_list)}")
        print(f"Low score: {min(scores_list)}")
        print(f"Score range: {max(scores_list) - min(scores_list)}")
