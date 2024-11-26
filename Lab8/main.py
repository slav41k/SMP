import pandas as pd
import matplotlib.pyplot as plt

# Абстракція
class Observer:
    def update(self, message):
        raise NotImplementedError("This method should be overridden by subclasses.")

class ChartObserver(Observer):
    def update(self, message):
        print(f"ChartObserver: {message}")

class DataObserver(Observer):
    def update(self, message):
        print(f"DataObserver: {message}")

# ======== Адаптер (Adapter) ========
class ChartAdapter:
    def __init__(self, chart):
        self.chart = chart

    def plot(self, ax):
        self.chart.plot(ax)

# Наслідування
class MatplotlibChart:
    def __init__(self, data, x_column, y_column=None):
        self.data = data
        self.x_column = x_column
        self.y_column = y_column

class LineChart(MatplotlibChart):
    def plot(self, ax):
        ax.plot(self.data[self.x_column], self.data[self.y_column])
        ax.set_title("Line Chart")
        ax.set_xlabel(self.x_column)
        ax.set_ylabel(self.y_column)

class BarChart(MatplotlibChart):
    def plot(self, ax):
        ax.bar(self.data[self.x_column], self.data[self.y_column])
        ax.set_title("Bar Chart")
        ax.set_xlabel(self.x_column)
        ax.set_ylabel(self.y_column)

class ScatterChart(MatplotlibChart):
    def plot(self, ax):
        ax.scatter(self.data[self.x_column], self.data[self.y_column])
        ax.set_title("Scatter Chart")
        ax.set_xlabel(self.x_column)
        ax.set_ylabel(self.y_column)

class HistogramChart(MatplotlibChart):
    def plot(self, ax):
        ax.hist(self.data[self.x_column], bins=15)
        ax.set_title("Histogram")
        ax.set_xlabel(self.x_column)
        ax.set_ylabel("Frequency")

# ======== Основний додаток ========
class DataVisualizationApp:
    def __init__(self, file_path):
        self.data_loader = DataLoader(file_path)
        self.data = self.data_loader.get_data()
        self.observers = []

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def preprocess_data(self):
        self.data.dropna(inplace=True)
        self.notify_observers("Data has been preprocessed.")

    def show_data_summary(self):
        self.data_loader.explore_data()

    def visualize_double_chart(self, chart_type, x_column1, y_column1, x_column2, y_column2):
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        chart1 = None
        chart2 = None

        if chart_type == "line":
            chart1 = LineChart(self.data, x_column1, y_column1)
            chart2 = LineChart(self.data, x_column2, y_column2)
        elif chart_type == "bar":
            chart1 = BarChart(self.data, x_column1, y_column1)
            chart2 = BarChart(self.data, x_column2, y_column2)
        elif chart_type == "scatter":
            chart1 = ScatterChart(self.data, x_column1, y_column1)
            chart2 = ScatterChart(self.data, x_column2, y_column2)
        elif chart_type == "histogram":
            chart1 = HistogramChart(self.data, x_column1)
            chart2 = HistogramChart(self.data, x_column2)

        adapter1 = ChartAdapter(chart1)
        adapter2 = ChartAdapter(chart2)

        adapter1.plot(axs[0])
        adapter2.plot(axs[1])

        plt.tight_layout()
        plt.show()

        save_option = input("Do you want to save these charts? (y/n): ").lower()
        if save_option == 'y':
            file_name = input("Enter the file name to save the chart (without extension): ")
            fig.savefig(file_name + ".png")
            print(f"Charts saved as {file_name}.png")
        self.notify_observers(f"Two {chart_type} charts have been visualized and optionally saved.")

    def show_menu(self):
        while True:
            print("\nSelect an option:")
            print("1. Show data summary and extreme values")
            print("2. Line Chart (Date vs Temperature and Humidity)")
            print("3. Bar Chart (Date vs Temperature and Humidity)")
            print("4. Scatter Chart (Date vs Temperature and Humidity)")
            print("5. Histogram (Temperature and Humidity)")
            print("6. Exit")

            choice = input("Enter choice (1-6): ")
            try:
                if choice == '6':
                    print("Exiting the program.")
                    break
                elif choice == '1':
                    self.show_data_summary()
                elif choice in ['2', '3', '4', '5']:
                    chart_type = {
                        '2': 'line',
                        '3': 'bar',
                        '4': 'scatter',
                        '5': 'histogram'
                    }[choice]
                    self.visualize_double_chart(chart_type, "date", "temperature", "date", "humidity")
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

#Інкарсуляція
class DataLoader:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def get_data(self):
        return self.data

    def explore_data(self):
        print("Data Summary:")
        print(self.data.describe())
        print("\nExtreme Values:")
        print("Min Values:\n", self.data.min())
        print("Max Values:\n", self.data.max())

# ======== Використання ========
if __name__ == "__main__":
    file_path = "/Users/cyanide/Desktop/Polytech/SMP/SMP-main/Lab8/data.csv"  # Replace with your actual file path
    app = DataVisualizationApp(file_path)

    # Реєструємо спостерігачів
    chart_observer = ChartObserver()
    data_observer = DataObserver()
    app.register_observer(chart_observer)
    app.register_observer(data_observer)

    # Виконуємо операції
    app.preprocess_data()
    app.show_menu()