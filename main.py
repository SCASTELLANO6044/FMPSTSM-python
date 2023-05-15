import os
import time
import Memoization
import Tabulation
import sys

def __read_matrix_from_file__(file_name):
    with open(file_name, 'r') as f:
        rows = int(f.readline().strip())
        matrix = []
        for _ in range(rows):
            line = f.readline().strip().split(" ")
            row = [int(x) for x in line]
            matrix.append(row)
    return matrix

tab = False
mem = False
both = False
isDirectory = False

valid_first = ["-d", "--directory", "-f", "--file", "-h", "--help"]
valid_second = ["-sm", "--memoization", "-st", "--tabulation", "--check"]


if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("usage: FMPSTSM.exe [-h] [-d [DIRECTORY] | -f [FILE]] [-sm | -st | -check] [-t]\n\n" +
                "optional arguments:\n" +
                "    -h, --help                                  Show this help message and exit\n" +
                "    -d [DIRECTORY], --directory [DIRECTORY]     Process many files in a directory\n" +
                "    -f [FILE], --file [FILE]                    Process a single file\n" +
                "    -sm, --memoization                          Find the minimum path sum in a triangle-shaped matrix\n" +
                "                                                   through Memoization\n" +
                "    -st, --tabulation                           Find the minimum path sum in a triangle-shaped matrix\n" +
                "                                                   through Tabulation\n" +
                "    -check                                      Check that the minimum path sum in a triangle-shaped matrix\n" +
                "                                                   is the same through Tabulation and Memoization\n")
elif sys.argv[1] not in valid_first or sys.argv[3] not in valid_second:
    print("No ha escrito los parámetros de entrada del programa correctamente:\n"
          "usage: FMPSTSM.exe [-h] [-d [DIRECTORY] | -f [FILE]] [-sm | -st | -check] [-t]\n\n" +
                "optional arguments:\n" +
                "    -h, --help                                  Show this help message and exit\n" +
                "    -d [DIRECTORY], --directory [DIRECTORY]     Process many files in a directory\n" +
                "    -f [FILE], --file [FILE]                    Process a single file\n" +
                "    -sm, --memoization                          Find the minimum path sum in a triangle-shaped matrix\n" +
                "                                                   through Memoization\n" +
                "    -st, --tabulation                           Find the minimum path sum in a triangle-shaped matrix\n" +
                "                                                   through Tabulation\n" +
                "    -check                                      Check that the minimum path sum in a triangle-shaped matrix\n" +
                "                                                   is the same through Tabulation and Memoization\n")
else:
    second_param = ""
    if sys.argv[1] == valid_first[0] or sys.argv[1] == valid_first[1]:
        isDirectory = True
        second_param = sys.argv[2]
        print(second_param)
    elif sys.argv[1] == valid_first[2] or sys.argv[1] == valid_first[3]:
        second_param = sys.argv[2]

    if sys.argv[3] == valid_second[4]:
        both = True
    elif sys.argv[3] == valid_second[0] or sys.argv[3] == valid_second[1]:
        mem = True
    elif sys.argv[3] == valid_second[2] or sys.argv[3] == valid_second[3]:
        tab = True

    def __fmpstsm_in_file__(file_name):
        t = time.time()

        matrix = __read_matrix_from_file__(file_name)

        if both:
            print("Memoization: ")
            print(Memoization.execute(matrix))
            print("****************************************************")
            print("Tabulation: ")
            print(Tabulation.execute(matrix))
        elif tab:
            print("Tabulation: ")
            print(Tabulation.execute(matrix))
        elif mem:
            print("Memoization: ")
            print(Memoization.execute(matrix))

        final_time = time.time() - t
        formatted_time = "{:.4f}".format(final_time)
        print("Tiempo: " +str(formatted_time))
        print("\n"+"-----------------------------------"+"\n")

    if isDirectory:
        files = []
        for path in os.listdir(second_param):
            if os.path.isfile(os.path.join(second_param, path)):
                files.append(path)
        for file in files:
            print("Using: "+file+" as input")
            __fmpstsm_in_file__(second_param + file)
    else:
        __fmpstsm_in_file__(second_param)
