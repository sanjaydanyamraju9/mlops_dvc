Create ENV
```bash
conda create -n mlops_dvc python -y
```
Activate ENV
```bash
conda activate mlops_dvc
```
Create reqs.txt
```bash
touch requirements.txt
```
Install packages
```bash
pip install -r requirements.txt
```
Install and configure awscli
```bash
pip install awscli
aws configure
```
Create template.py
```bash
touch template.py
```
```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/*.csv 
```