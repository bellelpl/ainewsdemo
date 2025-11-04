import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def count_words(text):
    if pd.isna(text):
        return 0
    return len(str(text).split())

def process_articles(input_csv):
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Get the number of articles
    num_articles = len(df)
    
    # Add word count column
    df['word_count'] = df['body'].apply(count_words)
    
    # Save the enhanced CSV
    output_path = Path('/workspaces/ainewsdemo/practice/output')
    output_csv = output_path / 'articles_with_wordcount.csv'
    df.to_csv(output_csv, index=False)
    
    # Generate visualizations
    
    # 1. Word count distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='word_count', bins=30)
    plt.title('Distribution of Article Word Counts')
    plt.xlabel('Word Count')
    plt.ylabel('Number of Articles')
    plt.savefig(output_path / 'word_count_distribution.png')
    plt.close()
    
    # 2. Box plot of word counts
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df['word_count'])
    plt.title('Box Plot of Article Word Counts')
    plt.ylabel('Word Count')
    plt.savefig(output_path / 'word_count_boxplot.png')
    plt.close()
    
    # Generate statistics report
    stats = {
        'Total number of articles': num_articles,
        'Average word count': df['word_count'].mean(),
        'Median word count': df['word_count'].median(),
        'Min word count': df['word_count'].min(),
        'Max word count': df['word_count'].max()
    }
    
    # Save statistics to markdown file
    with open(output_path / 'statistics_report.md', 'w') as f:
        f.write('# Article Statistics Report\n\n')
        for key, value in stats.items():
            f.write(f'## {key}\n')
            f.write(f'{value:.2f}\n\n')

def main():
    input_csv = '/workspaces/ainewsdemo/data/trump_xi_meeting_fulltext_dedup-1657.csv'
    process_articles(input_csv)
    print("Processing complete. Check the output folder for results.")

if __name__ == '__main__':
    main()