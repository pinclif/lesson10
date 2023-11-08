import math

class Sphere:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.center[0])**2 + (y - self.center[1])**2 + (z - self.center[2]) ** 2)
        if distance <= self.radius:
            return True
        else:
            return False


sphere = Sphere(5, (0, 0, 0))


print("Sphere volume:", sphere.get_volume())
print("Outer surface area of a sphere:", sphere.get_square())
print("Sphere radius:", sphere.get_radius())
print("Sphere center coordinates:", sphere.get_center())


sphere.set_radius(10)
sphere.set_center(1, 2, 3)
print("New sphere radius:", sphere.get_radius())
print("New coordinates of the center of the sphere:", sphere.get_center())


print("Point (3, 4, 5) inside the sphere:", sphere.is_point_inside(3, 4, 5))
print("Point (10, 20, 30) insaide the sphere:", sphere.is_point_inside(10, 20, 30))