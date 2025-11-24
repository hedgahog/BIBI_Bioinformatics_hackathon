import sys
import subprocess
from pathlib import Path

from python.streamlit_ui import run_streamlit


def run_streamlit():
    app = Path(__file__).with_name("streamlit_ui.py").resolve()
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(app)], check=True)


if __name__ == "__main__":
    run_streamlit()
