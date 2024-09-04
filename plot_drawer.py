import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class PlotDrawer:
    def __init__(self, plot_dir):
        self.plot_dir = plot_dir
        os.makedirs(self.plot_dir, exist_ok=True)

    def draw_plots(self, json_file):
        # Read the JSON file into a DataFrame
        df = pd.read_json(json_file)
        plot_paths = []
        # Distribution of Mean Deviations
        plt.figure(figsize=(10, 6))
        sns.histplot(df['mean'], bins=20, kde=True)
        plt.title('Distribution of Mean Deviations')
        plt.xlabel('Mean Deviation')
        plt.ylabel('Frequency')
        plot_path = os.path.join(self.plot_dir, 'mean_deviation_distribution.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(plot_path)
        # Box Plot of Deviations
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[['mean', 'max', 'min']])
        plt.title('Box Plot of Deviations')
        plt.xlabel('Deviation Type')
        plt.ylabel('Deviation')
        plot_path = os.path.join(self.plot_dir, 'deviation_boxplot.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(plot_path)
        # Box Plot of Floor Deviations
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[['floor_mean', 'floor_max', 'floor_min']])
        plt.title('Box Plot of Floor Deviations')
        plt.xlabel('Deviation Type')
        plt.ylabel('Deviation')
        plot_path = os.path.join(self.plot_dir, 'deviation_floor_boxplot.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(plot_path)
        # Box Plot of Ceiling Deviations
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[['ceiling_mean', 'ceiling_max', 'ceiling_min']])
        plt.title('Box Plot of Ceiling Deviations')
        plt.xlabel('Deviation Type')
        plt.ylabel('Deviation')
        plot_path = os.path.join(self.plot_dir, 'deviation_ceiling_boxplot.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(plot_path)
        # Scatter Plot
        plt.figure(figsize=(10, 6))
        plt.scatter(df['min'], df['max'], alpha=0.7)
        plt.title('Scatter Plot of Min vs Max')
        plt.xlabel('Min Value')
        plt.ylabel('Max Value')
        plt.xscale('log')  # Log scale for x-axis
        plt.grid(True)
        scatter_plot_path = os.path.join(self.plot_dir, 'scatter_plot.png')
        plt.savefig(scatter_plot_path)
        plt.close()
        plot_paths.append(scatter_plot_path)
        plt.figure(figsize=(10, 8))
        sns.pairplot(df[df.columns[3:]], diag_kind='kde')
        pairplot_path = os.path.join(self.plot_dir, 'pairplot.png')
        plt.savefig(pairplot_path)
        plt.close()
        plot_paths.append(pairplot_path)
        # Relational Plot of Mean Deviation
        plt.figure(figsize=(10, 6))
        sns.relplot(data=df, x="gt_corners", y="rb_corners")
        relplot_path = os.path.join(self.plot_dir, 'mean_deviation_relplot.png')
        plt.savefig(relplot_path)
        plt.close()
        plot_paths.append(relplot_path)
        # Distribution Plot of gt_corners
        plt.figure(figsize=(10, 6))
        plt.title('Distribution Plot of gt_corners')
        sns.histplot(data=df, x="gt_corners")
        gt_corners_histplot_path = os.path.join(self.plot_dir, 'gt_corners_histplot.png')
        plt.savefig(gt_corners_histplot_path)
        plt.close()
        plot_paths.append(gt_corners_histplot_path)
        return plot_paths