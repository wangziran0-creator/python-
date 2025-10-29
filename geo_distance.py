"""
地理坐标距离计算模块
Geographical Coordinate Distance Calculation Module

实现两个经纬度之间的距离计算，使用 Haversine 公式
Implements distance calculation between two latitude/longitude coordinates using the Haversine formula
"""

import math


class GeoDistanceCalculator:
    """
    地理距离计算器
    Geographical Distance Calculator
    
    用于计算两个地理坐标之间的距离
    Used to calculate the distance between two geographical coordinates
    """
    
    # 地球半径（单位：千米）
    # Earth radius in kilometers
    EARTH_RADIUS_KM = 6371.0
    
    # 地球半径（单位：英里）
    # Earth radius in miles
    EARTH_RADIUS_MILES = 3959.0
    
    # 地球半径（单位：米）
    # Earth radius in meters
    EARTH_RADIUS_METERS = 6371000.0
    
    # 地球半径（单位：海里）
    # Earth radius in nautical miles
    EARTH_RADIUS_NAUTICAL_MILES = 3440.0
    
    @staticmethod
    def _to_radians(degrees):
        """
        将角度转换为弧度
        Convert degrees to radians
        
        Args:
            degrees (float): 角度值 / Degree value
            
        Returns:
            float: 弧度值 / Radian value
        """
        return degrees * math.pi / 180.0
    
    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2, unit='km'):
        """
        使用 Haversine 公式计算两个经纬度坐标之间的距离
        Calculate the distance between two lat/lng coordinates using the Haversine formula
        
        Haversine 公式是一个用于计算球面上两点之间距离的公式，
        适用于地球这样的近似球体。
        
        The Haversine formula is used to calculate the distance between two points 
        on a sphere, suitable for approximating the Earth.
        
        Args:
            lat1 (float): 第一个点的纬度 / Latitude of the first point (-90 to 90)
            lon1 (float): 第一个点的经度 / Longitude of the first point (-180 to 180)
            lat2 (float): 第二个点的纬度 / Latitude of the second point (-90 to 90)
            lon2 (float): 第二个点的经度 / Longitude of the second point (-180 to 180)
            unit (str): 距离单位 / Distance unit
                       'km' - 千米 (kilometers, default)
                       'miles' - 英里 (miles)
                       'm' - 米 (meters)
                       'nm' - 海里 (nautical miles)
        
        Returns:
            float: 两点之间的距离 / Distance between the two points
            
        Raises:
            ValueError: 如果输入的坐标或单位无效 / If coordinates or unit are invalid
        
        Examples:
            >>> calc = GeoDistanceCalculator()
            >>> # 北京到上海的距离 (Beijing to Shanghai)
            >>> distance = calc.calculate_distance(39.9042, 116.4074, 31.2304, 121.4737)
            >>> print(f"Distance: {distance:.2f} km")
            Distance: 1067.52 km
        """
        # 验证输入
        # Validate input
        if not (-90 <= lat1 <= 90) or not (-90 <= lat2 <= 90):
            raise ValueError("纬度必须在 -90 到 90 之间 / Latitude must be between -90 and 90")
        
        if not (-180 <= lon1 <= 180) or not (-180 <= lon2 <= 180):
            raise ValueError("经度必须在 -180 到 180 之间 / Longitude must be between -180 and 180")
        
        # 选择地球半径
        # Select Earth radius based on unit
        radius_map = {
            'km': GeoDistanceCalculator.EARTH_RADIUS_KM,
            'miles': GeoDistanceCalculator.EARTH_RADIUS_MILES,
            'm': GeoDistanceCalculator.EARTH_RADIUS_METERS,
            'nm': GeoDistanceCalculator.EARTH_RADIUS_NAUTICAL_MILES
        }
        
        if unit not in radius_map:
            raise ValueError(f"不支持的单位: {unit}. 支持的单位: {', '.join(radius_map.keys())} / "
                           f"Unsupported unit: {unit}. Supported units: {', '.join(radius_map.keys())}")
        
        earth_radius = radius_map[unit]
        
        # 将角度转换为弧度
        # Convert degrees to radians
        lat1_rad = GeoDistanceCalculator._to_radians(lat1)
        lon1_rad = GeoDistanceCalculator._to_radians(lon1)
        lat2_rad = GeoDistanceCalculator._to_radians(lat2)
        lon2_rad = GeoDistanceCalculator._to_radians(lon2)
        
        # 计算纬度和经度的差值
        # Calculate differences in latitude and longitude
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        # Haversine 公式
        # Haversine formula
        a = (math.sin(dlat / 2) ** 2 + 
             math.cos(lat1_rad) * math.cos(lat2_rad) * 
             math.sin(dlon / 2) ** 2)
        
        c = 2 * math.asin(math.sqrt(a))
        
        # 计算距离
        # Calculate distance
        distance = earth_radius * c
        
        return distance
    
    @staticmethod
    def calculate_distance_km(lat1, lon1, lat2, lon2):
        """
        计算两点之间的距离（千米）
        Calculate distance in kilometers
        
        Args:
            lat1 (float): 第一个点的纬度 / Latitude of the first point
            lon1 (float): 第一个点的经度 / Longitude of the first point
            lat2 (float): 第二个点的纬度 / Latitude of the second point
            lon2 (float): 第二个点的经度 / Longitude of the second point
            
        Returns:
            float: 距离（千米）/ Distance in kilometers
        """
        return GeoDistanceCalculator.calculate_distance(lat1, lon1, lat2, lon2, unit='km')
    
    @staticmethod
    def calculate_distance_miles(lat1, lon1, lat2, lon2):
        """
        计算两点之间的距离（英里）
        Calculate distance in miles
        
        Args:
            lat1 (float): 第一个点的纬度 / Latitude of the first point
            lon1 (float): 第一个点的经度 / Longitude of the first point
            lat2 (float): 第二个点的纬度 / Latitude of the second point
            lon2 (float): 第二个点的经度 / Longitude of the second point
            
        Returns:
            float: 距离（英里）/ Distance in miles
        """
        return GeoDistanceCalculator.calculate_distance(lat1, lon1, lat2, lon2, unit='miles')
    
    @staticmethod
    def calculate_distance_meters(lat1, lon1, lat2, lon2):
        """
        计算两点之间的距离（米）
        Calculate distance in meters
        
        Args:
            lat1 (float): 第一个点的纬度 / Latitude of the first point
            lon1 (float): 第一个点的经度 / Longitude of the first point
            lat2 (float): 第二个点的纬度 / Latitude of the second point
            lon2 (float): 第二个点的经度 / Longitude of the second point
            
        Returns:
            float: 距离（米）/ Distance in meters
        """
        return GeoDistanceCalculator.calculate_distance(lat1, lon1, lat2, lon2, unit='m')


# 便捷函数 / Convenience functions
def calculate_distance(lat1, lon1, lat2, lon2, unit='km'):
    """
    计算两个经纬度坐标之间的距离（便捷函数）
    Calculate distance between two coordinates (convenience function)
    
    Args:
        lat1 (float): 第一个点的纬度 / Latitude of the first point
        lon1 (float): 第一个点的经度 / Longitude of the first point
        lat2 (float): 第二个点的纬度 / Latitude of the second point
        lon2 (float): 第二个点的经度 / Longitude of the second point
        unit (str): 距离单位 / Distance unit ('km', 'miles', 'm', 'nm')
        
    Returns:
        float: 两点之间的距离 / Distance between the two points
    """
    return GeoDistanceCalculator.calculate_distance(lat1, lon1, lat2, lon2, unit)


if __name__ == "__main__":
    # 示例使用 / Example usage
    print("=" * 60)
    print("地理坐标距离计算示例 / Geographical Distance Calculation Examples")
    print("=" * 60)
    
    # 示例 1: 北京到上海
    # Example 1: Beijing to Shanghai
    beijing_lat, beijing_lon = 39.9042, 116.4074
    shanghai_lat, shanghai_lon = 31.2304, 121.4737
    
    print("\n示例 1 / Example 1: 北京到上海 / Beijing to Shanghai")
    print(f"北京坐标 / Beijing: ({beijing_lat}, {beijing_lon})")
    print(f"上海坐标 / Shanghai: ({shanghai_lat}, {shanghai_lon})")
    
    calculator = GeoDistanceCalculator()
    
    distance_km = calculator.calculate_distance_km(
        beijing_lat, beijing_lon, shanghai_lat, shanghai_lon
    )
    print(f"距离 / Distance: {distance_km:.2f} km")
    
    distance_miles = calculator.calculate_distance_miles(
        beijing_lat, beijing_lon, shanghai_lat, shanghai_lon
    )
    print(f"距离 / Distance: {distance_miles:.2f} miles")
    
    # 示例 2: 纽约到洛杉矶
    # Example 2: New York to Los Angeles
    ny_lat, ny_lon = 40.7128, -74.0060
    la_lat, la_lon = 34.0522, -118.2437
    
    print("\n示例 2 / Example 2: 纽约到洛杉矶 / New York to Los Angeles")
    print(f"纽约坐标 / New York: ({ny_lat}, {ny_lon})")
    print(f"洛杉矶坐标 / Los Angeles: ({la_lat}, {la_lon})")
    
    distance_km = calculate_distance(ny_lat, ny_lon, la_lat, la_lon, 'km')
    print(f"距离 / Distance: {distance_km:.2f} km")
    
    distance_miles = calculate_distance(ny_lat, ny_lon, la_lat, la_lon, 'miles')
    print(f"距离 / Distance: {distance_miles:.2f} miles")
    
    # 示例 3: 同一点（距离应该为 0）
    # Example 3: Same point (distance should be 0)
    print("\n示例 3 / Example 3: 同一点 / Same Point")
    print(f"坐标 / Coordinate: ({beijing_lat}, {beijing_lon})")
    
    distance = calculate_distance(beijing_lat, beijing_lon, beijing_lat, beijing_lon)
    print(f"距离 / Distance: {distance:.2f} km")
    
    print("\n" + "=" * 60)
