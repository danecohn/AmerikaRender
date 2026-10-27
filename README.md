# Cohnsoft Render

<img src="src/amerika_render/cohnsoft/logos/mark/cohnsoft-mark.svg" alt="Cohnsoft" width="96">

**A product of Cohnsoft.** Founded by **Demetria Althea Cohn**.

Canonical identity and Cohn Sans are pinned to cohnsoftassets `752e894f90f1e58e62ae466352cb03c8bfd7d703`.



**Render**: Blender with an AI modelling assistant (an add-on plus launcher and branding). Powered by Blender (GPL-3.0-or-later); Blender is a trademark of the Blender Foundation; not affiliated or endorsed.

Developed by **Cohnsoft** for **Cohnsoft OS** (Ubuntu 26.10 ARM64): describe what you want, and the built-in assistant (Anthropic Claude, through your own API key) builds it. The key is stored in your login keyring by Studio and never reaches the app; see `docs/STUDIO-ARCHITECTURE.md` and `docs/README.md`. Local automation uses the existing Studio bridge; installing OpenClaw is not required.



Source layout: `src/` (installed under `/usr/share`), `tools/builders/render.py` (Debian package builder used by the Amerika OS build), `tests/`, `docs/render.md`.
Licence: GPL-3.0-only for Amerika code (see `LICENSE`); third-party licences are listed in `src/NOTICE`.

Existing package names, addon/operator IDs, project/config paths, scene files and Studio APIs remain compatible. Native package and extension archives include local brand resources and their licences. Custom interface fonts are preserved. Blender and historical upstream notices remain intact. Original product SVG and Sprite sources are included.
