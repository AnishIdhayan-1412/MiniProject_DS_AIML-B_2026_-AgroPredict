def summarize(data):
    print(data.describe())
    print("\nShape:", data.shape)
    print("\nNull values:\n", data.isnull().sum())
