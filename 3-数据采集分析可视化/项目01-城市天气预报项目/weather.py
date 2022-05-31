import requests
import time
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType

key = "18971b2be3e74760a0f7bbb79d0f6c71"
cities = ['北京', '上海',
          '天津', '重庆', '哈尔滨', '齐齐哈尔', '长春', '吉林',
          '大连', '沈阳', '呼和浩特', '鄂尔多斯', '承德', '石家庄', '乌鲁木齐',
          '阿勒泰', '皋兰', '兰州', '西宁', '大通', '西安', '咸阳', '银川', '郑州',
          '开封', '济南', '青岛', '太原', '大同', '合肥', '阜阳', '武汉', '武昌',
          '长沙', '浏阳', '南京', '无锡', '成都', '巴中', '贵阳', '六盘水', '昆明',
          '官渡', '南宁', '兴宁', '拉萨', '杭州', '苏州', '南昌', '九江', '广州',
          '仁化', '福州', '泉州', '台北', '高雄', '海口', '三亚', '香港', '广东',
        ]



def get_city_coordinate(city):
    """
    获取城市的坐标
    :return: 城市的经纬度
    """
    params = {
        "key": key,
        "location": city
    }
    text_json = requests.get(url="https://geoapi.qweather.com/v2/city/lookup", params=params).json()
    print(text_json)
    location = text_json["location"][0]
    return [location["lon"], location["lat"]]


def get_temp(coordinate):
    """
    获取城市次日的天气
    :return: 次日的天气
    """
    data_form = {
        'location': "{:.2f},{:.2f}".format(float(coordinate[0]), float(coordinate[1])),
        'key': key,
    }
    # 通过API接口获取天气数据
    temp_data = requests.get(url="https://devapi.qweather.com/v7/weather/3d", params=data_form).json()
    print(temp_data)
    text_day = temp_data['daily'][0]["textDay"]  # 明天的天气（晴、多云、小雨等）
    temp_max = temp_data['daily'][0]["tempMax"]  # 明天的最高温
    temp_min = temp_data['daily'][0]["tempMin"]  # 明天的最低温
    return f"次日天气{text_day}，最高温{temp_max}℃，最低温{temp_min}℃"


def geo(coors, fl_temps):
    """
    绘制中国地图，显示温度数据
    :return: 生成全国体感温度分布图
    """
    # 构建图形
    c = Geo()
    # 利用经纬度确定在地图上的位置
    # 城市名、经度、纬度
    for i, city in enumerate(cities):
        c.add_coordinate(city, coors[i][0], coors[i][1])

    # 样式
    c.add_schema(itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"), )
    c.add("次日天气&最高温&最低温", [list(z) for z in zip(cities, fl_temps)], type_=ChartType.EFFECT_SCATTER)
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    c.set_global_opts(title_opts=opts.TitleOpts(title="城市天气预报图"))
    # 生成HTML文件
    c.render('weather.html')


def run():
    coors = []
    fl_temps = []
    for city in cities:
        coor = get_city_coordinate(city)  # 坐标
        coors.append(coor)
        fl_temps.append(get_temp(coor))  # 天气、温度
        time.sleep(0.1)

    geo(coors, fl_temps)


if __name__ == '__main__':
    run()
