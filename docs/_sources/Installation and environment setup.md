# Installation and environment setup

As part of this protocol, all analysis steps are carried out using Python, an interpreted, high-level general-purpose programming language that can be used on a wide variety of operating systems, including LINUX, Windows, and macOS. Currently, the protocol is written in Python (`v3.10.4`) on a Linus-based Linux system (Red Hat Enterprise Linux version 7.9 (Maipo)). In addition to Python, R packages and tools are required for several analyses such as WGCNA, though those analyses are not part of this protocol. The protocol can be run on most UNIX and Linux distributions, however, Ubuntu 22 and Fedora 36, Red Hat 7, and macOS Monterey are recommended. Besides HPC devices, this protocol has been tested on other devices, with the following specifications:

::::{grid}

:::{grid-item-card} OS!
Windows 11 (5.10.102.1-microsoft-standard-WSL2), and Fedora 36.
:::

::::


::::{grid}
:gutter: 4

:::{grid-item-card} RAM!
16 GB 
:::

:::{grid-item-card} SDD!
256 GB 
:::

:::{grid-item-card} CPU!
Intel i7
:::

:::{grid-item-card} Conda!
v4.12.0
:::
::::





## Create conda environment

````{tab-set}
```{tab-item} Fedora (37<) and Ubuntu (22<) and WSL2
[centralitycosdist.yml](https://github.com/nilesh-iiita/CentralityCosDist/blob/main/centralitycosdist.yml)

    conda env create -n centralitycosdist --file centralitycosdist.yml
```

```{tab-item} Mac OS
[centralitycosdist.yml](https://github.com/nilesh-iiita/CentralityCosDist/blob/main/centralitycosdist.yml)

    conda env create -n centralitycosdist --file centralitycosdist.yml
```

```{tab-item} Windows 11/10
[centralitycosdist.yml](https://github.com/nilesh-iiita/CentralityCosDist/blob/main/centralitycosdist.yml)

    conda env create -n centralitycosdist --file centralitycosdist.yml
```
````


## Clone git repository

Fork the [CentralityCosDist](https://github.com/nilesh-iiita/CentralityCosDist) git repository and clone or download.

    git clone https://github.com/<User Name>/CentralityCosDist.git


## Citations

```{bibliography}
```

