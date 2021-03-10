##### Requirements:

- Python version == 3.6
- numpy == 1.19.2
- torch == 1.7.1
- torchvision == 0.8.0

##### Run the examples:

1. Download the dataset from https://cloud.tsinghua.edu.cn/d/00e0704738e04d32978b/ and organized the data as follows:
   ```css
   hw2
   ├── README.md
   └── data
       ├── cifar_10_4x
           ├── train
           └── valid
   	├── cifar10_4x.py
   	├── evaluation.py
   	├── model.py
       └── train.py
   ```
   
2. Run the example:

   ``` bash
   python train.py
   ```

3. Evaluate your model:

   ```bash
   python evaluation.py
   ```

##### Task

1. Run the example.
2. Modify train.py and model.py to train your model. **<u>*Do not*</u>** modify evaluation.py and make sure your can finally test your model using evaluation.py, since we don't provide you the test yet, evaluation.py will test your model on the validation set.
3. Submit your model named "cifar10_4x_best.pth" and your model.py. Test and make sure you can run the evaluation.py successfully, otherwise your will lose the score of coding.
4. Submit your report. 