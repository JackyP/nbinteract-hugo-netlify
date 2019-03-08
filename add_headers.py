""" Iterates over html files and adds header """
import glob
import json
import re
import os
import time

for notebook_file in glob.glob("content/posts/*.ipynb"):
    # Get details:
    with open(notebook_file, "r") as f:
        notebook_json = json.load(f)

        pattern = re.compile("ipynb", re.IGNORECASE)
        title = pattern.sub("", os.path.basename(f.name)).replace(".", " ")
        date = time.strftime(
            "%Y-%m-%dT%H:%M:%S+00:00",
            time.gmtime(
                os.path.getmtime(notebook_file)
            )
        )
        description = " ".join(notebook_json["cells"][0]["source"]).replace("\n", "")
        f.close()

    # Make template
    header_template = f"""+++
title =  "{title}"
date = {date}
tags = []
featured_image = ""
description = "{description}"
+++"""

    pattern = re.compile("ipynb", re.IGNORECASE)

    html_file = pattern.sub("html", notebook_file)

    print(html_file)

    with open(html_file, "r+") as f:
        contents = f.read()
        f.seek(0)
        f.write(header_template + contents)
        f.truncate()
        f.close()
