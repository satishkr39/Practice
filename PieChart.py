from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from scipy.constants import inch
from Week4Final import report

report_pie = Pie(width=3*inch, height=3*inch)
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
print(report_pie.data)

report_chart = Drawing()
report_chart.add(report_pie)
