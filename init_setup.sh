echo [$(date)]: "START"

echo [$(date)]: "creating env with python 3.9 version"

conda create --prefix ./env python=3.9 -y

echo [$(date)]: "activating the environment"

source activate ./env
echo [$(date)]: "installing the env requirements"
 pip install -r requirements.txt
 echo [$(date)]: "end"