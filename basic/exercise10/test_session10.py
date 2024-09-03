from session10 import Polygon, Polygons
import math
import unittest

def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.side_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.side_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

# Example Polygon class for testing purposes
class Polygon:
    def __init__(self, sides, radius):
        self.sides = sides
        self.radius = radius
        # Simplified calculations for area and perimeter
        import math
        self.perimeter = sides * (2 * radius * math.sin(math.pi / sides))
        self.area = 0.5 * sides * (radius ** 2) * math.sin(2 * math.pi / sides)


def test_iteration():
    """Test iteration over the Polygons."""
    polygons = Polygons(5, 10)
    sides_list = [polygon.sides for polygon in polygons]
    assert sides_list== [3, 4, 5]



# class TestPolygons(unittest.TestCase):
#     def setUp(self):
#         """Set up the test case environment."""
#         self.polygons = Polygons(5, 10)
        
#     def test_initialization(self):
#         """Test initialization of Polygons."""
#         self.assertEqual(len(self.polygons), 3)  # Should have polygons with 3, 4, and 5 sides
#         self.assertEqual(self.polygons._R, 10)
#         self.assertEqual(self.polygons[0].sides, 3)
#         self.assertEqual(self.polygons[1].sides, 4)
#         self.assertEqual(self.polygons[2].sides, 5)

#     def test_repr(self):
#         """Test the __repr__ method."""
#         self.assertEqual(repr(self.polygons), 'Polygons(m=5, R=10)')
        
#     def test_max_efficiency_polygon(self):
#         """Test the max_efficiency_polygon property."""
#         max_efficiency = self.polygons.max_efficiency_polygon
#         self.assertEqual(max_efficiency.sides, 3)  # Assuming 3-sided polygon has the highest efficiency

#     def test_iteration(self):
#         """Test iteration over the Polygons."""
#         sides_list = [polygon.sides for polygon in self.polygons]
#         self.assertEqual(sides_list, [3, 4, 5])

#     def test_indexing(self):
#         """Test indexing into the Polygons collection."""
#         self.assertEqual(self.polygons[0].sides, 3)
#         self.assertEqual(self.polygons[1].sides, 4)
#         self.assertEqual(self.polygons[2].sides, 5)
#         with self.assertRaises(IndexError):
#             _ = self.polygons[3]  # Index out of range