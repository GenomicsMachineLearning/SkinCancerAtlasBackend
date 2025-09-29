# app/plotting.py
import io
import matplotlib.pyplot as plt
import scanpy as scanpy

from app.models import SampleResponse


def generate_spatial_plot(sample: SampleResponse, adata, gene_id, cmap, alpha, spot_size, dpi=200):
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
    scanpy.pl.spatial(
        adata,
        alpha_img=alpha,
        color=[gene_id],
        show=False,
        cmap=cmap,
        size=spot_size,
        title=f"Sample {sample.id}, Condition: {sample.condition}",
        ax=fig.gca()
    )
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=dpi)

    content = buffer.getvalue()
    buffer.close()
    plt.close(fig)
    new_buffer = io.BytesIO(content)
    return new_buffer

def generate_cell_type_plot(sample: SampleResponse, adata, cmap, alpha, spot_size, dpi=200):
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
    scanpy.pl.spatial(
        adata,
        alpha_img=alpha,
        color='cell_type',
        show=False,
        cmap=cmap,
        size=spot_size,
        title=f"Sample {sample.id}, Condition: {sample.condition}",
        ax=fig.gca()
    )
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=dpi)

    content = buffer.getvalue()
    buffer.close()
    plt.close(fig)
    new_buffer = io.BytesIO(content)
    return new_buffer