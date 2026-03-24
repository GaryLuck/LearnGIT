import argparse
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def get_sierpinski_triangles(order, p1, p2, p3):
    if order == 0:
        return [[p1, p2, p3]]
    else:
        m1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        m2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
        m3 = ((p1[0] + p3[0]) / 2, (p1[1] + p3[1]) / 2)

        triangles = []
        triangles.extend(get_sierpinski_triangles(order - 1, p1, m1, m3))
        triangles.extend(get_sierpinski_triangles(order - 1, m1, p2, m2))
        triangles.extend(get_sierpinski_triangles(order - 1, m3, m2, p3))
        return triangles

def draw_sierpinski(depth):
    # Vertices of the main equilateral triangle
    p1 = (0.0, 0.0)
    p2 = (1.0, 0.0)
    p3 = (0.5, math.sqrt(3) / 2)

    triangles = get_sierpinski_triangles(depth, p1, p2, p3)

    fig, ax = plt.subplots(figsize=(8, 8))

    patches = []
    for t in triangles:
        polygon = Polygon(t, closed=True)
        patches.append(polygon)

    p = PatchCollection(patches, facecolor='black', edgecolor='none')
    ax.add_collection(p)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, math.sqrt(3) / 2)
    ax.set_aspect('equal')
    ax.axis('off')  # Hide axes for a cleaner look

    plt.title(f"Sierpinski Triangle (Depth = {depth})")
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Display a Sierpinski triangle using matplotlib.")
    parser.add_argument(
        '-d', '--depth',
        type=int,
        default=5,
        help="The recursion depth for the Sierpinski triangle (default: 5)."
    )
    args = parser.parse_args()

    if args.depth < 0:
        print("Depth must be a non-negative integer.")
    else:
        draw_sierpinski(args.depth)
