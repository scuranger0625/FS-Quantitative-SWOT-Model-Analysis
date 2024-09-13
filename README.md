# FS-Quantitative-SWOT-Model-Analysis
財務報表量化SWOT分析第一版

Usage
Run the Program: Simply execute the swot_analysis.py file.

Input Weights:

Enter the weight values for each SWOT category. The sum of weights should be 1. If the sum is not equal to 1, the program will display a warning.
View Results:

The program will calculate the total score for each SWOT category based on the input weights.
Results will be displayed as a bar chart, with each bar showing the corresponding score and weight.
Code Structure
set_swot_weights_from_input(): Prompts the user to input weights for each SWOT category and returns a dictionary of weights.
calculate_strengths(): Calculates the total score for Strengths.
calculate_weaknesses(): Calculates the total score for Weaknesses.
calculate_opportunities(): Calculates the total score for Opportunities.
calculate_threats(): Calculates the total score for Threats.
SWOTAnalysis class: Encapsulates the logic for calculating and displaying the analysis results.
