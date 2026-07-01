# VoxTubeS Listening Demo

Random speaker-balanced examples for comparing authentic VoxTube speech with privacy-aware synthetic variants.

> Public research demo. These short clips are selected examples for the VoxTubeS paper and should not be treated as a complete corpus release. Please do not attempt to identify speakers or redistribute the audio outside the context of reviewing or discussing the research demo.

- Seed: `20260616`
- Speakers: `5`
- Utterances per speaker: `3`
- Source split: English development manifests

## Methods

| Method | Description |
|---|---|
| Auth | Authentic VoxTube |
| OHNN-HiFiGAN | OHNN analysis-and-synthesis with HiFiGAN |
| OHNN-BigVGAN-SC | OHNN + BigVGAN + speaker consistency |
| SALT-k4 | SALT latent transformation with k=4 |
| SALT-k8 | SALT latent transformation with k=8 |
| DAIEN-NCFG(-1.0) | DAIEN-TTS negative speech CFG, gamma=-1.0 |
| DAIEN-NCFG(-0.75) | DAIEN-TTS negative speech CFG, gamma=-0.75 |
| DAIEN-NCFG(-0.5) | DAIEN-TTS negative speech CFG, gamma=-0.5 |

## Examples

### Speaker 1: `UCqhOC3lFQV17UcTdHVhUwow`

- U1: `UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008` (4.0 s)
  - Transcript: 9D. Painted Desert. And 9A.
- U2: `UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001` (4.0 s)
  - Transcript: I don't even know. I'll show you. Maybe you can figure this out.
- U3: `UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008` (4.0 s)
  - Transcript: I might actually have a gaming night with the kids. I reckon we might pull

| Method | U1 | U2 | U3 |
|---|---|---|---|
| Auth | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/01_UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/02_UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/03_UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008/auth.mp3" type="audio/mpeg"></audio> |
| OHNN-HiFiGAN | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/01_UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/02_UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/03_UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008/ohnn_hifigan.wav" type="audio/wav"></audio> |
| OHNN-BigVGAN-SC | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/01_UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/02_UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/03_UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> |
| SALT-k4 | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/01_UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/02_UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/03_UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008/salt_k4.wav" type="audio/wav"></audio> |
| SALT-k8 | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/01_UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/02_UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/03_UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008/salt_k8.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-1.0) | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/01_UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/02_UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/03_UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008/daien_ncfg_m1p0.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.75) | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/01_UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/02_UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/03_UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008/daien_ncfg_m0p75.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.5) | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/01_UCqhOC3lFQV17UcTdHVhUwow-2ubJ_lOlAw4-seg000008/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/02_UCqhOC3lFQV17UcTdHVhUwow-67aofxDjdOU-seg000001/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/01_UCqhOC3lFQV17UcTdHVhUwow/03_UCqhOC3lFQV17UcTdHVhUwow-BOhAzbSCS2E-seg000008/daien_ncfg_m0p5.wav" type="audio/wav"></audio> |

### Speaker 2: `UCZz58phVC9FWtYfcdd_IrOw`

- U1: `UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005` (4.0 s)
  - Transcript: of your charger so start saving a little bit of room and traveling a little
- U2: `UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002` (4.0 s)
  - Transcript: you know, the GoPro can be, you know, either gender, men, women. I mean, this is just a
- U3: `UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004` (4.0 s)
  - Transcript: Friday night is always pizza night in this house, so let's

| Method | U1 | U2 | U3 |
|---|---|---|---|
| Auth | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/01_UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/02_UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/03_UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004/auth.mp3" type="audio/mpeg"></audio> |
| OHNN-HiFiGAN | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/01_UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/02_UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/03_UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004/ohnn_hifigan.wav" type="audio/wav"></audio> |
| OHNN-BigVGAN-SC | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/01_UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/02_UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/03_UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> |
| SALT-k4 | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/01_UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/02_UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/03_UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004/salt_k4.wav" type="audio/wav"></audio> |
| SALT-k8 | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/01_UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/02_UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/03_UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004/salt_k8.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-1.0) | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/01_UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/02_UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/03_UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004/daien_ncfg_m1p0.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.75) | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/01_UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/02_UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/03_UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004/daien_ncfg_m0p75.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.5) | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/01_UCZz58phVC9FWtYfcdd_IrOw-AcWZcVz_TdE-seg000005/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/02_UCZz58phVC9FWtYfcdd_IrOw-DyOmyXhYjcE-seg000002/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/02_UCZz58phVC9FWtYfcdd_IrOw/03_UCZz58phVC9FWtYfcdd_IrOw-naUyElrd8s4-seg000004/daien_ncfg_m0p5.wav" type="audio/wav"></audio> |

### Speaker 3: `UCI__mod_SOk7w1oTG9jvwDg`

- U1: `UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002` (4.0 s)
  - Transcript: what's going on guys and welcome back to a new video for those of you that are new to the channel
- U2: `UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002` (4.0 s)
  - Transcript: thisworks.tm I will try and find it but like I said just
- U3: `UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005` (4.0 s)
  - Transcript: the ones that you know can be optimized

| Method | U1 | U2 | U3 |
|---|---|---|---|
| Auth | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/01_UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/02_UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/03_UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005/auth.mp3" type="audio/mpeg"></audio> |
| OHNN-HiFiGAN | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/01_UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/02_UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/03_UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005/ohnn_hifigan.wav" type="audio/wav"></audio> |
| OHNN-BigVGAN-SC | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/01_UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/02_UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/03_UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> |
| SALT-k4 | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/01_UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/02_UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/03_UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005/salt_k4.wav" type="audio/wav"></audio> |
| SALT-k8 | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/01_UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/02_UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/03_UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005/salt_k8.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-1.0) | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/01_UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/02_UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/03_UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005/daien_ncfg_m1p0.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.75) | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/01_UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/02_UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/03_UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005/daien_ncfg_m0p75.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.5) | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/01_UCI__mod_SOk7w1oTG9jvwDg-8jamAMgRsS8-seg000002/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/02_UCI__mod_SOk7w1oTG9jvwDg-GYSv0ig1Xow-seg000002/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/03_UCI__mod_SOk7w1oTG9jvwDg/03_UCI__mod_SOk7w1oTG9jvwDg-vHtYjqOrzno-seg000005/daien_ncfg_m0p5.wav" type="audio/wav"></audio> |

### Speaker 4: `UCqwLHNFtrOjrOC3CnvviS1g`

- U1: `UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004` (4.0 s)
  - Transcript: So this is what if you want to do
- U2: `UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004` (4.0 s)
  - Transcript: and field headers also, if you put it on it, you will find it. So the report is like this.
- U3: `UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008` (4.0 s)
  - Transcript: I don't need all of them, but all of them need content.

| Method | U1 | U2 | U3 |
|---|---|---|---|
| Auth | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/01_UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/02_UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/03_UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008/auth.mp3" type="audio/mpeg"></audio> |
| OHNN-HiFiGAN | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/01_UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/02_UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/03_UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008/ohnn_hifigan.wav" type="audio/wav"></audio> |
| OHNN-BigVGAN-SC | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/01_UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/02_UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/03_UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> |
| SALT-k4 | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/01_UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/02_UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/03_UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008/salt_k4.wav" type="audio/wav"></audio> |
| SALT-k8 | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/01_UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/02_UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/03_UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008/salt_k8.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-1.0) | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/01_UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/02_UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/03_UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008/daien_ncfg_m1p0.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.75) | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/01_UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/02_UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/03_UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008/daien_ncfg_m0p75.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.5) | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/01_UCqwLHNFtrOjrOC3CnvviS1g-FfmAXS57wHY-seg000004/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/02_UCqwLHNFtrOjrOC3CnvviS1g-WFOxhIoHAhY-seg000004/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/04_UCqwLHNFtrOjrOC3CnvviS1g/03_UCqwLHNFtrOjrOC3CnvviS1g-ryNJOzsm71c-seg000008/daien_ncfg_m0p5.wav" type="audio/wav"></audio> |

### Speaker 5: `UChyS0pZKG5Qa_8UqDMp8hhg`

- U1: `UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011` (4.0 s)
  - Transcript: of enjoyment as long as you're not sinning and you're not going against the Lord. I'm not getting like...
- U2: `UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009` (4.0 s)
  - Transcript: slash vlogging video room and I'm just revamping it
- U3: `UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005` (4.0 s)
  - Transcript: am just doing a little one two three check right in front of the lights the lighting was good want to make sure my

| Method | U1 | U2 | U3 |
|---|---|---|---|
| Auth | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/01_UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/02_UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009/auth.mp3" type="audio/mpeg"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/03_UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005/auth.mp3" type="audio/mpeg"></audio> |
| OHNN-HiFiGAN | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/01_UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/02_UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009/ohnn_hifigan.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/03_UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005/ohnn_hifigan.wav" type="audio/wav"></audio> |
| OHNN-BigVGAN-SC | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/01_UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/02_UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/03_UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005/ohnn_bigvgan_sc.wav" type="audio/wav"></audio> |
| SALT-k4 | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/01_UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/02_UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009/salt_k4.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/03_UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005/salt_k4.wav" type="audio/wav"></audio> |
| SALT-k8 | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/01_UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/02_UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009/salt_k8.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/03_UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005/salt_k8.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-1.0) | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/01_UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/02_UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009/daien_ncfg_m1p0.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/03_UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005/daien_ncfg_m1p0.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.75) | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/01_UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/02_UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009/daien_ncfg_m0p75.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/03_UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005/daien_ncfg_m0p75.wav" type="audio/wav"></audio> |
| DAIEN-NCFG(-0.5) | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/01_UChyS0pZKG5Qa_8UqDMp8hhg-3BT71qALFZU-seg000011/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/02_UChyS0pZKG5Qa_8UqDMp8hhg-Kli_JCb6KXY-seg000009/daien_ncfg_m0p5.wav" type="audio/wav"></audio> | <audio controls><source src="audio/05_UChyS0pZKG5Qa_8UqDMp8hhg/03_UChyS0pZKG5Qa_8UqDMp8hhg-S-1UsB6STo8-seg000005/daien_ncfg_m0p5.wav" type="audio/wav"></audio> |

## Release Note

Before publication, manually review every example, preserve the required source attribution and license metadata, and remove any sample that is unsuitable for public release.
