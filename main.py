import os

TEXT = (
    "Evening settles over the tide flats, and the water comes back in, "
    "slow as a thought you do not have to finish. Far above, light that "
    "left its star before anyone alive was born is still falling toward "
    "the sea. It will arrive tonight, and the sea will hold it a while."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} code points to /output/entry.txt")


if __name__ == "__main__":
    main()
