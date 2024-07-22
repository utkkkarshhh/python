import matplotlib.pyplot as plt

def plot_line_chart(x, y, title='Line Chart', xlabel='X-axis', ylabel='Y-axis'):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 30]
    
    # Plot the line chart
    plot_line_chart(x, y, title='Sample Line Chart', xlabel='X Values', ylabel='Y Values')
