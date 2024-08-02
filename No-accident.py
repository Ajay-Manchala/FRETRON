import matplotlib.pyplot as plt

def plot_flight_paths(flight_paths):
    for i, flight in enumerate(flight_paths):
        x, y = zip(*flight)
        plt.plot(x, y, marker='o', label=f"Flight {i + 1}")
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Flight Paths')
    plt.legend()
    plt.show()

def main():
    flight_paths = []

    num_flights = int(input("Enter the number of flights: "))

    for i in range(num_flights):
        path = input(f"Enter coordinates for Flight {i + 1} (comma-separated): ").split()
        coordinates = [tuple(map(int, coord.split(','))) for coord in path]
        flight_paths.append(coordinates)

    plot_flight_paths(flight_paths)

if __name__ == "__main__":
    main()
