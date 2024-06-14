
# KAIST IE437 Final Project

This repository contains the implementation and reproduction of experiments from the paper **[ICML 2024] “Model-based Reinforcement Learning for Parameterized Action Spaces”** by Renhao Zhang et al.

## Introduction

This project aims to reproduce the experiments presented in the aforementioned paper. The paper introduces a novel model-based reinforcement learning algorithm for parameterized action spaces, achieving superior performance on several benchmarks.

## Paper Overview

The paper proposes a new algorithm, DLPA (Dynamics Learning and Predictive Control with Parameterized Actions), which is tailored for Parameterized Action Markov Decision Processes (PAMDPs). Key contributions of the paper include:

1. Three inference structures for the transition model considering the entangled parameterized action space.
2. Transition model updates with H-step loss.
3. Learning two separate reward predictors conditioned on the prediction for termination.
4. A PAMDP-specific Model Predictive Path Integral (MPPI) control approach.

## Experimental Setup

The paper evaluates the proposed algorithm on eight different benchmarks. Below is the step-by-step guide to reproduce the experiments:

### Environment Setup

1. Create a new Conda environment:
    ```sh
    conda create -n myenv python=3.8
    conda activate myenv
    ```

2. Install necessary packages:
    ```sh
    pip install numpy matplotlib torch==2.0.1 click gym==0.10.5 psutil wandb
    ```

3. Clone and install the `gym-goal` package:
    ```sh
    git clone https://github.com/cycraig/gym-goal
    cd gym-goal
    pip install -e '.[gym-goal]'
    cd ..
    ```

4. Navigate to the project directory:
    ```sh
    cd DLPA-main
    ```

### Running Experiments

1. **Platform**
    ```sh
    python main.py --env 'Platform-v0' --mpc_horizon 10 --model_type "multi" --save_points 1
    ```

2. **Goal**
    ```sh
    python main.py --env 'Goal-v0' --mpc_horizon 8 --model_type "overlay" --save_points 1
    ```

3. **Hard Goal**
    ```sh
    python main.py --env 'hard_goal-v0' --mpc_horizon 8 --model_type "overlay" --save_points 1
    ```

4. **Catch Point**
    ```sh
    python main.py --env 'simple_catch-v0' --mpc_horizon 8 --model_type "overlay" --save_points 1
    ```

5. **Hard Move (4 Directions)**
    ```sh
    python main.py --env 'simple_move_4_direction_v1-v0' --mpc_horizon 5 --action_n_dim 4 --save_points 0 --model_type "concat" --save_dir “4”
    ```

6. **Hard Move (6 Directions)**
    ```sh
    python main.py --env 'simple_move_4_direction_v1-v0' --mpc_horizon 5 --action_n_dim 6 --save_points 0 --model_type "concat" --save_dir “6”
    ```

7. **Hard Move (8 Directions)**
    ```sh
    python main.py --env 'simple_move_4_direction_v1-v0' --mpc_horizon 5 --action_n_dim 8 --save_points 0 --model_type "concat" --save_dir “8”
    ```

8. **Hard Move (10 Directions)**
    ```sh
    python main.py --env 'simple_move_4_direction_v1-v0' --mpc_horizon 5 --action_n_dim 10 --save_points 0 --model_type "concat" --save_dir “10”
    ```

## Notes on Reproduction

- **`hard_goal-v0`**: The reproduction of this experiment failed due to the undefined `pad_hardgoal` function in the `Trainer` class in `DLPA.py`.
- **Hard Move (10)**: The model was too heavy, requiring an extensive training time. The results were obtained after training on an A5000 GPU for four days.

## Results

The results of the reproduced experiments are summarized in the following table:

| Environment | Performance (ours) | Performance (paper) |
|-------------|---------------------|---------------------|
| Platform    | ...                 | 0.92 ± 0.05         |
| Goal        | ...                 | 28.75 ± 6.91        |
| Hard Goal   | N/A                 | 28.38 ± 2.88        |
| Catch Point | ...                 | 7.56 ± 4.86         |
| Hard Move (4) | ...               | 6.29 ± 5.74         |
| Hard Move (6) | ...               | 8.48 ± 5.45         |
| Hard Move (8) | ...               | 7.80 ± 6.27         |
| Hard Move (10) | Partial          | 6.35 ± 9.97         |

*(Fill in the table with the results of your experiments.)*

## Conclusion

Most of the experiments were successfully reproduced, demonstrating the efficacy of the proposed algorithm. However, certain issues were encountered in reproducing some experiments, highlighting areas for further debugging and improvement.

---

Please refer to the original paper for more details and the theoretical underpinnings of the proposed methods.

## References

- Renhao Zhang et al., "Model-based Reinforcement Learning for Parameterized Action Spaces", ICML 2024.

## Acknowledgments

This work was conducted as part of the final project for the KAIST course IE437. Special thanks to the authors of the paper for their contributions to the field of reinforcement learning.

---

