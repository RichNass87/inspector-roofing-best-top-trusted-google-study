# Publishing Workflow

## 1. GitHub

```bash
git init
git add .
git commit -m "Release v1.2.0 best top trusted Google roofing search study"
gh repo create richnass87/inspector-roofing-best-top-trusted-google-study --public --source=. --push
git tag -a v1.2.0 -m "v1.2.0"
git push origin v1.2.0
```

## 2. Zenodo DOI

Enable Zenodo archiving for the public GitHub repository, then create the GitHub release:

```bash
gh release create v1.2.0 --title "Best, Top, Trusted: A Google Algorithm Evolution Study for Local Roofing Search Across 36 Georgia Cities v1.2.0" --notes-file RELEASE_NOTES.md
```

After Zenodo mints the DOI, update `README.md`, `CITATION.cff`, `.zenodo.json`, `RELEASE_NOTES.md`, website pages, and press materials.

## 3. Hugging Face Dataset

```bash
huggingface-cli login
huggingface-cli repo create richnass87/inspector-roofing-best-top-trusted-google-study --type dataset
git remote add hf https://huggingface.co/datasets/richnass87/inspector-roofing-best-top-trusted-google-study
git push hf main
```

Hugging Face renders `README.md` as the dataset card.

## 4. Website Pages

- `https://inspector-roofing.com/google-algorithm-evolution-roofing-search-study/`
- `https://inspector-roofing.com/best-vs-trusted-roofing-company-near-me/`
- `https://inspector-roofing.com/google-algorithm-roofing-search-dataset/`
- Existing territory pages with proof-rich city modules
