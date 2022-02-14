def printRoute(from_to):
    to_from = {}
    for k, v in from_to.items():
        to_from[v] = k

    start_city = None
    for key in from_to:
        if key not in to_from:
            start_city = key

    while(True):
        if from_to[start_city] in from_to:
            print(f"{start_city} -> {from_to[start_city]}")
            start_city = from_to[start_city]
        else:
            print(f"{start_city} -> {from_to[start_city]}")
            break


def main():
    from_to = {
        "Delhi": "Agra",
        "Ranthambor": "Jaipur",
        "Jaipur": "Mumbai",
        "Agra": "Ranthambor"
    }
    printRoute(from_to)


if __name__ == '__main__':
    main()
