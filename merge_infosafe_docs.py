"""
信息安全文档整合脚本
将信安1-6的md文件整合成一个完整的文档
"""

import os
from datetime import datetime

def merge_infosafe_docs(input_folder="infosafe", output_file="信息安全_完整版.md"):
    """
    整合信安1-6的md文件到一个大文档
    
    Args:
        input_folder: 输入文件夹路径
        output_file: 输出文件名
    """
    
    # 定义要整合的文件（按顺序）
    files_to_merge = [
        "信安1_信息安全基础.md",
        "信安2_密码学基础.md",
        "信安3_数字签名与认证.md",
        "信安4_操作系统与数据库安全.md",
        "信安5_网络安全协议与技术.md",
        "信安6_恶意代码与APT攻击.md"
    ]
    
    print("="*60)
    print("信息安全文档整合工具")
    print("="*60)
    print()
    
    # 创建输出内容列表
    merged_content = []
    
    # 添加文档头部
    merged_content.append("# 信息安全期末复习 - 完整版\n\n")
    merged_content.append("> 本文档整合自课程图片内容 + 《信息安全复习资料.md》\n")
    merged_content.append(f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    merged_content.append("---\n\n")
    
    # 添加目录
    merged_content.append("## 📑 目录\n\n")
    for i, filename in enumerate(files_to_merge, 1):
        chapter_name = filename.replace(".md", "").replace("信安", "第").replace("_", "章 ")
        merged_content.append(f"{i}. [{chapter_name}](#{i})\n")
    merged_content.append("\n---\n\n")
    
    # 逐个读取并合并文件
    for i, filename in enumerate(files_to_merge, 1):
        filepath = os.path.join(input_folder, filename)
        
        if not os.path.exists(filepath):
            print(f"⚠️  警告: 文件不存在 - {filename}")
            continue
        
        print(f"正在处理 [{i}/{len(files_to_merge)}]: {filename}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 添加章节分隔
            merged_content.append(f"\n<div id=\"{i}\"></div>\n\n")
            merged_content.append("="*80 + "\n\n")
            
            # 添加文件内容
            merged_content.append(content)
            
            # 添加章节结束标记
            merged_content.append("\n\n" + "="*80 + "\n\n")
            
            # 添加返回目录链接
            merged_content.append("[⬆️ 返回目录](#-目录)\n\n")
            merged_content.append("---\n\n")
            
        except Exception as e:
            print(f"❌ 错误: 处理 {filename} 时出错 - {str(e)}")
            continue
    
    # 添加文档尾部
    merged_content.append("\n\n---\n\n")
    merged_content.append("## 📌 文档说明\n\n")
    merged_content.append("**本文档包含以下章节：**\n\n")
    for i, filename in enumerate(files_to_merge, 1):
        chapter_name = filename.replace(".md", "").split("_")[1]
        merged_content.append(f"- 第{i}章：{chapter_name}\n")
    
    merged_content.append("\n**来源：**\n")
    merged_content.append("- 课程PPT图片（61张）\n")
    merged_content.append("- 《信息安全复习资料.md》\n")
    merged_content.append("- 老师课堂强调内容\n\n")
    
    merged_content.append("**使用建议：**\n")
    merged_content.append("1. 先看目录了解整体结构\n")
    merged_content.append("2. 优先复习标注⭐⭐⭐⭐⭐的必考内容\n")
    merged_content.append("3. 结合《信息安全复习资料.md》深入学习\n")
    merged_content.append("4. 重要知识点对照原始图片验证\n\n")
    
    merged_content.append("---\n\n")
    merged_content.append("**祝复习顺利！考试加油！🎓**\n\n")
    merged_content.append(f"*文档生成时间: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}*\n")
    
    # 写入输出文件
    output_path = os.path.join(input_folder, output_file)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(merged_content)
        
        print()
        print("="*60)
        print("✅ 整合完成！")
        print(f"📄 输出文件: {output_path}")
        print(f"📊 总共整合了 {len(files_to_merge)} 个章节")
        
        # 计算文件大小
        file_size = os.path.getsize(output_path)
        if file_size < 1024:
            size_str = f"{file_size} B"
        elif file_size < 1024 * 1024:
            size_str = f"{file_size / 1024:.2f} KB"
        else:
            size_str = f"{file_size / (1024 * 1024):.2f} MB"
        
        print(f"💾 文件大小: {size_str}")
        print("="*60)
        
    except Exception as e:
        print()
        print("="*60)
        print(f"❌ 错误: 写入文件时出错 - {str(e)}")
        print("="*60)

def main():
    """主函数"""
    # 检查输入文件夹是否存在
    if not os.path.exists("infosafe"):
        print("❌ 错误: 找不到 'infosafe' 文件夹")
        return
    
    # 执行整合
    merge_infosafe_docs()

if __name__ == "__main__":
    main()


