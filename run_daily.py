# run_daily.py
from pathlib import Path
import papermill as pm
from nbconvert import HTMLExporter

NB_IN  = "WFO_test_no_out.ipynb"
NB_OUT = "WFO_test_no_out_out.ipynb"
KERNEL_NAME = "gha-py311"   # <<< ใช้ชื่อเดียวกับที่ลงทะเบียนใน workflow

def render_html(nb_path: str, html_path: str):
    exp = HTMLExporter()
    exp.exclude_input = False
    exp.exclude_output_prompt = True
    body, _ = exp.from_filename(nb_path)
    Path(html_path).write_text(body, encoding="utf-8")

def main():
    pm.execute_notebook(
        input_path=NB_IN,
        output_path=NB_OUT,
        parameters={},
        kernel_name=KERNEL_NAME,   # <<< ใช้ชื่อ kernel ที่เราลงทะเบียน
    )
    Path("docs").mkdir(exist_ok=True)
    render_html(NB_OUT, "docs/index.html")

if __name__ == "__main__":
    main()
