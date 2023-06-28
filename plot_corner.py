import corner
import numpy as np
import matplotlib.pyplot as plt

class PlotCorner:
    def __init__(self, data):
        self.parameters = data.parameters
        self.valid_parameters = []
        self.posteriors = []
        self.injection_values = []
        self.lower_quantiles = []
        self.upper_quantiles = []
        self.medians = []

        for parameter in self.parameters:
            if len(set(data.posteriors_dict[parameter])) < 10:
                print('Ignoring fixed parameter ' + parameter + '.')
            else:
                self.valid_parameters.append(parameter)
                self.posteriors.append(data.posteriors_dict[parameter])
                self.injection_values.append(data.injection_dict[parameter])
                self.lower_quantiles.append(np.quantile(data.posteriors_dict[parameter], 0.05))
                self.upper_quantiles.append(np.quantile(data.posteriors_dict[parameter], 0.95))
                self.medians.append(np.median(data.posteriors_dict[parameter]))

        self.posteriors = np.array(self.posteriors).T
        self.injection_values = np.array(self.injection_values)
        self.lower_quantiles = np.array(self.lower_quantiles)
        self.upper_quantiles = np.array(self.upper_quantiles)
        self.medians = np.array(self.medians)

    def plot(self, show=False, save=False, title=''):
        fig = corner.corner(data=self.posteriors, labels=self.valid_parameters, show_titles=True, color='blue', title_quantiles=[0.05, 0.5, 0.95], title_kwargs={'fontsize' : 11})

        corner.overplot_lines(fig=fig, xs=self.injection_values, color='orange')
        corner.overplot_points(fig=fig, xs=self.injection_values[None], color='orange')

        corner.overplot_lines(fig=fig, xs=self.medians, color='black')
        corner.overplot_points(fig=fig, xs=self.medians[None], color='black')

        corner.overplot_lines(fig=fig, xs=self.lower_quantiles, color='red')
        corner.overplot_lines(fig=fig, xs=self.upper_quantiles, color='red')

        fig.suptitle(title, x=0.98, y=0.98, horizontalalignment='right')

        if save:
            plt.savefig('plots/' + title + '_plot.png')
        if show:
            plt.show()
