"""This modules demonstrates how to convert code to subtokenized sentences."""
import json
from sre_parse import FLAGS
from absl import app, flags
from tensor2tensor.data_generators import text_encoder

from cubert import code_to_subtokenized_sentences
from cubert import tokenizer_registry

FLAGS = flags.FLAGS
flags.DEFINE_string("vocabulary_filepath", None, "Path to the subword vocabulary.")

flags.DEFINE_string("input_filepath", None, "Path to the Python source code file.")

flags.DEFINE_string(
    "output_filepath", None, "Path to the output file of subtokenized source code."
)

flags.DEFINE_enum_class(
    "tokenizer",
    default=tokenizer_registry.TokenizerEnum.PYTHON,
    enum_class=tokenizer_registry.TokenizerEnum,
    help="The tokenizer to use.",
)


def main(argv):
    if len(argv) > 1:
        raise app.UsageError("Too many command-line arguments.")

    # The value of the `TokenizerEnum` is a `CuBertTokenizer` subclass.
    tokenizer = FLAGS.tokenizer.value()
    subword_tokenizer = text_encoder.SubwordTextEncoder(FLAGS.vocabulary_filepath)

    with open(FLAGS.input_filepath) as input_file:
        code = input_file.read()
        print("#" * 80)
        print("Original Code")
        print("#" * 80)
        print(code)

    subtokenized_sentences = code_to_subtokenized_sentences.code_to_cuber_sentences(
        code=code,
        initial_tokenizer=tokenizer,
        subword_tokenizer=subword_tokenizer,
    )

    print("#" * 80)
    print("CuBERT Sentences")
    print("#" * 80)
    print(subtokenized_sentences)


if __name__ == "__main__":
    flags.mark_flag_as_required("vocabulary_filepath")
    flags.mark_flag_as_required("input_filepath")
    flags.mark_flag_as_required("output_filepath")
    app.run(main)
