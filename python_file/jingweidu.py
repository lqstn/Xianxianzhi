import os
import requests
import json

# 获取所有JSON文件的文件名
json_folder = './mydata/records/record_json'  
output_folder = './mydata/records/record_json' 

# 确保输出文件夹存在，如果不存在就创建
os.makedirs(output_folder, exist_ok=True)

# Bing Maps API 密钥
bing_maps_api_key = 'AoqHXXfVk_gSSWXF5jbIOZ1IPfqyyzFDYNyHJdSZr1FWU7UgpT2ACOqFabgjFEQ6'  # 替换为你的 Bing Maps API 密钥
base_url = 'http://dev.virtualearth.net/REST/v1/Locations'

# 遍历JSON文件夹中的每个文件
for json_file in os.listdir(json_folder):
    if json_file.endswith('.json'):
        json_file_path = os.path.join(json_folder, json_file)

        # 读取JSON文件
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 对每个条目进行处理
        for item in data:
            city = item.get('地点', '')  # 假设城市名所在的键为'地点'

            # 构建请求参数
            params = {
                'query': city,
                'key': bing_maps_api_key,
            }

            # 发送请求
            response = requests.get(base_url, params=params)

            # 解析响应数据并提取经纬度
            if response.status_code == 200:
                result = response.json()
                try:
                    coordinates = result['resourceSets'][0]['resources'][0]['point']['coordinates']
                    latitude, longitude = coordinates
                    # 添加经纬度信息到数据中
                    item['纬度'] = latitude
                    item['经度'] = longitude
                except (KeyError, IndexError):
                    print(f"未能找到 {city} 的经纬度信息")
            else:
                print(f"请求失败：{response.status_code}")

        # 构建对应的输出文件路径
        output_file_path = os.path.join(output_folder, json_file)

        # 将更新后的数据保存回JSON文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f'{json_file} 已成功处理并保存为 {output_file_path}')