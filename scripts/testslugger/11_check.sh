#!/bin/sh

python3 generateTableOfContentEntries.py input.md > output.md

# diff -y -W 200 --color=always output.md expectedOutput.md
diff --color=always output.md expectedOutput.md
