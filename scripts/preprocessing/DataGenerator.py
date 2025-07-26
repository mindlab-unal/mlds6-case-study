import numpy as np
import keras

class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self, metadata, batch_size=32, dim=(32,32,3), shuffle=True):
        'Initialization'
        self.metadata = metadata
        self.batch_size = batch_size
        self.dim = dim
        self.shuffle = shuffle
        self.on_epoch_end()

    def __len__(self):
        'Denotes the number of batches per epoch'
        return int(np.floor(len(self.metadata) / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        batch_metadata = self.metadata.iloc[index*self.batch_size:(index+1)*self.batch_size]

        # Generate data
        X, y = self.__data_generation(batch_metadata)

        return X, y

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        if self.shuffle == True:
            self.metadata = self.metadata.sample(frac=1).reset_index(drop=True)

    def __data_generation(self, batch_metadata):
        'Generates data containing batch_size samples' 
        # Initialization
        X = np.zeros([self.batch_size, self.dim [0], self.dim [1], self.dim [2]])
        Y = np.zeros([self.batch_size,1])

        # Generate data
        for i in range(len(batch_metadata)):
            row = batch_metadata.iloc[i]
            path = row['path']
            label = row['label']

            image = keras.utils.load_img(path, target_size=(self.dim [0], self.dim [1]), color_mode='rgb')
            image = np.array(image)
            
            X[i] = image/255 
            Y[i] = label

            
        return X, Y