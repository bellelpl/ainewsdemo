# Basic Statistics Report for News Articles

## Dataset Overview
- **Data Source**: `/workspaces/ainewsdemo/data/trump_xi_meeting_fulltext_dedup-1657.csv`
- **Total Number of Articles**: 1,657
- **Date of Analysis**: November 4, 2025

## Word Count Statistics
### Basic Metrics
- **Average Word Count**: 520.08 words
- **Median Word Count**: 437.00 words
- **Minimum Word Count**: 18 words
- **Maximum Word Count**: 6,973 words

### Distribution Analysis
The word count distribution reveals:
- Most articles are of moderate length (300-700 words)
- There is a right-skewed distribution, meaning there are some very long articles pulling the average above the median
- The significant difference between mean (520) and median (437) confirms this skewness

### Visualization Files
Two visualization files have been generated to help understand the distribution:
1. `word_count_distribution.png`: Histogram showing the frequency distribution of article lengths
2. `word_count_boxplot.png`: Box plot showing the statistical spread and potential outliers

## Output Files Generated
1. `articles_with_wordcount.csv`: Enhanced dataset including word counts
2. `word_count_distribution.png`: Distribution visualization
3. `word_count_boxplot.png`: Statistical spread visualization
4. `statistics_report.md`: Basic numerical statistics

## Methodology
- Word counting was performed using Python's string split function
- Empty or null text fields were counted as 0 words
- All words were counted regardless of length or type
- Visualizations were created using matplotlib and seaborn libraries

## Technical Implementation
The analysis was performed using:
- Python with pandas for data processing
- matplotlib and seaborn for visualizations
- Standard Python string operations for word counting

The complete code can be found in `basic_stats.py` in the output directory.