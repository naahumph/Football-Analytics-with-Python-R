## Chapter 2
## Stable vs Unstable Quarterback Stats

## package installation
install.packages("nflfastR")
install.packages("tidyverse")
install.packages("ggthemes")

## load the libraries to be used
library("tidyverse")
library("nflfastR")
library("ggthemes")

pbp_r <- load_pbp(2016:2022)