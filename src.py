import csv

# Load the CSV data
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

# Compute performance and value scores
for row in data:
    performance_score = (
        0.4 * row["cpu"] +
        0.3 * row["gpu"] +
        0.2 * row["mem"] +
        0.1 * row["disk"]
    )
    row["performance_score"] = performance_score
    row["value_score"] = performance_score / row["base_price"]

# Find the best value model
best_value_model = max(data, key=lambda x: x["value_score"])

# Display results
print("Performance and Value Scores:")
for row in data:
    print(
        f"Model: {row['model']}, Performance Score: {row['performance_score']:.2f}, "
        f"Value Score: {row['value_score']:.5f}"
    )

print("\nBest Value Model:", best_value_model["model"])

