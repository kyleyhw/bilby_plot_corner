from data_loader_json import DataLoaderJSON
from plot_corner import PlotCorner

filename = 'bns_example_result'
# filename = 'bns_fixed_m_example_result'

parameters = ['chirp_mass', 'mass_ratio', 'lambda_tilde', 'chi_eff']

data = DataLoaderJSON(filename=filename + '.json', parameters=parameters)
plotter = PlotCorner(data)

plotter.plot(show=False, save=True, title=filename)