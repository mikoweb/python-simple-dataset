from src.dataset.Labels import Labels as BaseLabels


class Labels(BaseLabels):
    def __init__(self):
        super().__init__((
            'symboling',
            'normalized-losses',
            'make',
            'fuel-type',
            'aspiration',
            'num-of-doors',
            'body-style',
            'drive-wheels',
            'engine-location',
            'wheel-base',
            'length',
            'width',
            'height',
            'curb-weight',
            'engine-type',
            'num-of-cylinders',
            'engine-size',
            'fuel-system',
            'bore',
            'stroke',
            'compression-ratio',
            'horsepower',
            'peak-rpm',
            'city-mpg',
            'highway-mpg',
            'price'
        ))
