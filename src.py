import csv
import plotext as plt

# Step 1: Load the CSV data
data = []
with open("models.csv", "r") as csvfile:  # Replace with your file name
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert numeric fields to integers or floats
        row["base_price"] = int(row["base_price"])
        row["cpu"] = int(row["cpu"])
        row["gpu"] = int(row["gpu"])
        row["mem"] = int(row["mem"])
        row["disk"] = int(row["disk"])
        data.append(row)

# Step 2: Compute performance and value scores
for row in data:
    performance_score = (
        0.4 * row["cpu"] +
        0.3 * row["gpu"] +
        0.2 * row["mem"] +
        0.1 * row["disk"]
    )
    row["performance_score"] = performance_score
    row["value_score"] = performance_score / row["base_price"]

# Step 3: Extract models and value scores for plotting
models = [row["model"] for row in data]
value_scores = [row["value_score"] for row in data]

# Step 4: Plot the data using plotext
plt.bar(models, value_scores)
plt.title("Performance per Dollar")
plt.xlabel("Model")
plt.ylabel("Value Score")
plt.show()

# Step 5: Display the best value model
best_value_model = max(data, key=lambda x: x["value_score"])
print(f"\nBest Value Model: {best_value_model['model']}")
