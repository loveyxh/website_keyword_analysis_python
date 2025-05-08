import pandas as pd
import requests
import time
from datetime import datetime
import os

# 关键词列表
KEYWORDS = ['关键词1', '关键词2']

def get_website_content(url):
    """获取网站源代码，支持跳转链接"""
    if not url or not isinstance(url, str):
        return ""
    
    # 确保URL格式正确
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        response.raise_for_status()
        
        # 尝试检测编码
        if response.encoding == 'ISO-8859-1':
            response.encoding = response.apparent_encoding
        
        return response.text
    except Exception as e:
        print(f"获取网站 {url} 内容失败: {e}")
        return ""

def check_keywords(content, keywords):
    """检查内容是否包含关键词"""
    if not content:
        return False
    
    for keyword in keywords:
        if keyword in content:
            return True
    
    return False

def analyze_websites(df):
    """分析网站内容并检查关键词"""
    # 确保存在media_url列
    if 'media_url' not in df.columns:
        print("错误: 数据中没有'media_url'列")
        return df
    
    # 添加match_result列，默认为0
    df['match_result'] = 0
    
    total = len(df)
    for i, row in df.iterrows():
        url = row['media_url']
        print(f"处理 {i+1}/{total}: {url}")
        
        # 获取网站内容
        content = get_website_content(url)
        
        # 检查关键词
        if check_keywords(content, KEYWORDS):
            df.at[i, 'match_result'] = 1
            print(f"✓ 网站 {url} 命中关键词")
        else:
            print(f"✗ 网站 {url} 未命中关键词")
        
        # 避免请求过于频繁
        time.sleep(1)
    
    return df

def export_to_excel(df, original_file):
    """将结果导出到Excel文件"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.splitext(original_file)[0]
    filename = f"{base_name}_分析结果_{timestamp}.xlsx"
    
    try:
        df.to_excel(filename, index=False)
        print(f"结果已导出到文件: {filename}")
        return filename
    except Exception as e:
        print(f"导出Excel失败: {e}")
        return None

def main():
    """主函数"""
    print("开始网站数据分析...")
    
    # 读取Excel文件
    excel_file = "网站列表_样例数据.xlsx"
    try:
        df = pd.read_excel(excel_file)
        print(f"成功读取Excel文件，共 {len(df)} 条记录")
    except Exception as e:
        print(f"读取Excel文件失败: {e}")
        return
    
    # 分析网站内容
    df = analyze_websites(df)
    
    # 导出结果到Excel
    export_to_excel(df, excel_file)
    
    print("网站数据分析完成")

if __name__ == "__main__":
    main()