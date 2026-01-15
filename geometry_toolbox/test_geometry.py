"""Tests for geometry module."""

import math
import pytest
from click.testing import CliRunner
from geometry import (
    calculate_square_area,
    calculate_circle_area,
    calculate_triangle_area,
    calculate_rectangle_area,
    calculate_rhombus_area,
    calculate_square_perimeter,
    calculate_circle_perimeter,
    calculate_triangle_perimeter,
    calculate_rectangle_perimeter,
    calculate_rhombus_perimeter,
    calculate,
    SUPPORTED_SHAPES,
    SUPPORTED_CALCULATIONS,
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


class TestRhombusArea:
    """Tests for rhombus area calculation."""

    def test_rhombus_area_90_degrees(self):
        # At 90 degrees, rhombus is a square: side^2 * sin(90) = side^2
        assert calculate_rhombus_area(4, 90) == pytest.approx(16)

    def test_rhombus_area_45_degrees(self):
        # side^2 * sin(45) = 4^2 * sqrt(2)/2 = 16 * sqrt(2)/2
        expected = 16 * math.sin(math.radians(45))
        assert calculate_rhombus_area(4, 45) == pytest.approx(expected)

    def test_rhombus_area_30_degrees(self):
        # side^2 * sin(30) = 5^2 * 0.5 = 12.5
        assert calculate_rhombus_area(5, 30) == pytest.approx(12.5)

    def test_rhombus_area_60_degrees(self):
        expected = 3 * 3 * math.sin(math.radians(60))
        assert calculate_rhombus_area(3, 60) == pytest.approx(expected)

    def test_rhombus_area_zero_side(self):
        assert calculate_rhombus_area(0, 45) == 0

    def test_rhombus_area_float(self):
        expected = 2.5 * 2.5 * math.sin(math.radians(60))
        assert calculate_rhombus_area(2.5, 60) == pytest.approx(expected)

    def test_rhombus_area_negative_side_raises(self):
        with pytest.raises(ValueError):
            calculate_rhombus_area(-1, 45)

    def test_rhombus_area_zero_angle_raises(self):
        with pytest.raises(ValueError):
            calculate_rhombus_area(5, 0)

    def test_rhombus_area_negative_angle_raises(self):
        with pytest.raises(ValueError):
            calculate_rhombus_area(5, -45)

    def test_rhombus_area_angle_over_90_raises(self):
        with pytest.raises(ValueError):
            calculate_rhombus_area(5, 91)


class TestSquarePerimeter:
    """Tests for square perimeter calculation."""

    def test_square_perimeter_basic(self):
        assert calculate_square_perimeter(4) == 16

    def test_square_perimeter_zero(self):
        assert calculate_square_perimeter(0) == 0

    def test_square_perimeter_float(self):
        assert calculate_square_perimeter(2.5) == 10.0

    def test_square_perimeter_negative_raises(self):
        with pytest.raises(ValueError):
            calculate_square_perimeter(-1)


class TestCirclePerimeter:
    """Tests for circle perimeter (circumference) calculation."""

    def test_circle_perimeter_basic(self):
        assert calculate_circle_perimeter(1) == pytest.approx(2 * math.pi)

    def test_circle_perimeter_radius_2(self):
        assert calculate_circle_perimeter(2) == pytest.approx(4 * math.pi)

    def test_circle_perimeter_zero(self):
        assert calculate_circle_perimeter(0) == 0

    def test_circle_perimeter_float(self):
        expected = 2 * math.pi * 2.5
        assert calculate_circle_perimeter(2.5) == pytest.approx(expected)

    def test_circle_perimeter_negative_raises(self):
        with pytest.raises(ValueError):
            calculate_circle_perimeter(-1)


class TestTrianglePerimeter:
    """Tests for triangle perimeter calculation."""

    def test_triangle_perimeter_basic(self):
        assert calculate_triangle_perimeter(3, 4, 5) == 12

    def test_triangle_perimeter_equilateral(self):
        assert calculate_triangle_perimeter(5, 5, 5) == 15

    def test_triangle_perimeter_zero_side(self):
        assert calculate_triangle_perimeter(0, 4, 5) == 9

    def test_triangle_perimeter_float(self):
        assert calculate_triangle_perimeter(3.5, 4.5, 5.0) == 13.0

    def test_triangle_perimeter_negative_side1_raises(self):
        with pytest.raises(ValueError):
            calculate_triangle_perimeter(-1, 4, 5)

    def test_triangle_perimeter_negative_side2_raises(self):
        with pytest.raises(ValueError):
            calculate_triangle_perimeter(3, -1, 5)

    def test_triangle_perimeter_negative_side3_raises(self):
        with pytest.raises(ValueError):
            calculate_triangle_perimeter(3, 4, -1)


class TestRectanglePerimeter:
    """Tests for rectangle perimeter calculation."""

    def test_rectangle_perimeter_basic(self):
        assert calculate_rectangle_perimeter(4, 5) == 18

    def test_rectangle_perimeter_square(self):
        assert calculate_rectangle_perimeter(3, 3) == 12

    def test_rectangle_perimeter_zero_length(self):
        assert calculate_rectangle_perimeter(0, 5) == 10

    def test_rectangle_perimeter_zero_width(self):
        assert calculate_rectangle_perimeter(5, 0) == 10

    def test_rectangle_perimeter_float(self):
        assert calculate_rectangle_perimeter(2.5, 4.0) == 13.0

    def test_rectangle_perimeter_negative_length_raises(self):
        with pytest.raises(ValueError):
            calculate_rectangle_perimeter(-1, 5)

    def test_rectangle_perimeter_negative_width_raises(self):
        with pytest.raises(ValueError):
            calculate_rectangle_perimeter(5, -1)


class TestRhombusPerimeter:
    """Tests for rhombus perimeter calculation."""

    def test_rhombus_perimeter_basic(self):
        assert calculate_rhombus_perimeter(4) == 16

    def test_rhombus_perimeter_zero(self):
        assert calculate_rhombus_perimeter(0) == 0

    def test_rhombus_perimeter_float(self):
        assert calculate_rhombus_perimeter(2.5) == 10.0

    def test_rhombus_perimeter_negative_raises(self):
        with pytest.raises(ValueError):
            calculate_rhombus_perimeter(-1)


class TestCLIArea:
    """Tests for the Click CLI area calculations."""

    def test_square_area_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "square", "--calculation", "area"], input="4\n")
        assert result.exit_code == 0
        assert "Area of square: 16" in result.output

    def test_circle_area_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "circle", "--calculation", "area"], input="1\n")
        assert result.exit_code == 0
        assert "Area of circle:" in result.output

    def test_triangle_area_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "triangle", "--calculation", "area"], input="4\n3\n")
        assert result.exit_code == 0
        assert "Area of triangle: 6" in result.output

    def test_rectangle_area_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "rectangle", "--calculation", "area"], input="4\n5\n")
        assert result.exit_code == 0
        assert "Area of rectangle: 20" in result.output

    def test_rhombus_area_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "rhombus", "--calculation", "area"], input="5\n30\n")
        assert result.exit_code == 0
        assert "Area of rhombus:" in result.output


class TestCLIPerimeter:
    """Tests for the Click CLI perimeter calculations."""

    def test_square_perimeter_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "square", "--calculation", "perimeter"], input="4\n")
        assert result.exit_code == 0
        assert "Perimeter of square: 16" in result.output

    def test_circle_perimeter_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "circle", "--calculation", "perimeter"], input="1\n")
        assert result.exit_code == 0
        assert "Perimeter (circumference) of circle:" in result.output

    def test_triangle_perimeter_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "triangle", "--calculation", "perimeter"], input="3\n4\n5\n")
        assert result.exit_code == 0
        assert "Perimeter of triangle: 12" in result.output

    def test_rectangle_perimeter_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "rectangle", "--calculation", "perimeter"], input="4\n5\n")
        assert result.exit_code == 0
        assert "Perimeter of rectangle: 18" in result.output

    def test_rhombus_perimeter_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "rhombus", "--calculation", "perimeter"], input="4\n")
        assert result.exit_code == 0
        assert "Perimeter of rhombus: 16" in result.output


class TestCLIValidation:
    """Tests for CLI input validation."""

    def test_invalid_shape_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "hexagon", "--calculation", "area"])
        assert result.exit_code != 0
        assert "Invalid value" in result.output

    def test_invalid_calculation_cli(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "square", "--calculation", "volume"])
        assert result.exit_code != 0
        assert "Invalid value" in result.output

    def test_case_insensitive_shape(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "SQUARE", "--calculation", "area"], input="4\n")
        assert result.exit_code == 0
        assert "Area of square: 16" in result.output

    def test_case_insensitive_calculation(self):
        runner = CliRunner()
        result = runner.invoke(calculate, ["--shape", "square", "--calculation", "PERIMETER"], input="4\n")
        assert result.exit_code == 0
        assert "Perimeter of square: 16" in result.output
