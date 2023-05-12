import re

if __name__ == "__main__":
    title = input("Please provide a title: ")

    id = title.lower()
    id = re.sub(r'[^a-zA-Z\d\s:]', '', id)
    id = id.replace(' ', '-')

    print(f"Id: {id}")