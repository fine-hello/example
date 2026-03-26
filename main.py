# main.py:负责整体流程控制
import config
import spider
import storage
import time
from tqdm import tqdm  

def run():
    print("🚀 正在启动 ZOL 手机行情采集系统...")
    all_data = []
    max_pages = 5 # 建议先爬 5 页试试
    
    pbar = tqdm(total=max_pages, desc="🚚 采集进度", unit="页")
    
    next_url = config.BASE_URL
    page_count = 1
    
    while next_url and page_count <= max_pages:
        html = spider.get_html(next_url)
        if not html:
            break
            
        items = spider.parse_books(html)
        all_data.extend(items)
        
        pbar.set_postfix({"已抓取": f"{len(all_data)}条"})
        pbar.update(1)
        
        next_url = spider.get_next_page_url(html, next_url)
        page_count += 1
        time.sleep(1.5) # 电商站建议稍微慢一点

    pbar.close()

    if all_data:
        storage.save_to_csv(all_data, config.OUTPUT_FILE)
        print(f"\n✨ 任务圆满完成！")
    else:
        print("\n❌ 抓取失败，请检查网络或 config.py 中的选择器。")

if __name__ == "__main__":
    run()
