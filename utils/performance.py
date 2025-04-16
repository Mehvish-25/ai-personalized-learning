import matplotlib.pyplot as plt

def plot_performance(assess: int, test: int, subject: str):
    """Return a Matplotlib figure comparing initial quiz vs final test."""
    fig, ax = plt.subplots()
    ax.bar(["Initial Quiz", "Final Test"], [assess, test])
    ax.set_ylabel("Score")
    ax.set_ylim(0, max(assess, test, 4))  # assuming out of 4
    ax.set_title(f"{subject} Performance")
    return fig
