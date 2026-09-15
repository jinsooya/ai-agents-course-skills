---
name: writing-analysis-report
description: After a multi-step data analysis, write the results into a Markdown report saved as /report.md. Use when the user asks for an analysis report, a results summary, key insights, or a final write-up, or when the analysis procedure reaches its last step.
---

# Writing the Analysis Report

Do this once, in the report-writing step after all analysis steps are complete.

**Step 1: Collect the evidence** - Gather the key figures, tables, and saved chart PNG file names that each step printed with `print()`. Leave out any number that was not printed.

**Step 2: Check the template** - Read `references/report-template.md` and follow its structure. Do not write the report before reading that file.

**Step 3: Save** - Save the report to `/report.md` with the `write_file` tool. The root (`/`) of the file tools is the result folder. Do not save to a path such as `/report.md` from inside `python_execute` code.

**Step 4: Final answer** - Reply to the user with only the report path and a short summary of the key insights. The details are in the report.

## Writing rules

- Round amounts to two decimals and use thousands separators. Write shares as percentages with one decimal.
- Use Markdown tables and keep the sort order of the original output.
- Keep interpretations, personas, and strategy proposals consistent with the aggregates above, and tie every quantitative claim to those aggregates.
- Write 'not available in the data' for information the data does not contain; never fill it with invented numbers.
