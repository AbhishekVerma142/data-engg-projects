from PIL import Image
import numpy as np
import pathlib
import random
import tensorflow as tf

DATA_PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "chest_xray"
random.seed(42)
print(DATA_PATH)

def get_image_paths() -> list:
    """
    Returns a list of all image paths in the data directory inside tuples of the form (label, path) with
    1 for PNEUMONIA and 0 for NORMAL. Make sure that the list is shuffled
    """
    image_paths = []
    image_paths.extend((0, image_path) for image_path in DATA_PATH.glob("**/NORMAL/*.jpeg"))
    image_paths.extend((1, image_path) for image_path in DATA_PATH.glob("**/PNEUMONIA/*.jpeg"))

    random.shuffle(image_paths)

    return image_paths


def process_image(path: str) -> np.ndarray:
    """
    Returns a numpy array of shape (256, 256, 1) with the image data from the given path
    """
    process_image_lambda = lambda path: np.expand_dims(np.array(Image.open(path).convert('L').resize((256, 256)), dtype=np.float32) / 255.0, axis=-1)
    return process_image_lambda(path)


def write_image(writer, image, label):
    """
    Writes the given image and label to the given writer
    """
    image = image.astype(np.float64)
    feature = {
        "image": tf.train.Feature(
            bytes_list=tf.train.BytesList(value=[image.tobytes()])
        ),
        "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
    }
    example = tf.train.Example()
    example.features.feature["image"].bytes_list.value.extend([image.tobytes()])
    example.features.feature["label"].int64_list.value.extend([label])
    writer.write(example.SerializeToString())


def main():
    writer = tf.io.TFRecordWriter("dataset.tfrecords")
    for label, path in get_image_paths():
        image = process_image(path)
        write_image(writer, image, label)


if __name__ == "__main__":
    print(get_image_paths())
