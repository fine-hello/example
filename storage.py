# storage.py:负责数据存储
import csv

def save_to_csv(data, filename):
    if not data:
        print("⚠️ 没有数据需要保存")
        return False
    try:
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            # 定义中文表头
            field_map = {
                'title': '型号',
                'price': '价格',
                'price_raw': '原始价格',
                'score': '评分',
                'comments': '评价人数'
            }
            writer = csv.DictWriter(f, fieldnames=field_map.keys())
            
            # 写入自定义中文表头
            f.write("型号,价格,原始价格,评分,评价人数\n")
            writer.writerows(data)

        print(f"✅ 成功：数据已存入 {filename}（共 {len(data)} 条）")
        return True
    except Exception as e:
        print(f"❌ 存储失败: {e}")
        return False
