import pandas as pd


def summarize_scores(records):
    df = pd.DataFrame(records)
    average_score = df["Score"].mean()
    top_module = df.loc[df["Score"].idxmax(), "Module"]

    print("--- Moringa Data Science Progress ---")
    print(df.to_string(index=False))
    print(f"\nAverage Score: {average_score:.1f}%")
    print(f"Top Module: {top_module}")


if __name__ == "__main__":
    moringa_progress = [
        {"Module": "Python Fundamentals", "Score": 92},
        {"Module": "Git & GitHub", "Score": 95},
        {"Module": "Pandas & Data Cleaning", "Score": 88},
        {"Module": "Data Visualization", "Score": 90},
    ]
    summarize_scores(moringa_progress)
