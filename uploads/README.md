# uploads/

Source PDFs, recordings and data files, one per cited work, for **offline citation
verification**. A reviewer checking a citation reads the file here rather than
chasing a URL that may have moved.

Name each file after the reference id it backs: `uploads/<id>.pdf`.

This is not the reference list — that is authored content. This directory is
the evidence behind it.

## 2026-10-06 CRDM walkthrough recording and transcripts (`folio-assistant-1r0p`, `folio-assistant-uphx`)

| File | SHA-256 | Bytes | Description |
|---|---|---:|---|
| `output.mp4` | `5cdd6c09ef690a0f516f4277fefdb000fee849292ff04ca6ef7d8c85116cabb3` | 24,776,789 | Walkthrough video (17:09, H.264 1920×1080 16 fps, AAC mono 16 kHz audio, English, two speakers: Carl Leitner and Chinemerem Chika Eyetan). |
| `Quick-touchbase-re_-Ref-arc-feedback-and-Assured-AI-WS1.vtt` | `299ebd7d212f767a321f89da52fb002d9290a037f7ec60e1d7491d736bed410a` | 42,055 | Microsoft Teams WebVTT auto-caption export (275 cues, 2,474 words). |
| `Quick-touchbase-re_-Ref-arc-feedback-and-Assured-AI-WS1.docx` | `87f5017b2c19c1b9db1c11132caff83097ade39b8d615797054b29b1243dcbfd` | 693,476 | Microsoft Teams `.docx` transcript export (67 speaker turns, 2,469 words; same recognition as the `.vtt`, 98.0% word similarity). |
| `output.whisper-base.json` | `d72b592bd85f9e1b4e5ffb674b692f2517c47e989154dffe05a52cdd26e6bd2c` | 35,950 | Independent transcript generated offline with `whisper.cpp` (`ggml-base.bin`, 139 timed segments, 2,395 words). |

### Provenance (`output.whisper-base.json`, `folio-assistant-iqim` / `folio-assistant-1r0p`)

- **Tool**: [`ggml-org/whisper.cpp`](https://github.com/ggml-org/whisper.cpp) (`./build/bin/whisper-cli`, Tool node `transcribe-whisper-cpp`), commit `231638a0717b7822784297e5980965ffcec05810`
- **Model**: `models/ggml-base.bin` (`base`, multilingual, 147,951,465 bytes), SHA-256 `60ed5bc3dd14eea856493d334349b405782ddcaf0028d4b5df4088345fba2efe`
- **Audio extraction**: `ffmpeg -i uploads/output.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le output.wav` (FFmpeg 9.0.2 / `Lavf63.1.102`, 16 kHz mono 16-bit PCM, 1,028.992 s, 32,927,822 bytes), WAV SHA-256 `e63fba5ee95c5c2e973ed8cc1739bb409978713c6f883c2cc374132fe49fef01`
- **Invocation**: `./build/bin/whisper-cli -m models/ggml-base.bin -f output.wav -oj -of output.whisper-base`

### Library entry (`folio-assistant-1r0p`)

`library/crdm-walkthrough-2026-10-06/` files this recording: `recording.json` (title, date, language and speakers from the Teams record; `source.sha256` is `output.mp4` above) and `transcript/en.json`, the `whisper.cpp` transcript as it came out, in state `draft`. Written by `cat-harness-tools/scripts/recording-transcript.py`. Translations go beside it as `transcript/<lang>.json`; names it mishears (`Carl Lightner`, `Ginny`) are a reviewer's to correct.

### Agreement with Microsoft Teams exports

Word-level comparison after lower-casing and stripping punctuation (`meeting-recording.py compare`, `difflib.SequenceMatcher` with `autojunk=False`):

| Pair | Words (A vs B) | Matched words | Word similarity (`SequenceMatcher`) | Word edits (S / D / I) | Edit rate vs A |
|---|---:|---:|---:|---:|---:|
| Teams `.vtt` vs `output.whisper-base.json` | 2,474 vs 2,395 | 2,269 | **0.932** (93.2%) | 66 / 139 / 60 | 10.7% |
| Teams `.docx` vs `output.whisper-base.json` | 2,469 vs 2,395 | 2,250 | **0.925** (92.5%) | 76 / 143 / 69 | 11.7% |
| Teams `.vtt` vs Teams `.docx` (same recogniser) | 2,474 vs 2,469 | 2,421 | **0.980** (98.0%) | 5 / 48 / 43 | 3.9% |
| Teams `.vtt` vs Vosk `small-en` (earlier run, `uphx`) | 2,474 vs 2,610 | — | **0.802** (80.2%) | — | — |

Most of the 139 word deletions against the `.vtt` are listener back-channels (`"okay"`, `"yeah"`, `"mhm"`) that Teams recorded on the listener's separate microphone channel while the active speaker was talking; in the mixed mono track of `output.mp4`, `whisper.cpp` transcribes the primary speaker without interleaving quiet back-channels.

### Name, term, and coverage differences (`Teams .vtt` vs `whisper.cpp base`)

| Timestamp | Teams `.vtt` | `whisper.cpp` (`ggml-base.bin`) | Notes / Ground-truth reading |
|---|---|---|---|
| `0:05` | `"Carl Lightner"` | `"Carl Lightner"` | Both misspell **Carl Leitner** (Vosk `small-en` had `"leitner"`). |
| `0:12` | `"CRDM"` | `"CRDM"` | Both agree on **CRDM** (Collaborative Requirements Development Methodology). |
| `0:54` | `"Chinni Eyetan"` | `"Ginny Aie turn"` | Teams had speaker metadata; **Chinemerem Chika (Chinni) Eyetan**. |
| `2:21`, `2:26` | `"change sets"` | `"change sets"` | Both agree at 2:21–2:26; both have `"chain sets"` at `8:49`. |
| `2:28`, `3:34` | `"CS001"`, `"CS164"` | `"CS 001"`, `"CS 164"` | Both agree on change-set IDs **CS-001** and **CS-164**. |
| `2:45` | `"DPIF"` | `"DPI F"` | `whisper.cpp` separates the initialism (**DPI-F**). |
| `3:27` | `"Tini"` | *(omitted back-channel)* | Teams misheard **Chinni** as `"Tini"`. |
| `3:45` | `"Saroop"` | `"Saroop"` | Both agree on `"Saroop"` at 3:45 (colleague on product registry WG). |
| `4:18` | `"co-pilot"` | `"Copilot"` | Both recognise **GitHub Copilot**. |
| `7:53` | `"reviewed by the editorial team in terms of WHO"` | `"reviewed by the editorial team in terms of WHO"` | `whisper.cpp` confirms Teams' reading on REQ-02 (where Vosk had `"the it team in terms of the beach"`). |
| `9:56–10:08` | *(12 s omitted in `.vtt` and `.docx`)* | `"So, for example, we have the GDHP comments. Actually, to share the couple of ones that went into the reference architecture, I think it went to the reference architecture. Sorry, it went to the smart email mailbox."` | **Recovered by `whisper.cpp`**: Teams dropped a 12-second utterance naming the **GDHP comments** and the **SMART email mailbox** right before `10:11` (`"and some of them might not have been routed properly to the mailbox..."`). |
| `10:11` | `"routed"` | `"rooted"` | UK/US spelling variant of the same word (`routed`). |
| `14:14` | `"philtres"` | `"filters"` | `whisper.cpp` corrects Teams' `"philtres"` to **filters**. |
| `14:35` | `"Jiun"` | `"Ginny"` | Both mishear **Chinni** (`"Jiun"` vs `"Ginny"`). |
| `14:49` | `"Swarupu"` | `"Sorrupa"` | Same colleague named at 3:45 (`"Saroop"` / `"Swarupu"` / `"Sorrupa"`). |
| `15:43`, `16:28` | `"WHO"`, `"WHO Iris"` | `"WHO"`, `"WHO, IRIS"` | Both agree on **WHO** and **WHO IRIS**. |
| `16:11` | `"Nat shared"` | `"not shared"` | Unresolved proper name vs negation (`"Nat shared"` vs `"not shared"`). |
| `17:03–17:09` | *(cues end at `17:03.7`)* | `"Thank you. And I'll stop the recording now, but yeah, that's great. What I can also"` | `whisper.cpp` captures the final 5.3 seconds before the recording stops. |
