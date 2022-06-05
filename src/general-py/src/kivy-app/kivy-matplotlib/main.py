# Kivy specific imports
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg \
    import FigureCanvasKivyAgg

# Other imports
import matplotlib.pyplot as plt
from math import e as euler_number

n: int = 0

# Parse random graph data based on user's range
def parse_graph_data(default: int = 10):
    global n
    try:
        n = int(input("Range of the graph [x]: "))
    except ValueError:
        print("Invalid input, defaulting to 10")
        n = default

    # Default function: e^{x/n}
    # Composes axis values
    return [i + 1 for i in range(n)], [euler_number ** (i /n) for i in range(n)]


# Clear the terminal screen, clear kivy boilerplate messages
print("\033[2J\033[1;1H", end='')

# Plot parsed iterable to graph
plt.plot(*parse_graph_data())
plt.title(f'y=e^(x/{n})')
plt.xlabel('x-axis')
plt.ylabel('y-axis')


class Main(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a figure with the matplotlib backend
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def save_graph(self):
        name = self.ids.namer.text  # Detect the passed name in the box

        # If name exists in the box, save the graph
        if name:
            plt.savefig(f'exp/{name}.png')
            # Close the app
            self.get_parent_window().close()
            

# Build default app from `.kv` file
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        Builder.load_file('main.kv')
        return Main()


MainApp().run()