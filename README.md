# kattis-test
Quickly test your code on the input/output samples provided in a kattis problem description before submitting your solution.

# Installation
Run `git clone https://https://github.com/wkrill/kattis-test` to clone the repository.

To run the client as a command from anywhere on your file system, you need to add the `kattis-test` directory to your `$PATH` variable.
On mac/linux this is done by adding the line `export PATH="$PATH:/path/to/kattis-cli` to your `.bash_profile` (or `.zshrc` if you use the Z shell).
Then you can run the client with the command `kattis-test hello.py`

# Usage
The client only works for *python* solutions. The easiest way to use the client is to name your solution *problem_id*.py.

E.g. assume you try to solve the [Aaah!](https://open.kattis.com/problems/aaah) problem (with id `aaah`) and your (possible) solution is `aaah.py`. Then running `kattis-test aaah.py` will run `aaah.py` with the two inputs `aaah\naaaaah` and `aaah\nah` and compare the results with the expected outputs `no` and `go` respectly. If there is a mismatch the computed and expected output is printed.

If the file name is not the problem id, then you can instead provide the id as a second argument. E.g. `kattis-test uuuh.py aaah`.
