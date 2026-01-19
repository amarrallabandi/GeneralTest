import pandas as pd

def main():
    df = pd.DataFrame({
        "Name": ["Alice", "Bob"],
        "Age": [23,27]
    })

    print(df.Name[0])

if __name__ == "__main__":
    main()