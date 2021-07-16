
##Falnker task
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("flanker_data/P1Flanker1.csv")
    mean = df["Correct"].mean()    
    correct_df = df[df.Correct == 1]
    correct_Mean = correct_df["ReactionTime"].mean()
    incorrect_df = df[df.Correct == 0]
    incorrect_Mean = incorrect_df["ReactionTime"].mean()
    print(f"mean accuracy across the task: \t\t\t\t\t\t {mean}")
    print(f"mean reaction time across the task - for correct responses only:\t {correct_Mean}")
    print(f"mean reaction time across the task - for incorrect responses only:\t {incorrect_Mean}")
    congruent = correct_df[correct_df.Condition == 0]["ReactionTime"].mean()
    neutral = correct_df[correct_df.Condition == 1]["ReactionTime"].mean()
    incongruent = correct_df[correct_df.Condition == 2]["ReactionTime"].mean()
    bplot = pd.DataFrame({'mean reaction time':['congruent', 'neutral', 'incongruent'], 'val':[congruent, neutral, incongruent]})
    bplot.plot.bar(x='mean reaction time', y='val', rot=0)
    plt.show()
    
if __name__ == "__main__":
    main()