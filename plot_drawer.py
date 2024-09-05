import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import time

file_handler = logging.FileHandler('extended.log', 'a')
logging.basicConfig(handlers = [file_handler],
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

class PlotDrawer:
    def __init__(self, plot_dir):
        self.plot_dir = plot_dir
        os.makedirs(self.plot_dir, exist_ok=True)
        logging.info(f"Создана директория для графиков: {self.plot_dir}")

    def draw_plots(self, json_file):
        start_time = time.time()  # Запуск таймера
        logging.info(f"Начало обработки файла: {json_file}")

        # Read the JSON file into a DataFrame
        df = pd.read_json(json_file)
        plot_paths = []

        # Distribution of Mean Deviations
        start_plot_time = time.time()
        plt.figure(figsize=(10, 6))
        sns.histplot(df['mean'], bins=20, kde=True)
        plt.title('Distribution of Mean Deviations')
        plt.xlabel('Mean Deviation')
        plt.ylabel('Frequency')
        plot_path = os.path.join(self.plot_dir, 'mean_deviation_distribution.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(plot_path)
        logging.info(f"Гистограмма 'Mean Deviations' сохранена: {plot_path}, время выполнения: {time.time() - start_plot_time:.2f} секунд")

        # Box Plot of Deviations
        start_plot_time = time.time()
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[['mean', 'max', 'min']])
        plt.title('Box Plot of Deviations')
        plt.xlabel('Deviation Type')
        plt.ylabel('Deviation')
        plot_path = os.path.join(self.plot_dir, 'deviation_boxplot.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(plot_path)
        logging.info(f"Box Plot of Deviations сохранен: {plot_path}, время выполнения: {time.time() - start_plot_time:.2f} секунд")

        # Box Plot of Floor Deviations
        start_plot_time = time.time()
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[['floor_mean', 'floor_max', 'floor_min']])
        plt.title('Box Plot of Floor Deviations')
        plt.xlabel('Deviation Type')
        plt.ylabel('Deviation')
        plot_path = os.path.join(self.plot_dir, 'deviation_floor_boxplot.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(plot_path)
        logging.info(f"Box Plot of Floor Deviations сохранен: {plot_path}, время выполнения: {time.time() - start_plot_time:.2f} секунд")

        # Box Plot of Ceiling Deviations
        start_plot_time = time.time()
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[['ceiling_mean', 'ceiling_max', 'ceiling_min']])
        plt.title('Box Plot of Ceiling Deviations')
        plt.xlabel('Deviation Type')
        plt.ylabel('Deviation')
        plot_path = os.path.join(self.plot_dir, 'deviation_ceiling_boxplot.png')
        plt.savefig(plot_path)
        plt.close()
        plot_paths.append(plot_path)
        logging.info(f"Box Plot of Ceiling Deviations сохранен: {plot_path}, время выполнения: {time.time() - start_plot_time:.2f} секунд")

        # Scatter Plot
        start_plot_time = time.time()
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
        logging.info(f"Scatter Plot сохранен: {scatter_plot_path}, время выполнения: {time.time() - start_plot_time:.2f} секунд")

        # Pairplot
        start_plot_time = time.time()
        plt.figure(figsize=(10, 8))
        sns.pairplot(df[df.columns[3:]], diag_kind='kde')
        pairplot_path = os.path.join(self.plot_dir, 'pairplot.png')
        plt.savefig(pairplot_path)
        plt.close()
        plot_paths.append(pairplot_path)
        logging.info(f"Pairplot сохранен: {pairplot_path}, время выполнения: {time.time() - start_plot_time:.2f} секунд")

        # Relational Plot of Mean Deviation
        start_plot_time = time.time()
        plt.figure(figsize=(10, 6))
        sns.relplot(data=df, x="gt_corners", y="rb_corners")
        relplot_path = os.path.join(self.plot_dir, 'mean_deviation_relplot.png')
        plt.savefig(relplot_path)
        plt.close()
        plot_paths.append(relplot_path)
        logging.info(f"Relational Plot сохранен: {relplot_path}, время выполнения: {time.time() - start_plot_time:.2f} секунд")

        # Distribution Plot of gt_corners
        start_plot_time = time.time()
        plt.figure(figsize=(10, 6))
        plt.title('Distribution Plot of gt_corners')
        sns.histplot(data=df, x="gt_corners")
        gt_corners_histplot_path = os.path.join(self.plot_dir, 'gt_corners_histplot.png')
        plt.savefig(gt_corners_histplot_path)
        plt.close()
        plot_paths.append(gt_corners_histplot_path)
        logging.info(f"Гистограмма 'gt_corners' сохранена: {gt_corners_histplot_path}, время выполнения: {time.time() - start_plot_time:.2f} секунд")

        total_time = time.time() - start_time
        logging.info(f"Обработка файла {json_file} завершена за {total_time:.2f} секунд")

        return plot_paths
