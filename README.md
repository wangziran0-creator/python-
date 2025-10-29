# 地理坐标距离计算器 / Geographical Coordinate Distance Calculator

一个用于计算两个经纬度坐标之间距离的 Python 程序。使用 Haversine 公式精确计算球面距离。

A Python program for calculating the distance between two latitude/longitude coordinates. Uses the Haversine formula to accurately calculate spherical distances.

## 功能特性 / Features

- ✅ 精确的 Haversine 公式实现 / Accurate Haversine formula implementation
- ✅ 支持多种距离单位 / Multiple distance units supported
  - 千米 (km) - Kilometers
  - 英里 (miles) - Miles
  - 米 (m) - Meters
  - 海里 (nm) - Nautical miles
- ✅ 输入验证 / Input validation
- ✅ 完整的中英文文档 / Complete bilingual documentation (Chinese/English)
- ✅ 全面的单元测试 / Comprehensive unit tests
- ✅ 简单易用的 API / Easy-to-use API

## 安装 / Installation

无需额外依赖，只需要 Python 3.6+

No additional dependencies required, only Python 3.6+

```bash
# 克隆仓库 / Clone the repository
git clone https://github.com/wangziran0-creator/python-.git
cd python-
```

## 快速开始 / Quick Start

### 基本使用 / Basic Usage

```python
from geo_distance import GeoDistanceCalculator, calculate_distance

# 创建计算器实例 / Create calculator instance
calculator = GeoDistanceCalculator()

# 北京到上海的距离 / Distance from Beijing to Shanghai
beijing_lat, beijing_lon = 39.9042, 116.4074
shanghai_lat, shanghai_lon = 31.2304, 121.4737

distance_km = calculator.calculate_distance_km(
    beijing_lat, beijing_lon, 
    shanghai_lat, shanghai_lon
)
print(f"距离 / Distance: {distance_km:.2f} km")
# 输出 / Output: 距离 / Distance: 1067.31 km
```

### 使用便捷函数 / Using Convenience Function

```python
from geo_distance import calculate_distance

# 纽约到洛杉矶 / New York to Los Angeles
ny_lat, ny_lon = 40.7128, -74.0060
la_lat, la_lon = 34.0522, -118.2437

# 千米 / Kilometers
distance_km = calculate_distance(ny_lat, ny_lon, la_lat, la_lon, 'km')
print(f"{distance_km:.2f} km")

# 英里 / Miles
distance_miles = calculate_distance(ny_lat, ny_lon, la_lat, la_lon, 'miles')
print(f"{distance_miles:.2f} miles")
```

### 不同单位示例 / Different Units Examples

```python
from geo_distance import GeoDistanceCalculator

calculator = GeoDistanceCalculator()

lat1, lon1 = 0.0, 0.0
lat2, lon2 = 1.0, 1.0

# 千米 / Kilometers
print(calculator.calculate_distance(lat1, lon1, lat2, lon2, 'km'))

# 英里 / Miles
print(calculator.calculate_distance(lat1, lon1, lat2, lon2, 'miles'))

# 米 / Meters
print(calculator.calculate_distance(lat1, lon1, lat2, lon2, 'm'))

# 海里 / Nautical miles
print(calculator.calculate_distance(lat1, lon1, lat2, lon2, 'nm'))
```

## API 文档 / API Documentation

### GeoDistanceCalculator 类 / GeoDistanceCalculator Class

#### calculate_distance(lat1, lon1, lat2, lon2, unit='km')

计算两个坐标之间的距离 / Calculate distance between two coordinates

**参数 / Parameters:**
- `lat1` (float): 第一个点的纬度，范围 -90 到 90 / Latitude of first point, range -90 to 90
- `lon1` (float): 第一个点的经度，范围 -180 到 180 / Longitude of first point, range -180 to 180
- `lat2` (float): 第二个点的纬度，范围 -90 到 90 / Latitude of second point, range -90 to 90
- `lon2` (float): 第二个点的经度，范围 -180 到 180 / Longitude of second point, range -180 to 180
- `unit` (str): 距离单位 / Distance unit
  - `'km'` - 千米（默认）/ Kilometers (default)
  - `'miles'` - 英里 / Miles
  - `'m'` - 米 / Meters
  - `'nm'` - 海里 / Nautical miles

**返回 / Returns:**
- `float`: 距离值 / Distance value

**异常 / Raises:**
- `ValueError`: 输入坐标或单位无效时 / When coordinates or unit are invalid

#### calculate_distance_km(lat1, lon1, lat2, lon2)

计算距离（千米）/ Calculate distance in kilometers

#### calculate_distance_miles(lat1, lon1, lat2, lon2)

计算距离（英里）/ Calculate distance in miles

#### calculate_distance_meters(lat1, lon1, lat2, lon2)

计算距离（米）/ Calculate distance in meters

## 运行示例 / Running Examples

```bash
# 运行示例程序 / Run example program
python3 geo_distance.py
```

## 运行测试 / Running Tests

```bash
# 运行所有测试 / Run all tests
python3 -m unittest test_geo_distance -v

# 运行特定测试类 / Run specific test class
python3 -m unittest test_geo_distance.TestGeoDistanceCalculator -v
```

## 测试覆盖 / Test Coverage

测试包括 / Tests include:
- ✅ 基本距离计算 / Basic distance calculations
- ✅ 不同单位转换 / Different unit conversions
- ✅ 输入验证 / Input validation
- ✅ 边界情况（极点、国际日期变更线等）/ Edge cases (poles, date line, etc.)
- ✅ 负坐标（南半球、西半球）/ Negative coordinates (southern/western hemispheres)
- ✅ 极小距离和极大距离 / Very small and very large distances

## 技术细节 / Technical Details

### Haversine 公式 / Haversine Formula

本程序使用 Haversine 公式计算球面上两点之间的大圆距离：

This program uses the Haversine formula to calculate the great-circle distance between two points on a sphere:

```
a = sin²(Δlat/2) + cos(lat1) × cos(lat2) × sin²(Δlon/2)
c = 2 × asin(√a)
d = R × c
```

其中 / Where:
- `Δlat` = lat2 - lat1 (纬度差 / latitude difference)
- `Δlon` = lon2 - lon1 (经度差 / longitude difference)
- `R` = 地球半径 / Earth's radius
- `d` = 距离 / distance

### 地球半径常数 / Earth Radius Constants

- 千米 / Kilometers: 6371.0 km
- 英里 / Miles: 3959.0 miles
- 米 / Meters: 6371000.0 m
- 海里 / Nautical miles: 3440.0 nm

## 贡献 / Contributing

欢迎提交问题和拉取请求！

Issues and pull requests are welcome!

## 许可证 / License

MIT License

## 作者 / Author

wangziran0-creator