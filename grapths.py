import matplotlib.pyplot as plt

class Plot:
    def __init__(self, names: list, values: list) -> None:
        # Create the bar graph
        plt.bar(names, values)

        # Add labels and title
        plt.xlabel('Windows')
        plt.ylabel('Time')
        plt.title('Time Spent')

        # Display the plot
        plt.show()