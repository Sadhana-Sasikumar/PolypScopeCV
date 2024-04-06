import mlflow.tensorflow
import tensorflow as tf
from train import iou  # Import your custom metric function from the training script

if __name__ == "__main__":
    # Define the custom metric function
    def iou(y_true, y_pred):
        ...  # Define your IoU calculation logic here

    # Load the trained model from the H5 file
    with tf.keras.utils.custom_object_scope({'iou': iou}):
        model = tf.keras.models.load_model("files\model.h5")

    # Save the model with MLflow
    mlflow.tensorflow.log_model(tf_saved_model_dir="model_v1", tf_meta_graph_tags=None,
                                tf_signature_def_map=None, artifact_path="model_v1", keras_model=model)
