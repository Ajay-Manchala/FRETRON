def distribute_apples(apples, contributions):
    # Sort apples by weight in descending order
    apples.sort(reverse=True)
    
    # Calculate the total weight
    total_weight = sum(apples)
    
    # Calculate the target weights based on contributions
    total_contribution = sum(contributions)
    target_weights = [contrib / total_contribution * total_weight for contrib in contributions]
    
    # Initialize the distribution lists
    allocation = [[] for _ in contributions]
    current_weights = [0] * len(contributions)
    
    for apple in apples:
        # Find the person with the least proportion of their target weight
        min_index = min(range(len(contributions)), key=lambda i: current_weights[i] / target_weights[i])
        allocation[min_index].append(apple)
        current_weights[min_index] += apple
    
    return allocation

def main():
    apples = []
    
    print("Enter apple weights in grams. Type -1 when you are done:")
    while True:
        try:
            weight = int(input("Enter apple weight in gram (-1 to stop): "))
            if weight == -1:
                break
            apples.append(weight)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Contributions made by Ram, Sham, and Rahim
    contributions = [50, 30, 20]
    
    # Distribute apples based on contributions
    allocation = distribute_apples(apples, contributions)

    # Print the distribution result
    print("Distribution Result:")
    for i, person in enumerate(["Ram", "Sham", "Rahim"]):
        print(f"{person}: {', '.join(map(str, allocation[i]))}")

if __name__ == "__main__":
    main()
