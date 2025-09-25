# run_daily.py
from pathlib import Path
import papermill as pm
import nbconvert
from nbconvert import HTMLExporter
import nbformat

NB_IN  = "WFO_test_no_out.ipynb"
NB_OUT = "WFO_test_no_out_out.ipynb"

def render_html(nb_path: str, html_path: str):
    # แปลง ipynb เป็น HTML แบบ standalone
    exporter = HTMLExporter()
    exporter.exclude_input = False      # อยากซ่อน input เซลล์ = True
    exporter.exclude_output_prompt = True
    body, _ = exporter.from_filename(nb_path)
    Path(html_path).write_text(body, encoding="utf-8")

def main():
    # 1) รันโน้ตบุ๊ก (ถ้าต้องส่งพารามิเตอร์ให้ใส่ใน dict parameters={...})
    pm.execute_notebook(
        input_path=NB_IN,
        output_path=NB_OUT,
        parameters={}
    )

    # 2) สร้าง docs/ และทำ index.html จากโน้ตบุ๊กที่เพิ่งรัน
    docs = Path("docs")
    docs.mkdir(exist_ok=True)
    render_html(NB_OUT, str(docs / "index.html"))

if __name__ == "__main__":
    main()
