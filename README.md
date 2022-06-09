# leetcode-problems

My solutions to some leetcode.com coding problems, mostly Python/Go.

## Repository Structure

The directory `name` corresponds to the problem reachable under `https://leetcode.com/problems/<name>/`.
For example to see the description of `jewels-and-stones` go to https://leetcode.com/problems/jewels-and-stones/

My submitted revisions are called `one.py`, `two.py`, etc. (`v1.py`/`go` for newer ones).

Most of the solutions contain the result as a comment on the bottom of the file, for example:

```python
# Runtime: 96 ms, faster than 98.07% of Python3 online submissions for Array Partition I.
# Memory Usage: 15.2 MB, less than 5.20% of Python3 online submissions for Array Partition I.
```

Note that runtime and memory usage given by Leetcode isn't very consistent between runs of the same code.
Sometimes runs a few months later also take longer due to newly added test cases or version upgrades.

## Formatting

```shell
# install git hook
pip install pre-commit
pre-commit install

# run manually
pre-commit run --all-files
```

This autoformats the following code files: Python, C++, Golang.
