from manim import *
from math import cos

class IntegralApproximation(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2, 0.5],
            y_range=[0, 4, 1],
            axis_config={"color": WHITE},
        )

        curve = axes.plot(lambda x: x**2, color=PINK)
        curve_label = axes.get_graph_label(curve, label="x^2")

        self.play(Create(axes), Create(curve), Write(curve_label))
        self.wait(1)

        rectangles_group = VGroup()  # Initialize an empty group for rectangles

        for n in [1, 2, 4, 8, 16, 32, 64, 128, 256]:
            new_rectangles_group = self.get_riemann_rectangles(axes, curve, n)
            if rectangles_group:  # If there are previous rectangles, remove them
                self.remove(rectangles_group)
            rectangles_group = new_rectangles_group
            self.add(rectangles_group)
            self.wait(0.31)  # Pause to observe each step

        self.wait(2)

    def get_riemann_rectangles(self, axes, curve, n):
        rectangles = VGroup()
        dx = (axes.x_range[1] - axes.x_range[0]) / n  # Width of each rectangle
        for i in range(0, n):
            # For midpoint Riemann sum, the height of the rectangle is the value of the function at the midpoint
            x_left = axes.x_range[0] + i * dx
            y_mid = curve.underlying_function(x_left)
            rectangle = Rectangle(
                width=axes.c2p(dx, 0)[0] - axes.c2p(0, 0)[0], # Width is the difference in x-coordinates
                height=axes.c2p(0, y_mid)[1] - axes.c2p(0, 0)[1],  # Height is the difference in y-coordinates
                fill_color=BLUE,
                fill_opacity=0.5,
                stroke_color=GREEN,
                stroke_width=0.5,
            )
            rectangle.move_to(axes.c2p(dx/2 + x_left, y_mid / 2), aligned_edge=ORIGIN)
            rectangles.add(rectangle)
        return rectangles

