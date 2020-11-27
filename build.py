# -*- coding: utf-8 -*-

import os
import sys
from yapf.yapflib.yapf_api import FormatFile

MAGIC_COMMENT = "# BUILD_IGNORE\n"


def build(scanner_path):
    scanner_name = scanner_path.replace("_", " ").title()
    output_path = os.path.join(".", "build", scanner_name + ".py")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as output:
        append_file(output, 'base_scanner.py')
        append_file(output, scanner_path + ".py")

    format_file(output_path)
    print(f"built distribution at {output_path}")


def format_file(path):
    FormatFile(path, in_place=True, style_config=".style.yapf")


def append_file(output, file_path):
    with open(file_path, "r") as file:
        for line in file:
            if not line.endswith(MAGIC_COMMENT): output.write(line)
    pass


if __name__ == '__main__':
    build(sys.argv[1])
