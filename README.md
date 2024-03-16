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

## Where to get more help:
- Read Outreachy's contribution [tasks](https://ersilia.gitbook.io/ersilia-book/contributors/internships/outreachy-summer-2024)
- Read Ersilia's [documentation](https://ersilia.gitbook.io/ersilia-book)
- Get inspiration from Ersilia's work, for example on this repository for [data processing](https://github.com/ersilia-os/open-data-cleaning)
- Use Slack to ask the mentors and the other interns for help!

## License
All the code in this repository is licensed under a GPLv3 License.