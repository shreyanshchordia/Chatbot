import ntpath
from keras.models import model_from_json

def load(filename, weights):

    json_file = open(filename, 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    # load weights into new model
    model.load_weights(weights)

    return model

def load_model(name, model_path, weights_path):
    # load json and create model
    filename = model_path
    weights = weights_path

    model = load(filename, weights)

    print(f"Loaded {name} Model from Disk!")

    return model