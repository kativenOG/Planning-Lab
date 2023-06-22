from envs.obsgrid_env import ObsGrid


class LavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "L", "L", "P"],
                ["L", "P", "L", "P"],
                ["L", "L", "L", "G"]
            ]
        rewards = {"L": 1, "S": 1, "P": -10, "G": 50}
        actdyn = {0: {0: 1, 1: 0.0, 2: 0.0, 3: 0.0}, 1: {1: 1, 0: 0.0, 2: 0.0, 3: 0.0}, 2: {2: 1, 1: 0.0, 0: 0.0,
                  3: 0.0}, 3: {3: 1, 1: 0.0, 2: 0.0, 0: 0.0}}
        super().__init__(actions, grid, actdyn, rewards)

#used this
class VeryBadLavaFloorEnv(ObsGrid):
    """
    The floor is lava... but very bad and dangerous lava! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "L", "L", "G"],
                ["L", "W", "L", "P"],
                ["L", "L", "L", "L"]
            ]
        rewards = {"L": -0.01, "S": -0.01, "P": -1.0, "G": 1.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)

#used this
class NiceLavaFloorEnv(ObsGrid):
    """
    The floor is lava but the agent really likes it! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "L", "L", "G"],
                ["L", "W", "L", "P"],
                ["L", "L", "L", "L"]
            ]
        rewards = {"L": 0.5, "S": 0.5, "P": -1.0, "G": 1.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class BiggerLavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome. Bigger grid.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
            ["S", "L", "L", "L", "L", "L"],
            ["L", "L", "W", "L", "L", "P"],
            ["L", "P", "W", "L", "L", "W"],
            ["L", "L", "L", "L", "L", "L"],
            ["P", "L", "L", "L", "L", "G"]
        ]
        rewards = {"L": -0.04, "S": -0.04, "P": -10.0, "G": 10.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class HugeLavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome. Bigger grid.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
            ["S", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L", "P", "L", "L", "L", "L"],
            ["L", "L", "L", "W", "L", "L", "W", "L", "L", "L"],
            ["L", "L", "P", "W", "L", "L", "W", "L", "P", "L"],
            ["L", "L", "L", "W", "L", "L", "W", "L", "L", "L"],
            ["L", "L", "L", "W", "W", "W", "W", "L", "L", "L"],
            ["L", "L", "P", "L", "L", "L", "L", "L", "L", "P"],
            ["L", "L", "L", "L", "L", "P", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
            ["P", "L", "L", "L", "L", "L", "L", "L", "L", "G"]
        ]
        rewards = {"L": -0.04, "S": -0.04, "P": -10.0, "G": 10.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


