import json
import h5py

class DataLoaderJSON:
    def __init__(self, filename, parameters):
        self.parameters = parameters

        with open(filename) as file:
            data = json.load(file)

        posteriors = data['posterior']['content']
        injection_parameters = data['injection_parameters']

        self.posteriors_dict = {}
        self.injection_dict = {}

        for parameter in self.parameters:
            self.posteriors_dict[parameter] = posteriors[parameter]
            self.injection_dict[parameter] = injection_parameters[parameter]

class DataLoaderH5:
    def __init__(self, filename, parameters):
        self.parameters = parameters

        file = h5py.File(filename, 'r')

        posteriors = file['posterior']
        injection_parameters = file['injection_parameters']

        self.posteriors_dict = {}
        self.injection_dict = {}

        for parameter in parameters:
            self.posteriors_dict[parameter] = posteriors[parameter][:]
            self.injection_dict[parameter] = injection_parameters[parameter][()]
            if parameter == 'chi_eff':
                print(set(self.posteriors_dict[parameter]))