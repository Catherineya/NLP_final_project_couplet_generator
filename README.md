<img width="1191" alt="image" src="https://github.com/user-attachments/assets/25a85e17-69f9-4ade-9efa-5929ce36d8af" /># NLP_final_project_couplet_generator
 
# 🧾 Chinese Couplet Generator Based on Transformer

## 🧠 Overview

This project presents a **Transformer-based Chinese Couplet Generator**, designed to automatically generate the **lower line** of a traditional Chinese couplet when given the **upper line**. The model aims to preserve the syntactic symmetry and cultural aesthetics of classical Chinese duilian (对联), widely used during festivals like the Lunar New Year.

## 🏗️ Project Structure

- `chinese-couplets-generator-based-on-transformer.ipynb`: Main Jupyter notebook for training and generating couplets.
- `data/`: Folder for the training dataset (not included in this repo).
- `vocab.py`: Vocabulary building and token management.
- `model.py`: Transformer-based Encoder-Decoder architecture with attention.
- `utils.py`: Helper functions for training and generation (e.g., padding, batching).
- `Final_Project_Paper_for_Natural_Language_Processing.pdf`: Full project report.

## 🧰 Dependencies

```bash
pip install torch numpy tqdm matplotlib notebook
```

## 📚 Dataset

We used a cleaned Chinese couplet dataset containing over **74,000 lines**, excluding vulgar content. Each data point consists of an upper line and a corresponding lower line.

Dataset split:
- **Training set**: 80%
- **Validation set**: 20%

Tokenization includes:
- `<PAD>`: Padding
- `<BOS>`: Beginning of Sentence
- `<EOS>`: End of Sentence
- `<UNK>`: Unknown token

## 🧠 Model Architecture

- Transformer Encoder-Decoder architecture with:
  - Token & Positional Embeddings
  - Multi-head Attention Layers
  - Cross-Attention Decoder
- Loss Function: Cross-Entropy Loss
- Optimizer: Adam

## 🚀 Training

Training was done at 10, 20, 30, and 40 epochs with adjustable batch size and learning rate.

### Example:
```python
for epoch in range(num_epochs):
    train(model, train_loader)
    val_loss = evaluate(model, val_loader)
```

## 📊 Evaluation

### Quantitative:
| Epoch | Perplexity | Cross-Entropy |
|-------|------------|----------------|
| 10    | 27.44      | 3.39           |
| 30    | 22.95      | 3.09           |
| 40    | 22.29      | 3.02           |

### Human Evaluation:
- Blind tests with native speakers comparing generated vs. real lines.
- Ratings on syntactic symmetry, semantic fluency, and overall impression (scale: 1–5).

## 🌟 Sample Results

| Upper Line | Generated Lower Line (Epoch 40) |
|------------|---------------------------------|
| 对月赏荷吟风韵 | 临风听雨听雨声 |
| 临风披晓月 | 临水听清音 |
| 千古华堂奉君子 | 宗臣遗像肃清高 |

More in [`Final_Project_Paper_for_Natural_Language_Processing.pdf`](./Final_Project_Paper_for_Natural_Language_Processing.pdf).

## 🔮 Future Improvements

- Reduce character repetition in long lines
- Add rhyme and tone pattern alignment
- Develop automated stylistic scoring

## 👨‍💻 Contributors

- **Jianing Zhang** – jz5212@nyu.edu  
- **Haotong Wu** – hw2933@nyu.edu  
- **Xinwei Xie** – xx2185@nyu.edu
