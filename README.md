# Document Image Classifier

This is a simple image classifier based on the [Inception model](https://github.com/google/inception) to get predictions on whether a supplied image is a document or not.

## Getting Started

Install Python dependencies using [PIP](https://pip.pypa.io/en/stable/):

```
pip install -r requirements.txt
```

## Training

Add training images in the `training/images` directory like shown below. Due to the usage of the Inception model you can achieve great results with a relatively small data set (~100 images for each category).

```
├── training
│   ├── images
│   │   ├── documents [your training images]
│   │   └── random    [your training images]
```

Once we have the training images we can start the process of retraining the Inception model.

```
scripts/training.sh
```

## Predictions

**Notice that this image classifier currently only works with JPEG images.**

```
$ python src/prediction.py <YOUR_IMAGE_URL>
> document (score = 0.99978)
> random (score = 0.00022)
```

## Rest-API (development-only)

For development purposes you can run a simple REST endpoint to serve predictions. For serious production use something like [TensorFlow Serving](https://tensorflow.github.io/serving/) is highly recommended.

```
export FLASK_APP="api.py"
export FLASK_DEBUG=1

flask run
```
