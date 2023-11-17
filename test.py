import os
import subprocess
import sys

def test(PROG, NAME):
    prog_name = PROG.lower()
    process =  subprocess.Popen(["python3",f"prog/{prog_name}.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        with open(f"test/{PROG}.{NAME}.in", "r") as in_file:
            input_file = in_file.read()
            stdout, stderr = process.communicate(input=input_file)

        if process.returncode != 0:
            print(f"FAIL: {PROG} {NAME} failed (TestResult.ExitStatus): non-zero exit status")

        expected_output_file = f"test/{PROG}.{NAME}.out"
        with open(expected_output_file, "r") as out_file:
            expected_output = out_file.read()
        
       
        if stdout != expected_output:
            print(f"FAIL: {PROG} {NAME} failed (TestResult.OutputMismatch)")
            print("      expected:\n")
            print(expected_output)
            print("\n           got:\n")
            print(stdout)
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