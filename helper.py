import matplotlib.pyplot as plt

def plot(scores, mean_scores):
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores, label='Score')
    plt.plot(mean_scores, label='Mean Score')
    plt.legend()
    plt.ylim(ymin=0)
    plt.pause(0.001)  # Pause briefly to update the plot
