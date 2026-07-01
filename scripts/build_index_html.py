#!/usr/bin/env python3
"""Build the standalone HTML listening demo from the selection manifest."""

from __future__ import annotations

import csv
from collections import defaultdict
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "selection_manifest.csv"
TRANSCRIPTS = ROOT / "transcripts.csv"
OUT = ROOT / "index.html"
OUT_MD = ROOT / "index.md"

METHOD_INFO = {
    "Auth": {
        "description": "Authentic VoxTube speech",
        "refs": [("VoxTube", "https://doi.org/10.21437/Interspeech.2023-1083")],
    },
    "OHNN-HiFiGAN": {
        "description": "OHNN speaker anonymization with HiFi-GAN vocoder",
        "refs": [
            ("OHNN", "https://doi.org/10.1109/TASLP.2023.3313429"),
            ("HiFi-GAN", "https://proceedings.neurips.cc/paper/2020/hash/c5d736809766d46260d816d8dbc9eb44-Abstract.html"),
        ],
    },
    "OHNN-BigVGAN-SC": {
        "description": "OHNN speaker anonymization with BigVGAN vocoder and speaker-consistency training",
        "refs": [
            ("OHNN", "https://doi.org/10.1109/TASLP.2023.3313429"),
            ("BigVGAN", "https://openreview.net/forum?id=iTtGCMDEzS_"),
        ],
    },
    "SALT-k4": {
        "description": "SALT speaker anonymization with four-speaker mixture; k=4",
        "refs": [("SALT", "https://doi.org/10.1109/ASRU57964.2023.10389719")],
    },
    "SALT-k8": {
        "description": "SALT speaker anonymization with eight-speaker mixture; k=8",
        "refs": [("SALT", "https://doi.org/10.1109/ASRU57964.2023.10389719")],
    },
    "DAIEN-NCFG(-1.0)": {
        "description": "DAIEN-TTS with negative classifier-free guidance; gamma=-1.0",
        "refs": [
            ("DAIEN-TTS", "https://doi.org/10.1109/ICASSP55912.2026.11460953"),
            ("CFG", "https://doi.org/10.48550/arXiv.2207.12598"),
        ],
    },
    "DAIEN-NCFG(-0.75)": {
        "description": "DAIEN-TTS with negative classifier-free guidance; gamma=-0.75",
        "refs": [
            ("DAIEN-TTS", "https://doi.org/10.1109/ICASSP55912.2026.11460953"),
            ("CFG", "https://doi.org/10.48550/arXiv.2207.12598"),
        ],
    },
    "DAIEN-NCFG(-0.5)": {
        "description": "DAIEN-TTS with negative classifier-free guidance; gamma=-0.5",
        "refs": [
            ("DAIEN-TTS", "https://doi.org/10.1109/ICASSP55912.2026.11460953"),
            ("CFG", "https://doi.org/10.48550/arXiv.2207.12598"),
        ],
    },
}


def audio_tag(path: str) -> str:
    media_type = "audio/mpeg" if path.endswith(".mp3") else "audio/wav"
    src = escape(path, quote=True)
    return f'<audio controls preload="none"><source src="{src}" type="{media_type}"></audio>'


def markdown_audio_tag(path: str) -> str:
    media_type = "audio/mpeg" if path.endswith(".mp3") else "audio/wav"
    src = escape(path, quote=True)
    return f'<audio controls><source src="{src}" type="{media_type}"></audio>'


def markdown_refs(refs: list[tuple[str, str]]) -> str:
    return ", ".join(f"[{label}]({url})" for label, url in refs)


def html_refs(refs: list[tuple[str, str]]) -> str:
    return ", ".join(
        f'<a href="{escape(url, quote=True)}">{escape(label)}</a>' for label, url in refs
    )


def load_transcripts() -> dict[str, str]:
    if not TRANSCRIPTS.exists():
        return {}
    with TRANSCRIPTS.open(newline="", encoding="utf-8") as f:
        return {row["utterance_id"]: row["transcript"] for row in csv.DictReader(f)}


def build_markdown(
    rows: list[dict[str, str]], method_order: list[str], transcripts: dict[str, str]
) -> None:
    by_speaker: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_speaker[int(row["speaker_index"])].append(row)

    parts = [
        "# VoxTubeS Listening Demo",
        "",
        "This page provides a small listening set for VoxTubeS, with five randomly selected speakers and three utterances per speaker from the English development split. Each utterance is shown with its Whisper large-v3-turbo transcript, the authentic VoxTube clip, and aligned privacy-aware synthetic variants.",
        "",
        "The source utterances are derived from [VoxTube](https://www.isca-archive.org/interspeech_2023/yakovlev23_interspeech.html), a speaker-recognition corpus collected from YouTube videos released under Creative Commons Attribution (CC BY) licenses. The examples here retain that source-license provenance and are intended to illustrate the paper's anonymization and synthesis conditions.",
        "",
        "## Methods",
        "",
        "| Method | Description | Reference |",
        "|---|---|---|",
    ]
    for method in method_order:
        info = METHOD_INFO[method]
        parts.append(
            f"| {method} | {info['description']} | {markdown_refs(info['refs'])} |"
        )

    parts.extend(["", "## Examples", ""])

    for speaker_index in sorted(by_speaker):
        speaker_rows = by_speaker[speaker_index]
        speaker_id = speaker_rows[0]["speaker_id"]
        utterances = {}
        for row in speaker_rows:
            utterances[int(row["utterance_index"])] = (
                row["utterance_id"],
                float(row["duration"]),
            )

        parts.append(f"### Speaker {speaker_index}: `{speaker_id}`")
        parts.append("")
        for utt_index in sorted(utterances):
            utt_id, duration = utterances[utt_index]
            parts.append(f"- U{utt_index}: `{utt_id}` ({duration:.1f} s)")
            transcript = transcripts.get(utt_id)
            if transcript:
                parts.append(f"  - Transcript: {transcript}")
        parts.extend(["", "| Method | U1 | U2 | U3 |", "|---|---|---|---|"])

        row_lookup = {
            (int(row["utterance_index"]), row["method"]): row for row in speaker_rows
        }
        for method in method_order:
            cells = [method]
            for utt_index in (1, 2, 3):
                row = row_lookup[(utt_index, method)]
                cells.append(markdown_audio_tag(row["local_audio"]))
            parts.append("| " + " | ".join(cells) + " |")
        parts.append("")

    OUT_MD.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    transcripts = load_transcripts()

    by_speaker: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_speaker[int(row["speaker_index"])].append(row)

    method_order: list[str] = []
    for row in rows:
        method = row["method"]
        if method not in method_order:
            method_order.append(method)

    build_markdown(rows, method_order, transcripts)

    parts: list[str] = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>VoxTubeS Listening Demo</title>",
        "<style>",
        ":root { color-scheme: light; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }",
        "body { margin: 0; background: #f7f8fa; color: #1f2328; }",
        "main { max-width: 1180px; margin: 0 auto; padding: 28px 18px 48px; }",
        "h1 { margin: 0 0 8px; font-size: 30px; }",
        "h2 { margin: 28px 0 10px; font-size: 22px; }",
        "h3 { margin: 28px 0 8px; font-size: 18px; }",
        "p, li { line-height: 1.45; }",
        ".notice { border-left: 4px solid #57606a; background: #fff; padding: 10px 14px; }",
        "table { width: 100%; border-collapse: collapse; margin: 12px 0 20px; background: #fff; }",
        "th, td { border: 1px solid #d0d7de; padding: 8px 10px; vertical-align: middle; }",
        "th { background: #f0f3f6; text-align: left; }",
        ".method { width: 180px; font-weight: 600; }",
        ".utterance-list { margin-top: 8px; }",
        ".transcript { margin: 3px 0 8px 20px; max-width: 900px; color: #57606a; }",
        ".transcript span { font-weight: 600; color: #24292f; }",
        "code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.92em; }",
        "audio { width: 100%; max-width: 260px; height: 32px; }",
        "@media (max-width: 760px) {",
        "  main { padding: 20px 10px 36px; }",
        "  table { display: block; overflow-x: auto; white-space: nowrap; }",
        "  th, td { min-width: 180px; }",
        "  .method { min-width: 150px; }",
        "}",
        "</style>",
        "</head>",
        "<body>",
        "<main>",
        "<h1>VoxTubeS Listening Demo</h1>",
        "<p>This page provides a small listening set for VoxTubeS, with five randomly selected speakers and three utterances per speaker from the English development split. Each utterance is shown with its Whisper large-v3-turbo transcript, the authentic VoxTube clip, and aligned privacy-aware synthetic variants.</p>",
        '<p class="notice">The source utterances are derived from <a href="https://www.isca-archive.org/interspeech_2023/yakovlev23_interspeech.html">VoxTube</a>, a speaker-recognition corpus collected from YouTube videos released under Creative Commons Attribution (CC BY) licenses. The examples here retain that source-license provenance and are intended to illustrate the paper&apos;s anonymization and synthesis conditions.</p>',
        "<h2>Methods</h2>",
        "<table>",
        "<thead><tr><th>Method</th><th>Description</th><th>Reference</th></tr></thead>",
        "<tbody>",
    ]

    for method in method_order:
        info = METHOD_INFO[method]
        parts.append(
            "<tr>"
            f"<td class=\"method\">{escape(method)}</td>"
            f"<td>{escape(info['description'])}</td>"
            f"<td>{html_refs(info['refs'])}</td>"
            "</tr>"
        )

    parts.extend(["</tbody>", "</table>", "<h2>Examples</h2>"])

    for speaker_index in sorted(by_speaker):
        speaker_rows = by_speaker[speaker_index]
        speaker_id = speaker_rows[0]["speaker_id"]
        utterances = {}
        for row in speaker_rows:
            utterances[int(row["utterance_index"])] = (
                row["utterance_id"],
                float(row["duration"]),
            )

        parts.append(f"<h3>Speaker {speaker_index}: <code>{escape(speaker_id)}</code></h3>")
        parts.append('<ul class="utterance-list">')
        for utt_index in sorted(utterances):
            utt_id, duration = utterances[utt_index]
            transcript = transcripts.get(utt_id)
            parts.append(
                f"<li>U{utt_index}: <code>{escape(utt_id)}</code> ({duration:.1f} s)"
            )
            if transcript:
                parts.append(
                    '<div class="transcript"><span>Transcript:</span> '
                    f"{escape(transcript)}</div>"
                )
            parts.append("</li>")
        parts.append("</ul>")

        row_lookup = {
            (int(row["utterance_index"]), row["method"]): row for row in speaker_rows
        }
        parts.extend(
            [
                "<table>",
                "<thead><tr><th>Method</th><th>U1</th><th>U2</th><th>U3</th></tr></thead>",
                "<tbody>",
            ]
        )
        for method in method_order:
            cells = [f'<td class="method">{escape(method)}</td>']
            for utt_index in (1, 2, 3):
                row = row_lookup[(utt_index, method)]
                cells.append(f"<td>{audio_tag(row['local_audio'])}</td>")
            parts.append("<tr>" + "".join(cells) + "</tr>")
        parts.extend(["</tbody>", "</table>"])

    parts.extend(["</main>", "</body>", "</html>", ""])

    OUT.write_text("\n".join(parts), encoding="utf-8")


if __name__ == "__main__":
    main()
