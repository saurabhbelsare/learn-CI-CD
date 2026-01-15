"""Tests for geometry module."""

import math
import pytest
from click.testing import CliRunner
from geometry import (
    calculate_square_area,
    calculate_circle_area,
    calculate_triangle_area,
    calculate_rectangle_area,
    area,
    SUPPORTED_SHAPES,
)


class TestSquareArea:
    """Tests for square area calculation."""

    def test_square_area_basic(self):
        assert calculate_square_area(4) == 16

    def test_square_area_zero(self):
        assert calculate_square_area(0) == 0

    def test_square_area_float(self):
        assert calculate_square_area(2.5) == 6.25

    def test_square_area_negative_raises(self):
        with pytest.raises(ValueError):
            calculate_square_area(-1)


class TestCircleArea:
    """Tests for circle area calculation."""

    def test_circle_area_basic(self):
        assert calculate_circle_area(1) == math.pi

    def test_circle_area_radius_2(self):
        assert calculate_circle_area(2) == pytest.approx(4 * math.pi)

    def test_circle_area_zero(self):
        assert calculate_circle_area(0) == 0

    def test_circle_area_float(self):
        expected = math.pi * 2.5 * 2.5
        assert calculate_circle_area(2.5) == pytest.approx(expected)

    def test_circle_area_negative_raises(self):
        with pytest.raises(ValueError):
            calculate_circle_area(-1)


class TestTriangleArea:
    """Tests for triangle area calculation."""

    def test_triangle_area_basic(self):
        assert calculate_triangle_area(4, 3) == 6

    def test_triangle_area_zero_base(self):
        assert calculate_triangle_area(0, 5) == 0

    def test_triangle_area_zero_height(self):
        assert calculate_triangle_area(5, 0) == 0

    def test_triangle_area_float(self):
        assert calculate_triangle_area(3.5, 2.0) == 3.5

    def test_triangle_area_negative_base_raises(self):
        with pytest.raises(ValueError):
            calculate_triangle_area(-1, 5)

    def test_triangle_area_negative_height_raises(self):
        with pytest.raises(ValueError):
            calculate_triangle_area(5, -1)


class TestRectangleArea:
    """Tests for rectangle area calculation."""

    def test_rectangle_area_basic(self):
        assert calculate_rectangle_area(4, 5) == 20

    def test_rectangle_area_square(self):
        assert calculate_rectangle_area(3, 3) == 9

    def test_rectangle_area_zero_length(self):
        assert calculate_rectangle_area(0, 5) == 0

    def test_rectangle_area_zero_width(self):
        assert calculate_rectangle_area(5, 0) == 0

    def test_rectangle_area_float(self):
        assert calculate_rectangle_area(2.5, 4.0) == 10.0

    def test_rectangle_area_negative_length_raises(self):
        with pytest.raises(ValueError):
            calculate_rectangle_area(-1, 5)

    def test_rectangle_area_negative_width_raises(self):
        with pytest.raises(ValueError):
            calculate_rectangle_area(5, -1)


class TestCLI:
    """Tests for the Click CLI."""

    def test_square_cli(self):
        runner = CliRunner()
        result = runner.invoke(area, ["--shape", "square"], input="4\n")
        assert result.exit_code == 0
        assert "Area of square: 16" in result.output

    def test_circle_cli(self):
        runner = CliRunner()
        result = runner.invoke(area, ["--shape", "circle"], input="1\n")
        assert result.exit_code == 0
        assert "Area of circle:" in result.output

    def test_triangle_cli(self):
        runner = CliRunner()
        result = runner.invoke(area, ["--shape", "triangle"], input="4\n3\n")
        assert result.exit_code == 0
        assert "Area of triangle: 6" in result.output

    def test_rectangle_cli(self):
        runner = CliRunner()
        result = runner.invoke(area, ["--shape", "rectangle"], input="4\n5\n")
        assert result.exit_code == 0
        assert "Area of rectangle: 20" in result.output

    def test_invalid_shape_cli(self):
        runner = CliRunner()
        result = runner.invoke(area, ["--shape", "hexagon"])
        assert result.exit_code != 0
        assert "Invalid value" in result.output

    def test_case_insensitive_shape(self):
        runner = CliRunner()
        result = runner.invoke(area, ["--shape", "SQUARE"], input="4\n")
        assert result.exit_code == 0
        assert "Area of square: 16" in result.output
