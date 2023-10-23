import matplotlib.pyplot as plt
import numpy as np

# Initialize an empty list to store food tuples
food_data = []

def add_entry():
    name = input("Enter the name of the food: ")
    calories = int(input("Enter the number of calories: "))
    protein = int(input("Enter the amount of protein (g): "))
    fat = int(input("Enter the amount of fat (g): "))
    carbs = int(input("Enter the amount of carbs (g): "))
    food_data.append((name, calories, protein, fat, carbs))
    print("Entry added.")

def visualize_data():
    if not food_data:
        print("No data to visualize.")
        return
    
    # Create a 2x2 grid of subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Data for Pie Chart
    labels = [food[0] for food in food_data]
    sizes = [food[1] for food in food_data]
    axs[0, 0].pie(sizes, labels=labels, autopct='%1.1f%%')
    axs[0, 0].set_title('Calorie Distribution by Food')

    # Data for Bar Chart
    index = np.arange(len(labels))
    axs[0, 1].bar(index, sizes)
    axs[0, 1].set_xlabel('Food')
    axs[0, 1].set_ylabel('Calories')
    axs[0, 1].set_xticks(index)
    axs[0, 1].set_xticklabels(labels, rotation=30)
    axs[0, 1].set_title('Calories in Different Foods')

    # Data for Histogram
    axs[1, 0].hist(sizes, bins=10, alpha=0.7, color='blue', edgecolor='black')
    axs[1, 0].set_xlabel('Calories')
    axs[1, 0].set_ylabel('Frequency')
    axs[1, 0].set_title('Calorie Distribution')

    # Data for Scatter Plot
    protein_values = [food[2] for food in food_data]
    axs[1, 1].scatter(labels, protein_values, c='red', label='Protein(g)')
    axs[1, 1].set_xlabel('Food')
    axs[1, 1].set_ylabel('Protein(g)')
    axs[1, 1].set_title('Protein Content in Different Foods')
    axs[1, 1].legend()

    plt.tight_layout()
    plt.show()


while True:
    print("\nFood Nutrient Tracker")
    print("1. Add Entry")
    print("2. Visualize Data")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_entry()
    elif choice == '2':
        visualize_data()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
