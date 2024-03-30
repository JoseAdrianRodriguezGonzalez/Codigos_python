import pixellib
from pixellib.tune_bg import alter_bg
cambiar=alter_bg()
cambiar.load_pascalvoc_model("pysccript\deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
cambiar.color_bg("8x_canary_yellow_1.webp",colors=(255,255,255),output_image_name="../pysccript",detect="hat")