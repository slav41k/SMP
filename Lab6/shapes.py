class Shape:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def create_3d(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def convert_to_2d(self):
        raise NotImplementedError("This method should be implemented by subclasses.")


class Cube(Shape):
    def create_3d(self):
        # 3D representation of a cube with only the edges visible
        layers = []
        size = self.size
        
        # Top face
        layers.append(" " * (size // 2) + "*" * size)

        # Sides
        for i in range(size - 2):
            layers.append(" " * (size // 2 - i - 1) + "*" + " " * (size - 2) + "*")
        
        # Bottom face
        layers.append("*" * size)
        return layers

    def convert_to_2d(self):
        return ["* " * self.size for _ in range(self.size)]


class Pyramid(Shape):
    def create_3d(self):
        # 3D representation of a pyramid with only the edges visible
        layers = []
        for i in range(self.size):
            spaces = " " * (self.size - i - 1)
            if i == self.size - 1:
                blocks = "*" * (2 * i + 1)
            else:
                blocks = "*" + " " * (2 * i - 1) + "*" if i > 0 else "*"
            layers.append(spaces + blocks)
        return layers

    def convert_to_2d(self):
        return [" " * (self.size - i - 1) + "* " * (i + 1) for i in range(self.size)]


class Sphere(Shape):
    def create_3d(self):
        # 3D representation of a sphere with only the edges visible
        layers = []
        radius = self.size // 2
        for i in range(self.size):
            distance_from_center = abs(radius - i)
            layer_width = radius - distance_from_center
            if layer_width > 0:
                layers.append(" " * (radius - layer_width) + "*" + " " * (2 * layer_width - 1) + "*")
            else:
                layers.append(" " * radius + "*")
        return layers

    def convert_to_2d(self):
        return [" " * abs(self.size // 2 - i) + "*" * (self.size - abs(self.size // 2 - i) * 2) for i in range(self.size)]

# You can instantiate and test these classes in your main application as follows:
if __name__ == "__main__":
    cube = Cube(7, "white")
    pyramid = Pyramid(7, "white")
    sphere = Sphere(7, "white")

    print("Cube 3D:")
    print("\n".join(cube.create_3d()))
    print("\nCube 2D:")
    print("\n".join(cube.convert_to_2d()))

    print("\nPyramid 3D:")
    print("\n".join(pyramid.create_3d()))
    print("\nPyramid 2D:")
    print("\n".join(pyramid.convert_to_2d()))

    print("\nSphere 3D:")
    print("\n".join(sphere.create_3d()))
    print("\nSphere 2D:")
    print("\n".join(sphere.convert_to_2d()))