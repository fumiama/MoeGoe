import azure.functions as func

from io import BytesIO
from pathlib import Path
from torch import no_grad, LongTensor

import commons
from utils import load_checkpoint, get_hparams_from_file, wav2
from models import SynthesizerTrn
from text import text_to_sequence, _clean_text
from urllib.parse import unquote

from scipy.io.wavfile import write


class Cleaner():
    def __init__(self, configfile: str):
        self.cleanernames = get_hparams_from_file(str(Path(__file__).parent/configfile)).data.text_cleaners

    def main(self, req: func.HttpRequest) -> func.HttpResponse:
        text = req.params.get('text')
        if not text:
            return func.HttpResponse(
                "400 BAD REQUEST: null text",
                status_code=400
            )
        try:
            return func.HttpResponse(
                _clean_text(unquote(text), self.cleanernames),
                status_code=200
            )
        except:
            return func.HttpResponse(
                "400 BAD REQUEST: invalid text",
                status_code=400
            )


class Speaker():
    def __init__(self, configfile: str, pthfile: str):
        self.hps_ms = get_hparams_from_file(str(Path(__file__).parent/configfile))
        self.net_g_ms = SynthesizerTrn(
            len(self.hps_ms.symbols),
            self.hps_ms.data.filter_length // 2 + 1,
            self.hps_ms.train.segment_size // self.hps_ms.data.hop_length,
            n_speakers=self.hps_ms.data.n_speakers,
            **self.hps_ms.model)
        _ = self.net_g_ms.eval()
        load_checkpoint(str(Path(__file__).parent/pthfile), self.net_g_ms)

    def get_text(self, text: str, cleaned=False):
        if cleaned:
            text_norm = text_to_sequence(text, self.hps_ms.symbols, [])
        else:
            text_norm = text_to_sequence(text, self.hps_ms.symbols, self.hps_ms.data.text_cleaners)
        if self.hps_ms.data.add_blank:
            text_norm = commons.intersperse(text_norm, 0)
        text_norm = LongTensor(text_norm)
        return text_norm

    def main(self, req: func.HttpRequest) -> func.HttpResponse:
        text = req.params.get('text')
        cleantext = req.params.get('cleantext')
        if not text and not cleantext:
            return func.HttpResponse(
                "400 BAD REQUEST: null text",
                status_code=400
            )
        if text and cleantext:
            return func.HttpResponse(
                "400 BAD REQUEST: text and cleantext cannot be set both",
                status_code=400
            )
        cleaned = False
        if cleantext:
            cleaned = True
            text = cleantext
        speaker_id = req.params.get('id')
        if not speaker_id:
            speaker = req.params.get('name')
            npc_list = ['空', '荧', '派蒙', '纳西妲', '阿贝多', '温迪', '枫原万叶', '钟离', '荒泷一斗', '八重神子', '艾尔海森', '提纳里', '迪希雅', '卡维', '宵宫', '莱依拉', '赛诺', '诺艾尔', '托马', '凝光', '莫娜', '北斗', '神里绫华', '雷电将军', '芭芭拉', '鹿野院平藏', '五郎', '迪奥娜', '凯亚', '安柏', '班尼特', '琴', '柯莱', '夜兰', '妮露', '辛焱', '珐露珊', '魈', '香菱', '达达利亚', '砂糖', '早柚', '云堇', '刻晴', '丽莎', '迪卢克', '烟绯', '重云', '珊瑚宫心海', '胡桃', '可莉', '流浪者', '久岐忍', '神里绫人', '甘雨', '戴因斯雷布', '优菈', '菲谢尔', '行秋', '白术', '九条裟罗', '雷泽', '申鹤', '迪娜泽黛', '凯瑟琳', '多莉', '坎蒂丝', '萍姥姥', '罗莎莉亚', '留云借风真君', '绮良良', '瑶瑶', '七七', '奥兹', '米卡', '夏洛蒂', '埃洛伊', '博士', '女士', '大慈树王', '三月七', '娜塔莎', '希露瓦', '虎克', '克拉拉', '丹恒', '希儿', '布洛妮娅', '瓦尔特', '杰帕德', '佩拉', '姬子', '艾丝妲', '白露', '星', '穹', '桑博', '伦纳德', '停云', '罗刹', '卡芙卡', '彦卿', '史瓦罗', '螺丝咕姆', '阿兰', '银狼', '素裳', '丹枢', '黑塔', '景元', '帕姆', '可可利亚', '半夏', '符玄', '公输师傅', '奥列格', '青雀', '大毫', '青镞', '费斯曼', '绿芙蓉', '镜流', '信使', '丽塔', '失落迷迭', '缭乱星棘', '伊甸', '伏特加女孩', '狂热蓝调', '莉莉娅', '萝莎莉娅', '八重樱', '八重霞', '卡莲', '第六夜想曲', '卡萝尔', '姬子', '极地战刃', '布洛妮娅', '次生银翼', '理之律者', '真理之律者', '迷城骇兔', '希儿', '魇夜星渊', '黑希儿', '帕朵菲莉丝', '天元骑英', '幽兰黛尔', '德丽莎', '月下初拥', '朔夜观星', '暮光骑士', '明日香', '李素裳', '格蕾修', '梅比乌斯', '渡鸦', '人之律者', '爱莉希雅', '爱衣', '天穹游侠', '琪亚娜', '空之律者', '终焉之律者', '薪炎之律者', '云墨丹心', '符华', '识之律者', '维尔薇', '始源之律者', '芽衣', '雷之律者', '苏莎娜', '阿波尼亚', '陆景和', '莫弈', '夏彦', '左然', '标贝']
            speaker_id = npc_list.index(speaker)
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
        if speaker_id not in range(self.hps_ms.data.n_speakers):
            return func.HttpResponse(
                "400 BAD REQUEST: speaker id out of range",
                status_code=400
            )
        format = req.params.get('format')
        if not format: format = "ogg"
        if format not in ("ogg", "mp3", "wav"):
            return func.HttpResponse(
                "400 BAD REQUEST: invalid format",
                status_code=400
            )
        noise = req.params.get('noise')
        if not noise: noise = 0.5
        else:
            try:
                noise = float(noise)
                if noise < 0.1 or noise > 2.0: raise Exception("invalid noise")
            except:
                return func.HttpResponse(
                    "400 BAD REQUEST: invalid noise",
                    status_code=400
                )
        noisew = req.params.get('noisew')
        if not noisew: noisew = 0.6
        else:
            try:
                noisew = float(noisew)
                if noisew < 0.1 or noisew > 2.0: raise Exception("invalid noisew")
            except:
                return func.HttpResponse(
                    "400 BAD REQUEST: invalid noisew",
                    status_code=400
                )
        length = req.params.get('length')
        if not length: length = 1.3
        else:
            try:
                length = float(length)
                if length < 0.3 or length > 2.0: raise Exception("invalid length")
            except:
                return func.HttpResponse(
                    "400 BAD REQUEST: invalid length",
                    status_code=400
                )
        try:
            stn_tst = self.get_text(unquote(text), cleaned)
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
                audio = self.net_g_ms.infer(
                    x_tst, x_tst_lengths, sid=sid,
                    noise_scale=noise, noise_scale_w=noisew, length_scale=length
                )[0][0,0].data.cpu().float().numpy()
                with BytesIO() as f:
                    write(f, self.hps_ms.data.sampling_rate, audio)
                    if format == "wav":
                        return func.HttpResponse(
                            f.getvalue(),
                            status_code=200,
                            mimetype="audio/wav",
                        )
                    else:
                        f.seek(0, 0)
                        with BytesIO() as ofp:
                            wav2(f, ofp, format)
                            return func.HttpResponse(
                                ofp.getvalue(),
                                status_code=200,
                                mimetype="audio/mpeg" if format == "mp3" else "audio/ogg",
                            )
        except Exception as e:
            return func.HttpResponse(
                        "500 Internal Server Error\n"+str(e),
                        status_code=500,
                    )
