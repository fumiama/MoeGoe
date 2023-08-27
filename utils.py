import logging
from json import loads
from torch import load
import logging
from av import open as avopen


class HParams():
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      if type(v) == dict:
        v = HParams(**v)
      self[k] = v

  def keys(self):
    return self.__dict__.keys()

  def items(self):
    return self.__dict__.items()

  def values(self):
    return self.__dict__.values()

  def __len__(self):
    return len(self.__dict__)

  def __getitem__(self, key):
    return getattr(self, key)

  def __setitem__(self, key, value):
    return setattr(self, key, value)

  def __contains__(self, key):
    return key in self.__dict__

  def __repr__(self):
    return self.__dict__.__repr__()


def load_checkpoint(checkpoint_path, model):
  checkpoint_dict = load(checkpoint_path, map_location='cpu')
  iteration = checkpoint_dict['iteration']
  saved_state_dict = checkpoint_dict['model']
  if hasattr(model, 'module'):
    state_dict = model.module.state_dict()
  else:
    state_dict = model.state_dict()
  for k, v in state_dict.items():
    if k not in saved_state_dict:
      logging.info("%s is not in the checkpoint" % k)
      saved_state_dict[k] = v
  del state_dict
  if hasattr(model, 'module'):
    model.module.load_state_dict(saved_state_dict)
  else:
    model.load_state_dict(saved_state_dict)
  logging.info("Loaded checkpoint '{}' (iteration {})" .format(
    checkpoint_path, iteration))
  del saved_state_dict, checkpoint_dict
  return


def get_hparams_from_file(config_path):
  with open(config_path, "r") as f:
    data = f.read()
  config = loads(data)

  hparams = HParams(**config)
  return hparams

def wav2(i, o, format):
  inp = avopen(i, 'rb')
  out = avopen(o, 'wb', format=format)
  if format == "ogg": format = "libvorbis"

  ostream = out.add_stream(format)

  for frame in inp.decode(audio=0):
      for p in ostream.encode(frame): out.mux(p)

  for p in ostream.encode(None): out.mux(p)

  out.close()
  inp.close()
