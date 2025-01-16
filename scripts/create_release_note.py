import sys
import pathlib
import re
import datetime

def replace_links(text):
   text = re.sub(r'(?<!\[`)\#(\d+)(?!\))', r'[`#\1`](https://github.com/OpenLineage/OpenLineage/pull/\1)', text)
   text = re.sub(r'(?<!\[)@(\w+)(?!\))', r'[@\1](https://github.com/\1)', text)
   return text

def main(tag, date, content):
    # Count the number of .md files in the directory
    releases_dir = pathlib.Path(__file__).resolve().parent / '../docs/releases'
    md_files_count = len(list(releases_dir.glob('*.md')))
    
    # Calculate sidebar_position
    sidebar_position = 10000 - md_files_count - 1
    
    # Create new .md file
    filename = f"{tag.replace('.', '_')}.md"
    new_file_path = releases_dir / filename
    
    # Replace links in the content
    content = replace_links(content.replace("\\r\\n", "\r\n"))
    
    # Extract formatted date from date string in following format 2025-01-16T12:17:08Z
    date = datetime.datetime.fromisoformat(date[:-1]).strftime('%Y-%m-%d')
    
    # Template for the new .md file
    template = f"""---
title: {tag}
sidebar_position: {sidebar_position}
---

# {tag} - {date}

{content}
"""
    # Write the content to the new file
    new_file_path.write_text(template)
    print(f"Release note created: {new_file_path}")
    print(template)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: create_release_note.py <tag> <date> <content>")
        sys.exit(1)
    
    tag = sys.argv[1]
    date = sys.argv[2]
    content = sys.argv[3]
    
    main(tag, date, content)
