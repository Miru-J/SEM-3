import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Import the keyboard layout data
from qwerty_layout import keys
# from colemak_layout import keys

def plot_keyboard():
    fig, ax = plt.subplots(figsize=(15, 6))
    
    for key, data in keys.items():
        x, y = data['pos']
        rect = Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=False)
        ax.add_patch(rect)
        ax.text(x, y, key, ha='center', va='center', fontsize=12)

    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    plt.title('QWERTY Keyboard Layout')
    plt.tight_layout()
    plt.show()

plot_keyboard()

