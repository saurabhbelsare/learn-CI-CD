"""Geometry toolbox for calculating areas of shapes."""

import math
import click

SUPPORTED_SHAPES = ["square", "circle", "triangle", "rectangle"]


def calculate_square_area(side: float) -> float:
    """Calculate the area of a square."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side


def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius


def calculate_triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle."""
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height


def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width


@click.command()
@click.option(
    "--shape", "-s",
    type=click.Choice(SUPPORTED_SHAPES, case_sensitive=False),
    prompt="Enter the shape name (square, circle, triangle, rectangle)",
    help="Name of the shape to calculate area for"
)
def area(shape: str):
    """Calculate the area of a shape."""
    shape = shape.lower()

    if shape == "square":
        side = click.prompt("Enter the side length", type=float)
        result = calculate_square_area(side)
        click.echo(f"Area of square: {result}")

    elif shape == "circle":
        radius = click.prompt("Enter the radius", type=float)
        result = calculate_circle_area(radius)
        click.echo(f"Area of circle: {result:.4f}")

    elif shape == "triangle":
        base = click.prompt("Enter the base", type=float)
        height = click.prompt("Enter the height", type=float)
        result = calculate_triangle_area(base, height)
        click.echo(f"Area of triangle: {result}")

    elif shape == "rectangle":
        length = click.prompt("Enter the length", type=float)
        width = click.prompt("Enter the width", type=float)
        result = calculate_rectangle_area(length, width)
        click.echo(f"Area of rectangle: {result}")


if __name__ == "__main__":
    area()
