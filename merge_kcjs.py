import argparse
import os
import re
from pathlib import Path


CH_NUM_MAP = {
    "零": 0,
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
}


def chinese_num_to_int(text: str) -> int:
    if not text:
        return -1
    if text.isdigit():
        return int(text)
    if text == "十":
        return 10
    if text.startswith("十") and len(text) == 2:
        return 10 + CH_NUM_MAP.get(text[1], 0)
    if len(text) == 2 and text[1] == "十":
        return CH_NUM_MAP.get(text[0], 0) * 10
    if len(text) == 3 and text[1] == "十":
        return CH_NUM_MAP.get(text[0], 0) * 10 + CH_NUM_MAP.get(text[2], 0)
    return -1


def extract_chapter_number(name: str) -> int:
    m = re.search(r"第(.+?)章", name)
    if not m:
        return -1
    return chinese_num_to_int(m.group(1))


def iter_md_files(root: Path, keyword: str, output: Path):
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            if keyword not in fn:
                continue
            path = Path(dirpath) / fn
            if path.resolve() == output.resolve():
                continue
            yield path


def sort_key(path: Path):
    name = path.name
    chapter = extract_chapter_number(name)
    return (chapter if chapter >= 0 else 999, name)


def merge_files(files, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as out:
        out.write("# 【考场精简】汇总\n\n")
        for idx, path in enumerate(files, 1):
            title = path.stem
            out.write(f"\n---\n\n## {title}\n\n")
            content = path.read_text(encoding="utf-8").strip()
            out.write(content)
            out.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Merge 考场精简 markdown files into one document.")
    parser.add_argument(
        "-d",
        "--dir",
        default="数据库期末复习资料",
        help="Root directory to search for files (default: 数据库期末复习资料)",
    )
    parser.add_argument(
        "-k",
        "--keyword",
        default="考场精简",
        help="Filename keyword filter (default: 考场精简)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="数据库期末复习资料/【考场精简】汇总.md",
        help="Output markdown path",
    )
    args = parser.parse_args()

    root = Path(args.dir)
    output = Path(args.output)

    files = sorted(iter_md_files(root, args.keyword, output), key=sort_key)
    if not files:
        raise SystemExit(f"No markdown files found in {root} with keyword '{args.keyword}'.")
    merge_files(files, output)
    print(f"Merged {len(files)} files into {output}")


if __name__ == "__main__":
    main()
