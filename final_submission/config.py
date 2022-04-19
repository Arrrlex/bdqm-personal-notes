from torch import nn


config = {
    "model": {
        "num_layers": 11,
        "num_nodes": 23,
        "name": "singlenn",
        "get_forces": False,
        "dropout": 1,
        "dropout_rate": 0.0,
        "initialization": "xavier",
        "activation": nn.Tanh,
    },
    "optim": {
        "gpus": 1,
        "lr": 0.000866342,
        "scheduler": {
            "policy": "StepLR",
            "params": {
                "step_size": 20,
                "gamma": 0.999565,
            },
        },
        "batch_size": 256,
        "loss": "mae",
        "epochs": 1000,
    },
    "dataset": {
        "lmdb_path": ["data/oc20_50k_alex.lmdb"],
        "cache": "full",
    },
    "cmd": {
        "seed": 12,
        "identifier": "test",
        "dtype": "torch.DoubleTensor",
        "verbose": True,
    },
}