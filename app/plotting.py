import io
import matplotlib.pyplot as plt
import scanpy as scanpy
from scanpy._utils import _empty

from app.models import SampleResponse
from app.platform import Platform


def generate_spatial_plot(adata, gene_id, cmap, alpha, library_id=None, spot_size=20,
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
    if library_id is None:
        library_id = _empty

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
        library_id=library_id,
        spot_size=spot_size,
        size=legend_spot_size,
        title="",
        ax=ax
    )

    # Make the colorbar more compact
    cbar = ax.collections[0].colorbar
    if cbar is not None:
        cbar.ax.tick_params(labelsize=8)
        cbar.ax.yaxis.set_major_locator(plt.MaxNLocator(5))
        ax_pos = ax.get_position()
        cbar_pos = cbar.ax.get_position()
        cbar.ax.set_position([
            cbar_pos.x0,
            ax_pos.y0,
            cbar_pos.width * 0.5,
            ax_pos.height
        ])

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

def generate_sample_cell_type_plot(sample: SampleResponse, adata, cmap, alpha,
                                   spot_size=20, library_id=None, legend_spot_size=1,
                                   dpi=200, flip_x=False, flip_y=False):
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
    if sample.platform == Platform.visium:
        cell_type_column = "cell_type"
    elif sample.platform == Platform.xenium:
        cell_type_column = "predicted.id"
    else:
        cell_type_column = "cell_type"

    return generate_cell_type_plot(adata, cell_type_column, cmap, alpha, spot_size,
                                   library_id, legend_spot_size, dpi, flip_x, flip_y)


def generate_cell_type_plot(adata, cell_type_column, cmap, alpha, spot_size, library_id,
                            legend_spot_size, dpi, flip_x, flip_y):
    if library_id is None:
        library_id = _empty
    plt.clf()
    plt.close('all')

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
        library_id=library_id,
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

def generate_umap(adata, spot_size, legend_spot_size, dpi, level='Level1'):
    plt.clf()
    plt.close('all')

    if dpi > 300:
        dpi = 300
    fig = plt.figure(figsize=(6.4, 6.4), dpi=dpi)
    ax = fig.gca()
    scanpy.pl.umap(
        adata,
        color=[level],
        show=False,
        size=spot_size,
        title="",
        ax=ax
    )
    legend = ax.get_legend()
    if legend:
        for handle in legend.legend_handles:
            handle.set_sizes([legend_spot_size])
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=dpi)
    content = buffer.getvalue()
    buffer.close()
    plt.close(fig)
    new_buffer = io.BytesIO(content)
    return new_buffer
