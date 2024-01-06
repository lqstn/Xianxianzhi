import os
import csv
import json

# 获取所有CSV文件的文件名
csv_folder = './mydata/records/record_csv'  # 替换成你的CSV文件所在的文件夹路径
json_folder = './mydata/records/record_json'  # 替换成你想保存JSON文件的文件夹路径

# 确保目标文件夹存在，如果不存在就创建
os.makedirs(json_folder, exist_ok=True)

# 遍历CSV文件夹中的每个文件
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith('.csv'):
        csv_file_path = os.path.join(csv_folder, csv_file)

        # 构建对应的JSON文件路径
        json_file_path = os.path.join(json_folder, f'{os.path.splitext(csv_file)[0]}.json')

        data = []

        # 读取CSV文件
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            # 遍历CSV文件的每一行
            for row in csv_reader:
                # 将每一行数据添加到列表
                data.append(row)

        # 将数据写入JSON文件
        with open(json_file_path, 'w', encoding='utf-8') as file:
            # 使用json.dump将数据写入JSON文件
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f'{csv_file} 已成功转换为 {json_file_path}')
