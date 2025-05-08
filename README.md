# 网站内容关键词检测工具

这是一个用于批量检测网站内容是否包含特定关键词的Python工具。该工具可以读取Excel文件中的网站URL列表，访问每个网站，并检查网站内容是否包含预设的关键词，最后将检测结果导出为Excel文件。

## 功能特点

- 读取Excel文件中的网站URL列表
- 自动访问网站并获取网页内容
- 支持URL格式自动修正（添加http://前缀）
- 支持网页编码自动检测
- 检查网页内容是否包含指定关键词
- 检测结果保存到新的Excel文件中
- 显示检测进度和结果统计

## 安装步骤

1. 确保已安装Python 3.6或更高版本
2. 克隆此仓库到本地：
   ```
   git clone https://github.com/loveyxh/website_keyword_analysis_python.git
   cd 网站内容关键词检测工具
   ```
3. 安装所需依赖包：
   ```
   pip install -r requirements.txt
   ```

   依赖包包括：
   - pandas>=1.3.0：用于Excel数据处理
   - requests>=2.26.0：用于网站内容获取
   - openpyxl>=3.0.9：用于Excel文件读写

## 项目结构

```
网站内容关键词检测工具/
├── website_analysis.py       # 主程序文件
├── requirements.txt          # 依赖包列表
├── README.md                 # 项目说明文档
└── 网站列表_样例数据.xlsx  # 示例输入文件
```

## 运行方法

1. 准备一个包含网站URL的Excel文件，确保文件中有名为'media_url'的列
2. 编辑`website_analysis.py`文件，根据需要修改`KEYWORDS`列表中的关键词
3. 运行脚本：
   ```
   python website_analysis.py
   ```
4. 脚本将读取默认的Excel文件（网站列表_样例数据.xlsx），并生成一个新的带有分析结果的Excel文件

### 自定义输入文件

如需使用其他Excel文件作为输入，可以修改`main()`函数中的`excel_file`变量：

```python
# 读取Excel文件
excel_file = "网站列表_样例数据.xlsx"
```

## 输出结果

脚本运行完成后，将在同一目录下生成一个新的Excel文件，文件名格式为：
`原文件名_分析结果_时间戳.xlsx`

该文件包含原始数据及新增的`match_result`列，值为1表示网站内容包含关键词，值为0表示不包含。 
