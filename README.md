# Keras Preprocessing

### 1) Setup
#### a) Clone the repo
Create a directory called KerasPreprocessing, ```cd``` into it, and then run ```$> git clone https://github.com/lootag/KerasPreprocessing.git .```.
#### b) Set up virtual environment  
In order to setup the application your going to need ```virtualenv``` installed on your machine.
Once you have it, run ```$> virtualenv env``` to create a python virtual environment. Then run ```$> source env/bin/activate``` to activate it.
Once you've activated the environment, install all dependencies by running ```pip3 install -r requirements.txt```.
### 2) Run 
#### a) Set up the directory tree
Always staying in the repo's directory, create a directory called Images, and another called Annotations. 
Copy your images (they need to be of the same size, https://github.com/lootag/ImageAuGomentationCLI is going to take care of preprocessing them for you) into the Images folder, and your annotations into the Annotations folder.
#### b) Run the utility
Just run ```$> python3 Program.py```. This is going to run the application with the default values ```--batch_size=10``` and ```--annotation_type=PASCAL_VOC```.
