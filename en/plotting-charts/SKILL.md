---
name: plotting-charts
description: Draw charts with matplotlib pyplot and seaborn inside the python_execute tool so that they are saved automatically as PNG files in the result folder. Use when the user asks for a visualization, chart, graph, histogram, scatter plot, bar chart, pie chart, or subplot grid.
---

# Plotting Charts

The `python_execute` tool saves the current figure to the result folder as a PNG and shows it in the notebook whenever `pyplot.show()` is called. The rules below keep that automatic save from being skipped.

## Rules

1. Draw with `pyplot` imported as `from matplotlib import pyplot`. Use `pyplot.subplots()`, `pyplot.plot()`, and so on; do not use the alias `plt`.
2. Use seaborn on a figure and axes created by `pyplot`, passing the axes through the `ax=` argument.
3. Call `pyplot.show()` at the end of every chart.
4. Do not build a standalone `matplotlib.figure.Figure`; the automatic save and the notebook display would be skipped.
5. You do not need to call `savefig()`; the tool saves the file. If you must save a file yourself, use only a `RESULT_FOLDER / '<name>.png'` path.
6. Do not call `pyplot.close('all')`; it skips the automatic save.
7. Write chart titles, axis labels, legends, and annotations in English so they render in environments without Korean fonts. Write the interpretation of the results in the language of the request.
8. When drawing several charts at once, use subplots and call `pyplot.tight_layout()`. A 2×2 grid works well with `figsize=(14, 10)`.
9. Sort bar charts from the largest value down, and show the color-coded variable of a scatter plot with a colorbar or a legend.

## Output

After drawing, describe what the chart shows in one or two sentences, and cite only figures that were computed in code and printed with `print()`.
