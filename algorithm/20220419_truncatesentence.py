def truncate_sentence(s: str, k: int) -> str:
    return " ".join(s.split()[:k])


if __name__ == '__main__':
    print(truncate_sentence("Hello how are you Contestant", 4))
