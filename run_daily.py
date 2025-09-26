# run_daily.py
import os
from pathlib import Path
import papermill as pm
from nbconvert import HTMLExporter

NB_IN  = "WFO_test_no_out.ipynb"
NB_OUT = "WFO_test_no_out_out.ipynb"

def render_html(nb_path: str, html_path: str):
    exp = HTMLExporter()
    exp.exclude_input = False        # จะซ่อนโค้ดให้เปลี่ยนเป็น True
    exp.exclude_output_prompt = True
    body, _ = exp.from_filename(nb_path)
    Path(html_path).write_text(body, encoding="utf-8")

def main():
    kernel = os.environ.get("KERNEL_NAME", "gha-py311")   # <<< อ่านจาก ENV
    print(f"[run_daily] Using kernel: {kernel}")

    pm.execute_notebook(
        input_path=NB_IN,
        output_path=NB_OUT,
        parameters={},
        kernel_name=kernel,           # <<< ส่งชื่อ kernel ที่แน่ใจว่ามี
    )

    Path("docs").mkdir(exist_ok=True)
    render_html(NB_OUT, "docs/index.html")

if __name__ == "__main__":
    main()
