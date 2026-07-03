import ptlflow

# List available models
print(ptlflow.get_model_names())

# Load a pretrained model (downloads checkpoint if not present)
model = ptlflow.get_model('raft', ckpt_path='sintel')
