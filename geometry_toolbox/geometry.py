"""Geometry toolbox for calculating areas and perimeters of shapes."""

import math
import click

SUPPORTED_SHAPES = ["square", "circle", "triangle", "rectangle", "rhombus"]
SUPPORTED_CALCULATIONS = ["area", "perimeter"]


# Area calculation functions
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


def calculate_rhombus_area(side: float, angle: float) -> float:
    """Calculate the area of a rhombus given side length and internal acute angle (in degrees)."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    if angle <= 0 or angle > 90:
        raise ValueError("Angle must be greater than 0 and at most 90 degrees")
    angle_radians = math.radians(angle)
    return side * side * math.sin(angle_radians)


# Perimeter calculation functions
def calculate_square_perimeter(side: float) -> float:
    """Calculate the perimeter of a square."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return 4 * side


def calculate_circle_perimeter(radius: float) -> float:
    """Calculate the perimeter (circumference) of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius


def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    """Calculate the perimeter of a triangle."""
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("Side lengths cannot be negative")
    return side1 + side2 + side3


def calculate_rectangle_perimeter(length: float, width: float) -> float:
    """Calculate the perimeter of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return 2 * (length + width)


def calculate_rhombus_perimeter(side: float) -> float:
    """Calculate the perimeter of a rhombus."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return 4 * side


@click.command()
@click.option(
    "--shape", "-s",
    type=click.Choice(SUPPORTED_SHAPES, case_sensitive=False),
    prompt="Enter the shape name (square, circle, triangle, rectangle, rhombus)",
    help="Name of the shape"
)
@click.option(
    "--calculation", "-c",
    type=click.Choice(SUPPORTED_CALCULATIONS, case_sensitive=False),
    prompt="Enter the calculation type (area, perimeter)",
    help="Type of calculation to perform"
)
def calculate(shape: str, calculation: str):
    """Calculate the area or perimeter of a shape."""
    shape = shape.lower()
    calculation = calculation.lower()

    if shape == "square":
        side = click.prompt("Enter the side length", type=float)
        if calculation == "area":
            result = calculate_square_area(side)
            click.echo(f"Area of square: {result}")
        else:
            result = calculate_square_perimeter(side)
            click.echo(f"Perimeter of square: {result}")

    elif shape == "circle":
        radius = click.prompt("Enter the radius", type=float)
        if calculation == "area":
            result = calculate_circle_area(radius)
            click.echo(f"Area of circle: {result:.4f}")
        else:
            result = calculate_circle_perimeter(radius)
            click.echo(f"Perimeter (circumference) of circle: {result:.4f}")

    elif shape == "triangle":
        if calculation == "area":
            base = click.prompt("Enter the base", type=float)
            height = click.prompt("Enter the height", type=float)
            result = calculate_triangle_area(base, height)
            click.echo(f"Area of triangle: {result}")
        else:
            side1 = click.prompt("Enter side 1", type=float)
            side2 = click.prompt("Enter side 2", type=float)
            side3 = click.prompt("Enter side 3", type=float)
            result = calculate_triangle_perimeter(side1, side2, side3)
            click.echo(f"Perimeter of triangle: {result}")

    elif shape == "rectangle":
        length = click.prompt("Enter the length", type=float)
        width = click.prompt("Enter the width", type=float)
        if calculation == "area":
            result = calculate_rectangle_area(length, width)
            click.echo(f"Area of rectangle: {result}")
        else:
            result = calculate_rectangle_perimeter(length, width)
            click.echo(f"Perimeter of rectangle: {result}")

    elif shape == "rhombus":
        side = click.prompt("Enter the side length", type=float)
        if calculation == "area":
            angle = click.prompt("Enter the internal acute angle (in degrees)", type=float)
            result = calculate_rhombus_area(side, angle)
            click.echo(f"Area of rhombus: {result:.4f}")
        else:
            result = calculate_rhombus_perimeter(side)
            click.echo(f"Perimeter of rhombus: {result}")


if __name__ == "__main__":
    calculate()
