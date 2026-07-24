import argparse
import logging
from pathlib import Path


def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=log_dir / "app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="llm-internship-30days demo script"
    )

    parser.add_argument(
        "--name",
        type=str,
        default="Student",
        help="Your name"
    )

    parser.add_argument(
        "--days",
        type=int,
        default=30,
        help="Number of study days"
    )

    return parser.parse_args()


def main():
    setup_logging()
    args = parse_args()

    message = f"Hello {args.name}, welcome to llm-internship-30days!"
    plan = f"You will study for {args.days} days."

    print(message)
    print(plan)

    logging.info("Program started")
    logging.info("name=%s, days=%s", args.name, args.days)
    logging.info("Program finished")


if __name__ == "__main__":
    main()