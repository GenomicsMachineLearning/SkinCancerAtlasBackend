# app/plotting.py
import io
import matplotlib.pyplot as plt
import scanpy as scanpy

from app.models import SampleResponse
from app.platform import Platform


def generate_spatial_plot(sample: SampleResponse, adata, gene_id, cmap, alpha, spot_size=20,
                            legend_spot_size=1, dpi=200, flip_x=False, flip_y=False):
    """Generate a spatial plot for a given gene in AnnData object.

    Args:
        adata: AnnData object containing spatial data
        gene_id: Gene identifier to plot
        cmap: Colour map
        alpha: Alpha transparency for dots
        spot_size: Size of spots in the plot

    Returns:
        io.BytesIO: Buffer containing PNG image data
    """
    plt.clf()
    plt.close('all')

    if dpi > 300:
        dpi = 300

    fig = plt.figure(figsize=(6.4, 6.4), dpi=dpi)
    ax = fig.gca()
    scanpy.pl.spatial(
        adata,
        alpha_img=alpha,
        color=[gene_id],
        show=False,
        cmap=cmap,
        spot_size=spot_size,
        size=legend_spot_size,
        title="",
        ax=ax
    )

    if flip_x:
        ax.invert_xaxis()
    if flip_y:
        ax.invert_yaxis()

    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=dpi)

    content = buffer.getvalue()
    buffer.close()
    plt.close(fig)
    new_buffer = io.BytesIO(content)
    return new_buffer

def generate_cell_type_plot(sample: SampleResponse, adata, cmap, alpha, spot_size=20,
                            legend_spot_size=1, dpi=200, flip_x=False, flip_y=False):
    """Generate a spatial plot for a given gene in AnnData object.

    Args:
        adata: AnnData object containing spatial data
        gene_id: Gene identifier to plot
        cmap: Colour map
        alpha: Alpha transparency for dots
        spot_size: Size of spots in the plot
        legend_spot_size: Size of spots in the legend

    Returns:
        io.BytesIO: Buffer containing PNG image data
    """
    plt.clf()
    plt.close('all')

    if sample.platform == Platform.visium:
        cell_type_column = "cell_type"
    elif sample.platform == Platform.xenium:
        cell_type_column = "predicted.id"
    else:
        cell_type_column = "cell_type"

    if dpi > 300:
        dpi = 300

    fig = plt.figure(figsize=(6.4, 6.4), dpi=dpi)
    ax = fig.gca()
    scanpy.pl.spatial(
        adata,
        alpha_img=alpha,
        color=cell_type_column,
        show=False,
        cmap=cmap,
        spot_size=spot_size,
        size=legend_spot_size,
        title="",
        ax=ax
    )

    if flip_x:
        ax.invert_xaxis()
    if flip_y:
        ax.invert_yaxis()

    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=dpi)

    content = buffer.getvalue()
    buffer.close()
    plt.close(fig)
    new_buffer = io.BytesIO(content)
    return new_buffer