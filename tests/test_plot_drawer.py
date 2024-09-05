import os
import pytest
import tempfile
import pandas as pd
import plot_drawer


@pytest.fixture
def sample_json(tmpdir):
    data = {
        'mean': [1, 2, 3, 4, 5],
        'max': [5, 6, 7, 8, 9],
        'min': [0, 1, 2, 3, 4],
        'floor_mean': [1, 2, 3, 4, 5],
        'floor_max': [5, 6, 7, 8, 9],
        'floor_min': [0, 1, 2, 3, 4],
        'ceiling_mean': [1, 2, 3, 4, 5],
        'ceiling_max': [5, 6, 7, 8, 9],
        'ceiling_min': [0, 1, 2, 3, 4],
        'gt_corners': [1, 2, 3, 4, 5],
        'rb_corners': [5, 6, 7, 8, 9],
    }
    df = pd.DataFrame(data)
    json_path = os.path.join(tmpdir, 'test_data.json')
    df.to_json(json_path)
    return json_path


def test_plot_drawer_creates_plots(sample_json):
    with tempfile.TemporaryDirectory() as tmpdirname:
        drawer = plot_drawer.PlotDrawer(plot_dir=tmpdirname)
        plot_paths = drawer.draw_plots(sample_json)
        assert len(plot_paths) == 8

        for plot_path in plot_paths:
            assert os.path.exists(plot_path)
