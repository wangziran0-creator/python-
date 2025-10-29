#!/usr/bin/env python3
"""
使用示例 / Usage Examples
演示如何使用地理坐标距离计算器
Demonstrates how to use the geographical coordinate distance calculator
"""

from geo_distance import GeoDistanceCalculator, calculate_distance


def example_1_basic_usage():
    """示例 1: 基本使用 / Example 1: Basic Usage"""
    print("=" * 70)
    print("示例 1: 基本使用 / Example 1: Basic Usage")
    print("=" * 70)
    
    calculator = GeoDistanceCalculator()
    
    # 北京到上海 / Beijing to Shanghai
    beijing = (39.9042, 116.4074)
    shanghai = (31.2304, 121.4737)
    
    distance = calculator.calculate_distance_km(*beijing, *shanghai)
    
    print(f"\n从北京到上海 / From Beijing to Shanghai:")
    print(f"  北京坐标 / Beijing: {beijing}")
    print(f"  上海坐标 / Shanghai: {shanghai}")
    print(f"  距离 / Distance: {distance:.2f} km")
    print()


def example_2_different_units():
    """示例 2: 使用不同单位 / Example 2: Using Different Units"""
    print("=" * 70)
    print("示例 2: 使用不同单位 / Example 2: Using Different Units")
    print("=" * 70)
    
    # 纽约到伦敦 / New York to London
    new_york = (40.7128, -74.0060)
    london = (51.5074, -0.1278)
    
    print(f"\n从纽约到伦敦 / From New York to London:")
    print(f"  纽约坐标 / New York: {new_york}")
    print(f"  伦敦坐标 / London: {london}")
    print()
    
    # 使用不同单位计算 / Calculate with different units
    for unit, unit_name in [('km', '千米/Kilometers'), 
                             ('miles', '英里/Miles'), 
                             ('m', '米/Meters'), 
                             ('nm', '海里/Nautical Miles')]:
        distance = calculate_distance(*new_york, *london, unit=unit)
        print(f"  {unit_name}: {distance:.2f} {unit}")
    print()


def example_3_world_cities():
    """示例 3: 世界各地城市距离 / Example 3: World Cities Distances"""
    print("=" * 70)
    print("示例 3: 世界各地城市距离 / Example 3: World Cities Distances")
    print("=" * 70)
    
    cities = {
        '北京/Beijing': (39.9042, 116.4074),
        '上海/Shanghai': (31.2304, 121.4737),
        '东京/Tokyo': (35.6762, 139.6503),
        '纽约/New York': (40.7128, -74.0060),
        '伦敦/London': (51.5074, -0.1278),
        '巴黎/Paris': (48.8566, 2.3522),
        '悉尼/Sydney': (-33.8688, 151.2093),
        '莫斯科/Moscow': (55.7558, 37.6173),
    }
    
    calculator = GeoDistanceCalculator()
    
    print("\n城市间距离表 / Distance Table Between Cities:")
    print("-" * 70)
    
    # 计算几个有趣的距离 / Calculate some interesting distances
    interesting_pairs = [
        ('北京/Beijing', '上海/Shanghai'),
        ('北京/Beijing', '东京/Tokyo'),
        ('纽约/New York', '伦敦/London'),
        ('悉尼/Sydney', '北京/Beijing'),
        ('巴黎/Paris', '莫斯科/Moscow'),
    ]
    
    for city1_name, city2_name in interesting_pairs:
        city1 = cities[city1_name]
        city2 = cities[city2_name]
        distance = calculator.calculate_distance_km(*city1, *city2)
        print(f"{city1_name:20} → {city2_name:20}: {distance:8.2f} km")
    print()


def example_4_validation():
    """示例 4: 输入验证 / Example 4: Input Validation"""
    print("=" * 70)
    print("示例 4: 输入验证 / Example 4: Input Validation")
    print("=" * 70)
    
    calculator = GeoDistanceCalculator()
    
    print("\n测试无效输入 / Testing Invalid Inputs:")
    print("-" * 70)
    
    # 测试无效纬度 / Test invalid latitude
    try:
        calculator.calculate_distance(100.0, 0.0, 0.0, 0.0)
    except ValueError as e:
        print(f"❌ 无效纬度 / Invalid latitude: {e}")
    
    # 测试无效经度 / Test invalid longitude
    try:
        calculator.calculate_distance(0.0, 200.0, 0.0, 0.0)
    except ValueError as e:
        print(f"❌ 无效经度 / Invalid longitude: {e}")
    
    # 测试无效单位 / Test invalid unit
    try:
        calculator.calculate_distance(0.0, 0.0, 1.0, 1.0, unit='invalid')
    except ValueError as e:
        print(f"❌ 无效单位 / Invalid unit: {e}")
    
    print()


def example_5_special_cases():
    """示例 5: 特殊情况 / Example 5: Special Cases"""
    print("=" * 70)
    print("示例 5: 特殊情况 / Example 5: Special Cases")
    print("=" * 70)
    
    calculator = GeoDistanceCalculator()
    
    # 同一点 / Same point
    beijing = (39.9042, 116.4074)
    distance = calculator.calculate_distance_km(*beijing, *beijing)
    print(f"\n同一点的距离 / Distance of same point:")
    print(f"  坐标 / Coordinate: {beijing}")
    print(f"  距离 / Distance: {distance:.2f} km")
    
    # 北极到南极 / North Pole to South Pole
    north_pole = (90.0, 0.0)
    south_pole = (-90.0, 0.0)
    distance = calculator.calculate_distance_km(*north_pole, *south_pole)
    print(f"\n北极到南极 / North Pole to South Pole:")
    print(f"  北极 / North Pole: {north_pole}")
    print(f"  南极 / South Pole: {south_pole}")
    print(f"  距离 / Distance: {distance:.2f} km")
    
    # 跨越国际日期变更线 / Crossing International Date Line
    point1 = (0.0, 179.0)
    point2 = (0.0, -179.0)
    distance = calculator.calculate_distance_km(*point1, *point2)
    print(f"\n跨越国际日期变更线 / Crossing International Date Line:")
    print(f"  点1 / Point 1: {point1}")
    print(f"  点2 / Point 2: {point2}")
    print(f"  距离 / Distance: {distance:.2f} km")
    print()


def main():
    """主函数 / Main function"""
    print("\n")
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*" + "  地理坐标距离计算器 - 使用示例".center(68) + "*")
    print("*" + "  Geographical Distance Calculator - Usage Examples".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*" * 70)
    print("\n")
    
    # 运行所有示例 / Run all examples
    example_1_basic_usage()
    example_2_different_units()
    example_3_world_cities()
    example_4_validation()
    example_5_special_cases()
    
    print("=" * 70)
    print("所有示例运行完成！/ All examples completed!")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
