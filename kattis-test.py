#! python3

from html.parser import HTMLParser
import os
import subprocess
import sys

import requests


class IOSampleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attributes):
        if tag != 'pre':
            return
        self.recording = 1

    def handle_endtag(self, tag):
        self.recording = 0

    def handle_data(self, data):
        if self.recording:
            self.data.append(data)


def fetch_io_samples(problem):
    '''Fetches the example pairs of inputs and expected outputs available in
    the problem description at open.kattis.org.

    Argument:
    problem -- the problem ID

    Returns:
    List of the form [i1, o1, i2, o2, ... ] containing the I/O strings
    '''
    # print('Fetching I/O samples for problem', problem)
    try:
        r = requests.get('https://open.kattis.com/problems/' + problem)
        # print('Done')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    parser = IOSampleParser()
    parser.feed(r.text)
    return parser.data


def test_script(fname, io_samples):
    """Runs python script specified by 'fname' on inputs from io_samples and
    compares output to the expected outputs.

    Arguments:
    fname -- name of the python script '/path/to/script.py'.
    io_samples -- list [i1, o1, i2, o2, ... ] containing the I/O strings
    """
    bash_cmd = ["python3", fname]
    for i in range(len(io_samples)//2):
        inp = io_samples[2*i]
        out = io_samples[2*i + 1]
        print('='*20)
        print()
        print('Testing input',i+1)
        process = subprocess.run(bash_cmd, input=inp,
                                 text=True, capture_output=True)
        if process.stdout == out:
            print('Success')
            print()
        else:
            print('Failure')
            print('Input:')
            print(inp)

            print('Output:')
            print(process.stdout)
            print('Expected output:')
            print(out)


def main():
    fname = sys.argv[1]
    if len(sys.argv) > 2:
        problem = sys.argv[2]
    else:
        problem, ext = os.path.splitext(os.path.basename(fname))
    io_samples = fetch_io_samples(problem)
    test_script(fname,io_samples)


if __name__ == '__main__':
    main()
