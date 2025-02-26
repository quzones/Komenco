STEPS TO INSTALL AND RUN THE SAMPLE PROBLEMS IN THE SDK

(1) Install Python
Install the latest version of python. https://www.anaconda.com/download 
put D:\ProgramData\anaconda3\Scripts on the System Path (Environment Variables)

Open a command prompt and type
>   conda init
[This will initialize conda]
Close the command prompt and open a new command prompt and proceed
 
(2) Create a Conda Environment

>	mkdir c:\automatski
[unzip the .zip file contents we sent earlier into c:\automatski
>	conda create –n automatski python==3.11
>	conda activate automatski
>	pip install requests matplotlib numpy jupyter networkx pandas scikit-learn
The environment is ready you can close the command prompt now.

(3) To Run The "Native" Client SDK Samples
Open a Command Prompt and type
>	conda activate automatski 
>	cd /d c:\automatski
>   cd native 
>	python <program-name>

Where program name is like

helloworld-komenco-native.py
...

(4) If you want to run the examples in other folders e.g. pytorch-quantum or qiskit then go into that folder and install the requirements for those framework and examples. 

>   cd qiskit
>   pip install -r requirements.txt
>   python <program-name>

Or if the folder doesn't have a requirements.txt file but has a readme.txt file then follow the instructions in the readme.txt file.

(5) if you want to start the Jupyter Notebook
Open a Command Prompt and type
>	conda activate automatski 
>	cd /d c:\automatski
>   jupyter notebook