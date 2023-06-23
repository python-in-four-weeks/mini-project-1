from typing import TypedDict


class Account(TypedDict):
    customer_name: str
    balance: float


accounts: list[Account] = [
    {"customer_name": "Alice Smith", "balance": 50},
    {"customer_name": "Bob Jones", "balance": 200},
    {"customer_name": "Charlie Taylor", "balance": 100},
    {"customer_name": "David Brown", "balance": 70},
    {"customer_name": "Eve Williams", "balance": 20},
    {"customer_name": "Frank Wilson", "balance": 250},
    {"customer_name": "Grace Johnson", "balance": 150},
    {"customer_name": "Heidi Davies", "balance": 125},
    {"customer_name": "Ivan Patel", "balance": 175},
    {"customer_name": "Judy Robinson", "balance": 220},
    {"customer_name": "Mallory Wright", "balance": 30},
]


def get_queue_length() -> int:
    return 0


def serve_customers(customer_count: int) -> None:
    pass


if __name__ == "__main__":
    queue_length = get_queue_length()
    serve_customers(queue_length)
    print("Time for a break!")
