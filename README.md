# model-validation
The model `eos30gr` that is [deepherg](https://github.com/ersilia-os/eos30gr/blob/main/README.md) has been chosen for model validation.

## Repository organisation
The repository is organised in folders:
- `/notebooks` contains the jupyter notebooks where most of the work is being developed
- `/data` contains all the .csv files. Model predictions are obtained outside this repository and saved in this folder.
- `/src` contains important functions I will re-use throughout the repository, to avoid typing them each time.
- `/plots` contains the plots I have produced during the model validation process
- `requirements.txt` lists all the required packages to run the notebooks in this repository. If possible I also specify the version of the package I am using.

## How to use this repository
- First refer to the [Ersilia](https://ersilia.gitbook.io/ersilia-book) documentation to set up a virtual environment and set up the Ersilia model hub.
- Enter the virtual environment and run the following command:
```
pip install -r requirements.txt
```
- Install `ipykernel` for this environment and set up the kernel for the Jupyter notebook for this virtual environment.
```
conda install ipykernel
python -m ipykernel install --user --name ersilia --display-name "ersilia"
```
- Run the `.ipynb` notebooks in `\notebooks` directory.

## Conclusion from the week 2 tasks
##### Task 1
- We notice that our model is biased towards non-hERG blockers, indicating that most of the compounds are not hERG blockers. This can be dependent on the number of hERG blockers present in reality and hence, our random dataset can be assumed to be a reflection of it.
- We can conclude that there are two possible reasons why we have the above result. There is a possibility that our dataset ended up with majorly non-hERG blockers purely by chance. Other possibility is that most of the compounds in nature do not have the property of being a non-hERG blocker, hence explaining our result.

##### Task 2
- According to our dataset, every single molecule should be a hERG blocker.
- However, we are not able to reproduce our dataset. There is a possibility that the model has not been trained correctly, explaining the result.

## Where to get more help:
- Read Outreachy's contribution [tasks](https://ersilia.gitbook.io/ersilia-book/contributors/internships/outreachy-summer-2024)
- Read Ersilia's [documentation](https://ersilia.gitbook.io/ersilia-book)
- Get inspiration from Ersilia's work, for example on this repository for [data processing](https://github.com/ersilia-os/open-data-cleaning)
- Use Slack to ask the mentors and the other interns for help!

## License
All the code in this repository is licensed under a GPLv3 License.