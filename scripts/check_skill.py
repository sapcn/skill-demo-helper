#!/usr/bin/env python3
"""
Skill 结构检查脚本

用于验证 skill 是否符合基本标准。
"""

import os
import sys
from pathlib import Path

def check_skill(skill_path: str) -> dict:
    """检查 skill 结构"""
    result = {
        "valid": True,
        "errors": [],
        "warnings": [],
        "info": {}
    }

    skill_dir = Path(skill_path)

    # 检查目录是否存在
    if not skill_dir.exists():
        result["valid"] = False
        result["errors"].append(f"目录不存在: {skill_path}")
        return result

    # 检查 SKILL.md
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        result["valid"] = False
        result["errors"].append("缺少 SKILL.md 文件")
        return result

    # 读取 SKILL.md 检查 frontmatter
    try:
        content = skill_md.read_text(encoding="utf-8")
        if not content.startswith("---"):
            result["errors"].append("SKILL.md 缺少 YAML frontmatter (应该以 --- 开头)")
            result["valid"] = False
        else:
            # 检查是否包含 name 和 description
            has_name = "name:" in content[:500]
            has_desc = "description:" in content[:500]
            if not has_name:
                result["errors"].append("YAML frontmatter 缺少 name 字段")
                result["valid"] = False
            if not has_desc:
                result["errors"].append("YAML frontmatter 缺少 description 字段")
                result["valid"] = False

        # 统计行数
        lines = content.count("\n")
        result["info"]["skill_md_lines"] = lines
        if lines > 500:
            result["warnings"].append(f"SKILL.md 过长 ({lines} 行)，建议控制在 500 行以内")

    except Exception as e:
        result["errors"].append(f"读取 SKILL.md 失败: {e}")
        result["valid"] = False

    # 检查资源目录
    for dir_name in ["scripts", "references", "assets"]:
        dir_path = skill_dir / dir_name
        if dir_path.exists():
            count = len(list(dir_path.iterdir()))
            result["info"][f"{dir_name}_count"] = count

    # 检查不应存在的文件
    unwanted_files = ["README.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md"]
    for fname in unwanted_files:
        if (skill_dir / fname).exists():
            result["warnings"].append(f"不应包含文件: {fname}")

    return result

def main():
    if len(sys.argv) < 2:
        print("用法: python check_skill.py <skill-path>")
        print(f"示例: python check_skill.py C:\\Users\\YourName\\.claude\\skills\\my-skill")
        sys.exit(1)

    result = check_skill(sys.argv[1])

    print(f"\n{'='*50}")
    print("Skill 检查结果")
    print(f"{'='*50}\n")

    if result["valid"]:
        print("状态: 通过")
    else:
        print("状态: 未通过")

    print("\n信息:")
    for k, v in result["info"].items():
        print(f"  {k}: {v}")

    if result["warnings"]:
        print("\n警告:")
        for w in result["warnings"]:
            print(f"  - {w}")

    if result["errors"]:
        print("\n错误:")
        for e in result["errors"]:
            print(f"  - {e}")

    print(f"\n{'='*50}\n")

    sys.exit(0 if result["valid"] else 1)

if __name__ == "__main__":
    main()
