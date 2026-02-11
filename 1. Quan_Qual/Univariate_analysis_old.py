class Univariate():
    def __init__(self,dataset):
        self.dataset = dataset

    # Method to separate the Quantitative and Qualitative Data
    def quanQual(self):  
        quan=[]
        qual=[]
        for columnName in self.dataset.columns:
            if (self.dataset[columnName].dtypes == "O"):   # "O" - Object Data type
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
