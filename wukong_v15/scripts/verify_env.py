import sys
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print("sys.path:")
for path in sys.path:
    print(f"  {path}")
