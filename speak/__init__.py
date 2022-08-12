import azure.functions as func

from io import BytesIO
from pathlib import Path
from torch import no_grad, LongTensor

import commons
import utils
from models import SynthesizerTrn
from text import text_to_sequence
from urllib.parse import unquote

from scipy.io.wavfile import write

model = str(Path(__file__).parent/'243_epochs.pth')
config = str(Path(__file__).parent/'config.json')
hps_ms = utils.get_hparams_from_file(config)
net_g_ms = SynthesizerTrn(
    len(hps_ms.symbols),
    hps_ms.data.filter_length // 2 + 1,
    hps_ms.train.segment_size // hps_ms.data.hop_length,
    n_speakers=hps_ms.data.n_speakers,
    **hps_ms.model)
_ = net_g_ms.eval()
_ = utils.load_checkpoint(model, net_g_ms, None)

def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.symbols, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = LongTensor(text_norm)
    return text_norm

def main(req: func.HttpRequest) -> func.HttpResponse:
    text = req.params.get('text')
    if not text:
        return func.HttpResponse(
             "400 BAD REQUEST: null text",
             status_code=400
        )
    speaker_id = req.params.get('id')
    if not speaker_id:
        return func.HttpResponse(
             "400 BAD REQUEST: null speaker id",
             status_code=400
        )
    try:
        speaker_id = int(speaker_id)
    except:
        return func.HttpResponse(
             "400 BAD REQUEST: invalid speaker id",
             status_code=400
        )
    try:
        stn_tst = get_text(unquote(text), hps_ms)
    except:
        return func.HttpResponse(
            "400 BAD REQUEST: invalid text",
            status_code=400
        )
    try:
        with no_grad():
            x_tst = stn_tst.unsqueeze(0)
            x_tst_lengths = LongTensor([stn_tst.size(0)])
            sid = LongTensor([speaker_id])
            audio = net_g_ms.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][0,0].data.cpu().float().numpy()
        with BytesIO() as f:
            write(f, hps_ms.data.sampling_rate, audio)
            return func.HttpResponse(
                f.getvalue(),
                status_code=200,
                mimetype="audio/wav",
            )
    except Exception as e:
        return func.HttpResponse(
            "500 Internal Server Error\n"+e,
            status_code=500
        )
