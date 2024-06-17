import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

path_dict ={
    'Goal' : '/data/jeonghwan/coursework/data_driven_decision_making/DLPA-main/DLPA-main/result/DLPA/Goal/070901/Test_epioside_step_0.csv',
    'Platform' : '/data/jeonghwan/coursework/data_driven_decision_making/DLPA-main/DLPA-main/result/DLPA/Platform/070901/Test_epioside_step_0.csv',
    'Simple Catch' : '/data/jeonghwan/coursework/data_driven_decision_making/DLPA-main/DLPA-main/result/DLPA/simple_catch/070901/Test_epioside_step_0.csv',
    'Hard Move(4)' : '/data/jeonghwan/coursework/data_driven_decision_making/DLPA-main/DLPA-main/result/DLPA/simple_move_4_direction_v1/4/Test_epioside_step_0.csv',
    'Hard Move(6)' : '/data/jeonghwan/coursework/data_driven_decision_making/DLPA-main/DLPA-main/result/DLPA/simple_move_4_direction_v1/6/Test_epioside_step_0.csv',
    'Hard Move(8)' : '/data/jeonghwan/coursework/data_driven_decision_making/DLPA-main/DLPA-main/result/DLPA/simple_move_4_direction_v1/8/Test_epioside_step_0.csv',
    'Hard Move(10)' : '/data/jeonghwan/coursework/data_driven_decision_making/DLPA-main/DLPA-main/result/DLPA/simple_move_4_direction_v1/10/Test_epioside_step_0.csv',
}

# Set plot layout (2x4 grid)
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(20, 10))
axes = axes.flatten()

# Set moving average window size
window_size = 10

# Generate plots
for idx, (experiment, path) in enumerate(path_dict.items()):
    print('='*30)
    print(experiment)
    data = pd.read_csv(path)
    
    num_rows = data.shape[0]
    row_means = data.mean(axis=1)
    
    # Select the last 10 steps
    last_10_means = row_means[-10:]
    overall_mean = last_10_means.mean()
    overall_std_dev = last_10_means.std()

    print(f'Time Steps: {num_rows*50}')
    print(f"Mean of last 10 steps: {round(overall_mean,2)}")
    print(f"Std of last 10 steps: {round(overall_std_dev,2)}")

    # Calculate moving average
    smooth_row_means = row_means.rolling(window=window_size).mean()
    smooth_std = row_means.rolling(window=window_size).std()

    x = np.arange(num_rows) * 50  # Set x values with 50 increment
    y = smooth_row_means

    axes[idx].plot(x, y, label='Smoothed Mean values')
    axes[idx].fill_between(x, y - smooth_std, y + smooth_std, alpha=0.2)
    axes[idx].set_title(experiment)
    axes[idx].set_xlabel('Time Steps')
    axes[idx].set_ylabel('Rewards')
    axes[idx].legend()

    print('='*30)
    print('')

# Remove empty plots
for i in range(len(path_dict), len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
save_path = '/data/jeonghwan/coursework/data_driven_decision_making/DLPA-main/DLPA-main/result/DLPA/combined_plot_episode.png'
plt.savefig(save_path)
plt.show()
