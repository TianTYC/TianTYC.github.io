from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
import time

def setup_proxy():
    """设置代理以避免被 Google 阻止"""
    try:
        pg = ProxyGenerator()
        # 使用免费代理
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        print("Proxy setup successful")
        return True
    except Exception as e:
        print(f"Proxy setup failed: {e}")
        return False

def fetch_scholar_data(scholar_id, max_retries=3):
    """获取学者数据，带重试机制"""
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}/{max_retries}: Fetching data for {scholar_id}")
            
            # 搜索作者
            author = scholarly.search_author_id(scholar_id)
            
            # 填充详细信息
            scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
            
            return author
            
        except AttributeError as e:
            print(f"AttributeError (likely blocked by Google): {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 10
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
                # 重新设置代理
                setup_proxy()
            else:
                raise
                
        except Exception as e:
            print(f"Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                raise
    
    return None

def main():
    try:
        # 获取环境变量
        scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
        if not scholar_id:
            raise ValueError("GOOGLE_SCHOLAR_ID environment variable not set")
        
        print(f"Starting to fetch Google Scholar data for ID: {scholar_id}")
        
        # 设置代理
        setup_proxy()
        
        # 获取作者数据
        author = fetch_scholar_data(scholar_id)
        
        if not author:
            raise Exception("Failed to fetch author data after all retries")
        
        # 处理数据
        name = author.get('name', 'Unknown')
        print(f"Successfully fetched data for: {name}")
        
        author['updated'] = str(datetime.now())
        
        # 转换 publications 为字典
        if 'publications' in author and isinstance(author['publications'], list):
            author['publications'] = {
                v.get('author_pub_id', f'pub_{i}'): v 
                for i, v in enumerate(author['publications'])
            }
        
        # 创建结果目录
        os.makedirs('results', exist_ok=True)
        
        # 保存完整数据
        print("Saving data to gs_data.json...")
        with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(author, outfile, ensure_ascii=False, indent=2)
        
        # 保存 shields.io 格式数据
        citations = author.get('citedby', 0)
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{citations}",
        }
        
        print("Saving data to gs_data_shieldsio.json...")
        with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
            json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)
        
        # 打印摘要
        print("\n" + "="*50)
        print("SUCCESS! Citation data updated:")
        print(f"  Name: {name}")
        print(f"  Citations: {citations}")
        print(f"  h-index: {author.get('hindex', 'N/A')}")
        print(f"  i10-index: {author.get('i10index', 'N/A')}")
        print(f"  Publications: {len(author.get('publications', {}))}")
        print("="*50 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("Creating fallback data file...")
        
        # 创建备用数据文件，避免完全失败
        os.makedirs('results', exist_ok=True)
        
        fallback_data = {
            'error': str(e),
            'updated': str(datetime.now()),
            'citedby': 0,
            'name': 'Error fetching data'
        }
        
        with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(fallback_data, outfile, ensure_ascii=False, indent=2)
        
        shieldio_fallback = {
            "schemaVersion": 1,
            "label": "citations",
            "message": "error",
        }
        
        with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
            json.dump(shieldio_fallback, outfile, ensure_ascii=False, indent=2)
        
        # 不抛出异常，让工作流继续
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
