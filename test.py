import os
import subprocess
import sys

def test(PROG, NAME):

    # prog_name = PROG.lower()
    with open(f"test/{PROG}.{NAME}.in", "r") as in_file:
        try:
            input_file = in_file.read()
            result = subprocess.run(input_file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  
            if result.returncode != 0:
                print(f"FAIL: {PROG} {NAME} failed (TestResult.ExitStatus): non-zero exit status")


            expected_output_file = f"test/{PROG}.{NAME}.out"
            with open(expected_output_file, "r") as out_file:
                expected_output = out_file.read()

            if result.stdout != expected_output:
                print(f"FAIL: {PROG} {NAME} failed (TestResult.OutputMismatch)")
                print("      expected:\n")
                print(expected_output)
                print("\n      got:\n")
                print(result.stdout)
                return True

            print(f"OK: {PROG}.{NAME}")
            return False

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    total_tests = 0
    failed_tests = 0

    for test_file in os.listdir("test"):
        if test_file.endswith(".in"):
            PROG =  test_file.split(".")[0]
            NAME =  test_file.split(".")[1]
            total_tests += 1

            if test(PROG, NAME):
                failed_tests += 1
    
    print("\nOK: ", total_tests - failed_tests)
    print("\noutput mismatch: ", failed_tests)
    print("\ntotal: ", total_tests)

    if failed_tests > 0:
        sys.exit(1)