#!/bin/bash
# Complete PDF Export Workflow for Academic Paper
# Exports marimo notebook to publication-ready PDF with Quarto

set -e  # Exit on error

echo "📄 EV Patent Analysis - PDF Export Workflow"
echo "==========================================="
echo ""

echo "Step 1: Export marimo notebook to Jupyter format with outputs..."
uv run marimo export ipynb patent_analysis_chapter.py \
    -o patent_analysis_chapter.ipynb \
    --include-outputs \
    -f

echo "✓ Exported to Jupyter notebook with embedded outputs"
echo ""

echo "Step 2: Convert Vega-Lite charts to PNG images..."
uv run python << 'EOF'
import json
import altair as alt
import io
import base64

# Read the notebook
with open('patent_analysis_chapter.ipynb', 'r') as f:
    nb = json.load(f)

converted = 0
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and cell.get('outputs'):
        for output in cell['outputs']:
            if 'data' in output and 'application/vnd.vegalite.v5+json' in output['data']:
                try:
                    vega_spec = output['data']['application/vnd.vegalite.v5+json']
                    if isinstance(vega_spec, str):
                        vega_spec = json.loads(vega_spec)

                    # Increase chart dimensions for better readability
                    if 'width' in vega_spec:
                        vega_spec['width'] = int(vega_spec['width'] * 1.4)
                    if 'height' in vega_spec:
                        vega_spec['height'] = int(vega_spec['height'] * 1.4)
                    if 'spec' in vega_spec:
                        if 'width' in vega_spec['spec']:
                            vega_spec['spec']['width'] = int(vega_spec['spec']['width'] * 1.4)
                        if 'height' in vega_spec['spec']:
                            vega_spec['spec']['height'] = int(vega_spec['spec']['height'] * 1.4)

                    # Increase font sizes
                    if 'config' not in vega_spec:
                        vega_spec['config'] = {}
                    vega_spec['config'].update({
                        'axis': {'labelFontSize': 11, 'titleFontSize': 12},
                        'legend': {'labelFontSize': 11, 'titleFontSize': 12},
                        'title': {'fontSize': 13}
                    })

                    # Convert to PNG with high resolution
                    chart = alt.Chart.from_dict(vega_spec)
                    png_buffer = io.BytesIO()
                    chart.save(png_buffer, format='png', engine='vl-convert', scale_factor=2.0)
                    png_buffer.seek(0)
                    png_data = base64.b64encode(png_buffer.read()).decode('utf-8')

                    output['data']['image/png'] = png_data
                    output['data']['application/vnd.vegalite.v5+json'] = vega_spec
                    converted += 1
                except:
                    pass

print(f"✓ Converted {converted} charts to high-resolution PNG")

# Save modified notebook
with open('patent_analysis_chapter.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
EOF

echo ""
echo "Step 3: Reorder cells and add metadata..."
uv run python << 'EOF'
import json

with open('patent_analysis_chapter.ipynb', 'r') as f:
    nb = json.load(f)

# Move Table 1 (Statistical Significance) to after Figure 2
# Table 1 is originally at cell 22, move it to position 9 (after Figure 2)
table1_cell = nb['cells'].pop(22)
nb['cells'].insert(9, table1_cell)
print("✓ Moved Table 1 to after Figure 2")

# Add cell metadata to hide code
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        if 'metadata' not in cell:
            cell['metadata'] = {}
        cell['metadata']['echo'] = False
        cell['metadata']['warning'] = False
        cell['metadata']['message'] = False

print("✓ Added metadata to hide code cells")

with open('patent_analysis_chapter.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
EOF

echo ""
echo "Step 4: Render PDF with Quarto..."
quarto render patent_analysis_chapter.ipynb --to pdf

echo ""
echo "Step 5: Cleanup intermediate files..."
rm -f patent_analysis_chapter.ipynb
rm -f patent_analysis_chapter.md
rm -rf .quarto/
echo "✓ Removed intermediate files"

echo ""
echo "✅ PDF export complete!"
echo ""
ls -lh patent_analysis_chapter.pdf
pdfinfo patent_analysis_chapter.pdf 2>/dev/null | grep Pages || echo ""
echo ""
echo "📄 Output: patent_analysis_chapter.pdf"
echo ""
echo "Configuration used:"
echo "  - Figures: 140% larger, 2× resolution, 11-13pt fonts"
echo "  - Tables: Smaller font (\footnotesize), reduced padding (3pt)"
echo "  - Layout: A4 paper, 1.5 line spacing, code hidden"
