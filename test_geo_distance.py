"""
单元测试 - 地理坐标距离计算模块
Unit Tests for Geographical Coordinate Distance Calculation Module
"""

import unittest
import math
from geo_distance import GeoDistanceCalculator, calculate_distance


class TestGeoDistanceCalculator(unittest.TestCase):
    """测试 GeoDistanceCalculator 类 / Test GeoDistanceCalculator class"""
    
    def setUp(self):
        """设置测试 / Set up test"""
        self.calculator = GeoDistanceCalculator()
        
    def test_same_point_distance(self):
        """测试同一点的距离应该为 0 / Test that distance between same point is 0"""
        lat, lon = 39.9042, 116.4074
        distance = self.calculator.calculate_distance(lat, lon, lat, lon)
        self.assertAlmostEqual(distance, 0.0, places=2)
        
    def test_beijing_to_shanghai_km(self):
        """测试北京到上海的距离（千米）/ Test Beijing to Shanghai distance in km"""
        beijing_lat, beijing_lon = 39.9042, 116.4074
        shanghai_lat, shanghai_lon = 31.2304, 121.4737
        
        distance = self.calculator.calculate_distance_km(
            beijing_lat, beijing_lon, shanghai_lat, shanghai_lon
        )
        
        # 实际距离约 1067 千米
        # Actual distance is approximately 1067 km
        self.assertAlmostEqual(distance, 1067.31, delta=1.0)
        
    def test_new_york_to_los_angeles_miles(self):
        """测试纽约到洛杉矶的距离（英里）/ Test New York to Los Angeles distance in miles"""
        ny_lat, ny_lon = 40.7128, -74.0060
        la_lat, la_lon = 34.0522, -118.2437
        
        distance = self.calculator.calculate_distance_miles(
            ny_lat, ny_lon, la_lat, la_lon
        )
        
        # 实际距离约 2445 英里
        # Actual distance is approximately 2445 miles
        self.assertAlmostEqual(distance, 2445.71, delta=5.0)
        
    def test_distance_meters(self):
        """测试米单位的距离计算 / Test distance calculation in meters"""
        lat1, lon1 = 0.0, 0.0
        lat2, lon2 = 0.0, 0.01  # 约 1.11 千米
        
        distance = self.calculator.calculate_distance_meters(lat1, lon1, lat2, lon2)
        
        # 应该约为 1111 米
        # Should be approximately 1111 meters
        self.assertAlmostEqual(distance, 1111.95, delta=10.0)
        
    def test_nautical_miles(self):
        """测试海里单位的距离计算 / Test distance calculation in nautical miles"""
        lat1, lon1 = 0.0, 0.0
        lat2, lon2 = 1.0, 0.0
        
        distance = self.calculator.calculate_distance(lat1, lon1, lat2, lon2, unit='nm')
        
        # 1 度纬度约为 60 海里
        # 1 degree of latitude is approximately 60 nautical miles
        self.assertAlmostEqual(distance, 60.0, delta=1.0)
        
    def test_invalid_latitude(self):
        """测试无效纬度应该抛出异常 / Test that invalid latitude raises ValueError"""
        with self.assertRaises(ValueError) as context:
            self.calculator.calculate_distance(100.0, 0.0, 0.0, 0.0)
        
        exception_str = str(context.exception)
        self.assertTrue("纬度" in exception_str or "latitude" in exception_str.lower())
        
    def test_invalid_longitude(self):
        """测试无效经度应该抛出异常 / Test that invalid longitude raises ValueError"""
        with self.assertRaises(ValueError) as context:
            self.calculator.calculate_distance(0.0, 200.0, 0.0, 0.0)
        
        exception_str = str(context.exception)
        self.assertTrue("经度" in exception_str or "longitude" in exception_str.lower())
        
    def test_invalid_unit(self):
        """测试无效单位应该抛出异常 / Test that invalid unit raises ValueError"""
        with self.assertRaises(ValueError) as context:
            self.calculator.calculate_distance(0.0, 0.0, 1.0, 1.0, unit='invalid')
        
        exception_str = str(context.exception)
        self.assertTrue("单位" in exception_str or "unit" in exception_str.lower())
        
    def test_negative_coordinates(self):
        """测试负坐标（南半球和西半球）/ Test negative coordinates (southern and western hemispheres)"""
        # 悉尼到开普敦
        # Sydney to Cape Town
        sydney_lat, sydney_lon = -33.8688, 151.2093
        cape_town_lat, cape_town_lon = -33.9249, 18.4241
        
        distance = self.calculator.calculate_distance_km(
            sydney_lat, sydney_lon, cape_town_lat, cape_town_lon
        )
        
        # 距离约 11,004 千米
        # Distance is approximately 11,004 km
        self.assertGreater(distance, 10000.0)
        self.assertLess(distance, 12000.0)
        
    def test_equator_distance(self):
        """测试赤道上的距离 / Test distance along the equator"""
        lat1, lon1 = 0.0, 0.0
        lat2, lon2 = 0.0, 1.0
        
        distance = self.calculator.calculate_distance_km(lat1, lon1, lat2, lon2)
        
        # 赤道上 1 度经度约为 111.32 千米
        # 1 degree of longitude at equator is approximately 111.32 km
        self.assertAlmostEqual(distance, 111.32, delta=1.0)
        
    def test_to_radians(self):
        """测试角度转弧度函数 / Test degrees to radians conversion"""
        self.assertAlmostEqual(
            GeoDistanceCalculator._to_radians(0),
            0.0,
            places=5
        )
        self.assertAlmostEqual(
            GeoDistanceCalculator._to_radians(90),
            math.pi / 2,
            places=5
        )
        self.assertAlmostEqual(
            GeoDistanceCalculator._to_radians(180),
            math.pi,
            places=5
        )
        self.assertAlmostEqual(
            GeoDistanceCalculator._to_radians(360),
            2 * math.pi,
            places=5
        )


class TestConvenienceFunction(unittest.TestCase):
    """测试便捷函数 / Test convenience function"""
    
    def test_convenience_function(self):
        """测试便捷函数与类方法的结果一致 / Test convenience function matches class method"""
        lat1, lon1 = 39.9042, 116.4074
        lat2, lon2 = 31.2304, 121.4737
        
        calculator = GeoDistanceCalculator()
        
        # 测试各种单位
        # Test various units
        for unit in ['km', 'miles', 'm', 'nm']:
            distance_class = calculator.calculate_distance(lat1, lon1, lat2, lon2, unit)
            distance_func = calculate_distance(lat1, lon1, lat2, lon2, unit)
            
            self.assertAlmostEqual(distance_class, distance_func, places=5,
                                 msg=f"Results differ for unit: {unit}")


class TestEdgeCases(unittest.TestCase):
    """测试边界情况 / Test edge cases"""
    
    def setUp(self):
        """设置测试 / Set up test"""
        self.calculator = GeoDistanceCalculator()
        
    def test_north_pole_to_south_pole(self):
        """测试从北极到南极的距离 / Test distance from North Pole to South Pole"""
        north_pole_lat, north_pole_lon = 90.0, 0.0
        south_pole_lat, south_pole_lon = -90.0, 0.0
        
        distance = self.calculator.calculate_distance_km(
            north_pole_lat, north_pole_lon,
            south_pole_lat, south_pole_lon
        )
        
        # 应该约为地球周长的一半（20,004 千米）
        # Should be approximately half Earth's circumference (20,004 km)
        self.assertAlmostEqual(distance, 20015.09, delta=50.0)
        
    def test_international_date_line(self):
        """测试跨越国际日期变更线 / Test crossing the International Date Line"""
        # 从接近 +180 到接近 -180
        # From near +180 to near -180
        lat1, lon1 = 0.0, 179.0
        lat2, lon2 = 0.0, -179.0
        
        distance = self.calculator.calculate_distance_km(lat1, lon1, lat2, lon2)
        
        # 应该约为 222.64 千米（2 度经度在赤道上）
        # Should be approximately 222.64 km (2 degrees of longitude at equator)
        self.assertAlmostEqual(distance, 222.64, delta=5.0)
        
    def test_very_small_distance(self):
        """测试非常小的距离 / Test very small distance"""
        lat1, lon1 = 40.0, -74.0
        lat2, lon2 = 40.0001, -74.0001
        
        distance = self.calculator.calculate_distance_meters(lat1, lon1, lat2, lon2)
        
        # 应该约为 15 米
        # Should be approximately 15 meters
        self.assertLess(distance, 20.0)
        self.assertGreater(distance, 10.0)


if __name__ == '__main__':
    # 运行测试
    # Run tests
    unittest.main(verbosity=2)
