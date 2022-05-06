import os
import re
import sys
from datetime import datetime
from typing import List

from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel


class Article(BaseModel):
    title: str
    tags: List[str]
    content: str


def search_prefix_in_lines(lines: List[str], prefix: str) -> List[int]:
    return [idx for idx, line in enumerate(lines) if line.strip().startswith(prefix)]


def extract_block(lines: List[str], start_idx: int, next_start_idx: int) -> Article:
    # ex. ### [a,b, c] this is title
    title_line = lines[start_idx]
    title = title_line[title_line.index("]") + 1 :].strip()

    found_tags = re.search("\[.+\]", title_line)
    if found_tags is None:
        msg = f'Cannot found tags in line{start_idx} with content "{title_line}"'
        raise ValueError(msg)
    tags = [tag.strip() for tag in found_tags.group(0)[1:-1].split(",")]

    content = "".join(lines[start_idx + 1 : next_start_idx])

    return Article(title=title, tags=tags, content=content)


def extract_weekly_page(filename: str) -> list:
    with open(filename, "r") as fp:
        lines = fp.readlines()

    h2_indexs = search_prefix_in_lines(lines, "## ")
    h3_indexs = search_prefix_in_lines(lines, "### ")

    if len(h2_indexs) != 2:
        msg = f"h2 tag must have Good/Other two elements only\nFound {len(h2_indexs)} in {filename}"
        raise ValueError(msg)

    blocks = [
        extract_block(lines, start_idx, next_start_idx - 1)
        for start_idx, next_start_idx in zip(h3_indexs[:-1], h3_indexs[1:])
    ]
    blocks.append(extract_block(lines, h3_indexs[-1], len(lines) - 1))

    return blocks


if __name__ == "__main__":
    # filename = 'content/posts/weekly/weekly_09.md'
    if len(sys.argv) != 2:
        raise OSError("Please input filename")
    filename = sys.argv[1]
    blog_folder = "content/posts/blogs/"

    date = datetime.utcnow()
    isodate = date.strftime("%Y-%m-%dT%H:%M:%S+08:00")

    print(f"=== Extract weekly file {filename} in {isodate}")
    blocks = extract_weekly_page(filename)

    env = Environment(
        loader=FileSystemLoader("src"),
    )
    template = env.get_template("blog_template.md")

    for block in blocks:
        render_doc = template.render(article=block, cur_time=isodate)
        title_without_space = block.title.replace(" ", "_")
        render_filename = os.path.join(blog_folder, f"{title_without_space}.md")
        print(f"=== Dump blog [{block.title}] to {render_filename}")
        with open(render_filename, "w") as fp:
            fp.write(render_doc)
