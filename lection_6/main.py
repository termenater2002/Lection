import time
from functools import lru_cache

@lru_cache()
def main():
    time.sleep(1.1)
    print("Hello from lection-6!")

for i in range(1000):
    if __name__ == "__main__":
        main()
