import sentencepiece as spm
from os.path import join
import pkg_resources

sentencepiece_processor = spm.SentencePieceProcessor()
DATA = pkg_resources.resource_filename("myutils", "data")
print("DATA",DATA)
model_file = join(DATA, "sentencepiece.model")
sentencepiece_processor.Load(model_file)

def to_tokens(sentence):
    return sentencepiece_processor.EncodeAsPieces(sentence)

def to_ids(sentence):
    return sentencepiece_processor.EncodeAsIds(sentence)

def from_ids(ids):
    return sentencepiece_processor.DecodeIds(ids)

def from_tokens(tokens):
    return sentencepiece_processor.DecodePieces(tokens)

def train(train_file, vocab_size=1000, model_type='bpe', character_coverage=1.0):
    spm.SentencePieceTrainer.Train(f'--input={train_file} --model_prefix={join(DATA, "sentencepiece")} --vocab_size={vocab_size} --character_coverage={character_coverage} --model_type={model_type}')
    sentencepiece_processor.Load(model_file)

def load(new_file):
    global model_file
    model_file = new_file

if __name__ == "__main__":
    s = "Mary had a little lambda"
    toks = to_tokens(s)
    ids = to_ids(s)
    print(f"Input:  '{s}'")
    print(f"Output: '{from_tokens(toks)}'")
    print(f"Output: '{from_ids(ids)}'")
