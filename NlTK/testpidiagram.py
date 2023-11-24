import matplotlib.pyplot as plt

# Sample HSC percentages, replace this with your data
hsc_percentages = {
    "Science": 80.0,
    "other": 20.0,

}

# Extract labels and values for the pie chart
labels = list(hsc_percentages.keys())
values = list(hsc_percentages.values())

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('HSC Percentage Distribution')

# Show the pie chart
plt.show()
