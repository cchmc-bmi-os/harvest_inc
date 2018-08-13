#!/usr/bin/env
import argparse

# from os import path
# dir_data='/users/labs9y/Projects/lpdr/data'
# filenames=['data100.csv', 'IBEMISProduction_DATA_2017-03-11_0603.csv', 'data200.csv']
# files=[path.join(dir_data, f) for f in filenames]

def get_first_line(fn):
        with open(fn, 'U') as f:
                l = f.readline()

        return(l)

def check_encoding(fn):
        l=get_first_line(fn)
        l30=l[0:30]
        print(l30)
        print(fn, l30, len(l30))
        try:
                l30=unicode(l30)
        except:
                raise Exception('*** Encoding problem! ***')

def check_files_encoding(files):
        for fn in files:
                check_encoding(fn)

def main():
        parser = argparse.ArgumentParser(description='Check file encoding by reading the first 30 characteres of the files and trying to cast it.')
        parser.add_argument('--file', dest='filename', help='Full path of file to be tested)')

        args = parser.parse_args()
        check_encoding(args.filename)

if __name__ == '__main__':
        main()
