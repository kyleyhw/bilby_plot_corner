from data_loaders import DataLoaderJSON, DataLoaderH5
from plot_corner import PlotCorner

parameters = ['chi_eff', 'lambda_tilde', 'mass_ratio']


# filename = 'bns_example_result'
# filename = 'bns_fixed_m_example_result'
# data = DataLoaderJSON(filename='data/' + filename + '.json', parameters=parameters)

# filename = 'bns_example_data0_1126259642-413_analysis_H1L1V1_result'
# filename = 'bns_free_spin_example_data0_1126259642-413_analysis_H1L1V1_result'
# filename = 'bns_zero_spin_example_data0_1126259642-413_analysis_H1L1V1_result'
# filename = 'bns_zero_spin_L1L2_example_data0_1126259642-413_analysis_H1L1V1_result'
filename = 'bns_binary_love_example_data0_1126259642-413_analysis_H1L1V1_result'
data = DataLoaderH5(filename='data/' + filename + '.hdf5', parameters=parameters)

plotter = PlotCorner(data)
plot_title = '_'.join(filename.split('_')[:4])
print(plot_title)
plotter.plot(show=False, save=True, title=plot_title)