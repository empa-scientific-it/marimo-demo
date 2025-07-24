import subprocess
import inspect
import pathlib


def run_tests(test_name: str, test_file: str = None) -> str:
    if test_file is None:
        # Get the caller's file (the notebook .py)
        frame = inspect.stack()[1]
        caller_file = pathlib.Path(frame.filename)
        test_file = caller_file.stem

    result = subprocess.run(
        [
            "uv",
            "run",
            "--with",
            ".[test]",
            "pytest",
            f"tests/test_{test_file}.py",
            "-k",
            f"test_{test_name}",
            "-v",
            "--tb=short",
            "--maxfail=1",
        ],
        capture_output=True,
        text=True,
    )

    return result.stdout
