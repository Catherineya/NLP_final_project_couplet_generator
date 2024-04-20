#split the dataset
import numpy as np
from sklearn.model_selection import train_test_split

def load_data(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        inputs = file.readlines()
    
    with open(output_filename, 'r') as file:
        outputs = file.readlines()
        
    inputs = [line.strip() for line in inputs]
    outputs = [line.strip() for line in outputs]
    
    return inputs, outputs

def split_data(inputs, outputs):
    X_train, X_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def save_datasets(X_train, X_test, y_train, y_test):
    np.savetxt('data/train_in.txt', X_train, fmt='%s')
    np.savetxt('data/train_out.txt', y_train, fmt='%s')
    np.savetxt('data/test_in.txt', X_test, fmt='%s')
    np.savetxt('data/test_out.txt', y_test, fmt='%s')

def main():
    inputs, outputs = load_data('data/in.txt', 'data/out.txt')
    X_train, X_test, y_train, y_test = split_data(inputs, outputs)
    save_datasets(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()