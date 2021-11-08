#!/usr/bin/env bash

markdown_file="docs/result.md"
python_dirs=""

for dir in $(echo src/*/)
do
    if [[ -n $(find "$dir" -name '*.py') ]]; then
        python_dirs+="${dir} "
        echo "found Python dir: $dir"
    fi
done

if [[ -z $python_dirs ]]; then
    echo "no Python modules found, cannot generate documentation, exiting..."
    exit 1
fi

echo "$python_dirs"

pdoc --pdf --force --output-dir docs/ $python_dirs > $markdown_file
awk -i inplace '{sub(/{#id}/, sprintf("{#id%d}", ++i))} 1' $markdown_file
