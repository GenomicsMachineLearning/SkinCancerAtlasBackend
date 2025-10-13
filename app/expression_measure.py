import enum as enum
import numpy as numpy
import pandas as pandas

class ExpressionMeasure(str, enum.Enum):
    total = "total"
    non_zero_mean = "non_zero_mean"
    mean = "mean"
    median = "median"
    mad = "mad"
    std = "std"

    @staticmethod
    def apply_measure_adata(adata, measure, gene_names, limit):

        # Get data as numpy array
        if hasattr(adata.X, 'toarray'):
            expression_matrix = adata.X.toarray()
        else:
            expression_matrix = adata.X

        return ExpressionMeasure.apply_measure(expression_matrix, measure, gene_names,
                                               limit)

    @staticmethod
    def apply_measure(expression_matrix, measure, gene_names, limit):
        # Apply measure
        if measure == ExpressionMeasure.total:
            agg_expression = numpy.sum(expression_matrix, axis=0)
        elif measure == ExpressionMeasure.non_zero_mean:
            agg_expression = numpy.array([
                numpy.mean(expression_matrix[:, i][expression_matrix[:, i] > 0])
                if numpy.any(expression_matrix[:, i] > 0) else 0
                for i in range(expression_matrix.shape[1])
            ])
        elif measure == ExpressionMeasure.mean:
            agg_expression = numpy.mean(expression_matrix, axis=0)
        elif measure == ExpressionMeasure.median:
            agg_expression = numpy.median(expression_matrix, axis=0)
        elif measure == ExpressionMeasure.std:
            agg_expression = numpy.std(expression_matrix, axis=0)
        elif measure == ExpressionMeasure.mad:
            median_vals = numpy.median(expression_matrix, axis=0)
            mad_vals = numpy.median(
                numpy.abs(expression_matrix - median_vals),
                axis=0
            )
            agg_expression = mad_vals
        else:
            agg_expression = None
        # Turn into panda object
        if agg_expression is not None:
            gene_expression_df = pandas.DataFrame({
                'gene': gene_names,
                'agg_expression': agg_expression
            })
            gene_expression_df = gene_expression_df.sort_values('agg_expression',
                                                                ascending=False)
            ordered_genes = gene_expression_df['gene'][0:limit].tolist()
        else:
            ordered_genes = None
        return ordered_genes

    def __str__(self):
        return self.value