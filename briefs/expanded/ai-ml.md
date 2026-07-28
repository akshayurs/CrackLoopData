# Area: AI & Machine Learning (ai-ml)

Reference outline — L2 (Topics) and L3 (slide headings) expanded from `briefs/area-group-map.md` § Area 12. Pending human review/approval; nothing here is written content yet.

---

## Group: ML Fundamentals (ml-fundamentals)
*Tier: 🔵 Rec · Scope: train/test, bias-variance, metrics*

### Topic: ML Problem Framing (ml-problem-framing, beginner)
What machine learning actually is, the supervised/unsupervised/RL taxonomy, and how to decide whether a problem needs ML at all.
- Concept: What machine learning actually is — extracting a function from data instead of hand-writing rules
- Diagram: The ML taxonomy — supervised, unsupervised, reinforcement, and self-supervised learning
- Concept: When NOT to use ML — deterministic logic, too little data, or a hard explainability requirement
- Concept: Framing a business problem as an ML problem — inputs, output, and where labels come from
- Concept: Features and labels — what the model actually sees at training time
- Compare: Classification vs regression vs ranking vs clustering — matching the problem type to the output shape
- Pitfall: Optimizing a proxy metric that quietly diverges from the real business goal
- Diagram: The ML lifecycle end-to-end — data → train → evaluate → deploy → monitor
- Interview: "How do you decide if a problem actually needs ML?" ⭐
- Interview: "Walk me through the ML lifecycle for a brand-new product feature" ⭐

### Topic: Train/Test/Validation Splits (train-test-validation, beginner)
Splitting data so evaluation is honest — train/val/test, cross-validation, and the leakage bugs that invalidate both.
- Concept: Why evaluating on training data lies — memorization vs generalization
- Concept: The three-way split — train, validation, and test, and what each one is for
- Diagram: K-fold cross-validation
- Concept: Data leakage — temporal leakage, target leakage, and preprocessing leakage
- Compare: Hold-out vs cross-validation vs time-based split — when each is the right call
- Concept: Stratified sampling for imbalanced classes
- Pitfall: Shuffling time-series data before splitting it
- Concept: Nested cross-validation — tuning hyperparameters without leaking into the test set
- Code: `train_test_split(stratify=...)` and `StratifiedKFold` — the calls interviewers expect you to know
- Interview: "Train accuracy 99%, test accuracy 60% — what's wrong and how do you find out?" ⭐
- Interview: "How would you split data for a fraud detection model?" ⭐

### Topic: Bias-Variance Tradeoff (bias-variance-tradeoff, intermediate)
The single lens for diagnosing model error — underfitting vs overfitting, and which lever fixes which.
- Concept: The tradeoff defined — bias (underfitting) vs variance (overfitting)
- Diagram: Bias-variance decomposition of total expected error
- Concept: What high bias looks like in practice — train and validation error both high and close together
- Concept: What high variance looks like — low train error, high validation error, large gap
- Diagram: Learning curves and how to read them
- Concept: How model complexity, data size, and regularization each move the tradeoff
- Compare: Fixing high bias vs fixing high variance — different, sometimes opposite, playbooks
- Pitfall: Throwing more data at a high-bias problem instead of a more expressive model
- Interview: "Your model overfits — list every lever you'd pull, in order" ⭐
- Interview: "Explain the bias-variance tradeoff to a non-technical PM" ⭐

### Topic: Evaluation Metrics — Classification (evaluation-metrics-classification, intermediate)
Reading a confusion matrix correctly and picking the metric that matches the business cost of being wrong.
- Concept: The confusion matrix — true/false positives and negatives as the foundation
- Concept: Accuracy, and why it lies on imbalanced data
- Concept: Precision vs recall — the trade-off and what each protects against
- Concept: F1 and F-beta — weighting precision against recall
- Diagram: The ROC curve and what AUC measures
- Compare: ROC-AUC vs PR-AUC — why PR-AUC wins when the positive class is rare
- Concept: Choosing a decision threshold from the actual business cost of each error type
- Pitfall: Reporting 99% accuracy on a 99:1 imbalanced dataset
- Interview: "Fraud detection — which metric do you optimize for and why?" ⭐
- Interview: "Precision or recall — when do you deliberately favor one?" ⭐

### Topic: Evaluation Metrics — Regression & Ranking (evaluation-metrics-regression-ranking, intermediate)
Metrics beyond classification — regression error measures and the ranking metrics recommenders/search rely on.
- Concept: MAE vs MSE vs RMSE — how differently each penalizes large errors
- Concept: R² and its limits — misleading, and even negative in the wrong context
- Concept: Why ranked-output problems need different metrics than plain regression
- Concept: Precision@k and Recall@k
- Concept: NDCG — rewarding the correct order, not just the correct set
- Concept: MAP (Mean Average Precision) for ranked retrieval
- Compare: Ranking metrics vs classification metrics on the same underlying model
- Pitfall: Using raw RMSE to compare models whose targets are on different scales
- Interview: "How do you evaluate a search ranking model end to end?" ⭐

### Topic: Feature Engineering & Selection (feature-engineering-selection, intermediate)
The practical craft of turning raw data into model-ready features, and knowing which ones to keep.
- Concept: Why features often matter more than model choice
- Concept: Encoding categorical variables — one-hot, ordinal, and target/embedding encoding
- Concept: Scaling and normalization — standardization vs min-max, and which models actually need it
- Concept: Handling missing data — imputation strategies, and missingness itself as a signal
- Concept: Feature crosses and interaction terms
- Concept: Feature selection methods — filter, wrapper, and embedded (L1-based)
- Compare: Tree-based models vs linear/distance-based models — who needs feature engineering more
- Pitfall: Fitting a scaler or encoder on the whole dataset before splitting — leakage again
- Interview: "A categorical feature has 50,000 unique values — what do you do?" ⭐

### Topic: Regularization & Optimization Basics (regularization-optimization-basics, intermediate)
The shared optimization and regularization toolkit that both classical ML and deep learning build on.
- Concept: What regularization does — penalizing complexity to fight variance
- Compare: L1 (Lasso) vs L2 (Ridge) — sparsity vs shrinkage
- Concept: Gradient descent — the update rule and the learning-rate intuition
- Diagram: Batch vs stochastic vs mini-batch gradient descent
- Concept: Convex vs non-convex loss surfaces, and what "local minimum" means in practice
- Pitfall: Learning rate too high (diverges) vs too low (stuck or painfully slow)
- Interview: "Explain gradient descent to a non-technical interviewer" ⭐
- Interview: "L1 vs L2 regularization — when would you pick each?" ⭐

---

## Group: Supervised Learning (supervised-learning)
*Tier: 🔵 Rec · Scope: regression, trees, SVM, ensembles*

### Topic: Linear & Logistic Regression (linear-logistic-regression, beginner)
The two workhorse linear models — how they're fit, what their outputs mean, and why they're still used at scale.
- Concept: Linear regression — the model, and normal equation vs gradient descent as two ways to fit it
- Concept: The assumptions behind linear regression and what breaks when they don't hold
- Concept: Logistic regression — turning a linear score into a probability via the sigmoid
- Diagram: The decision boundary a logistic regression model draws
- Concept: Interpreting coefficients as odds ratios — the real reason it's still popular
- Concept: Multiclass extension — softmax and one-vs-rest
- Compare: Linear regression vs logistic regression — when each applies
- Pitfall: Using linear regression to predict a bounded or probability-like target
- Code: Fitting a logistic regression model and reading its coefficients as log-odds
- Interview: "Why is logistic regression still used in production at scale?" ⭐

### Topic: Decision Trees (decision-trees, beginner)
How a single decision tree splits data, where it overfits, and why it needs no feature scaling.
- Concept: How a decision tree splits — recursive partitioning of the feature space
- Concept: Impurity measures — Gini impurity vs entropy/information gain
- Diagram: A tree growing, split by split, on a toy dataset
- Concept: Overfitting in trees — depth, minimum samples per leaf, and pruning
- Concept: Regression trees — splitting on variance reduction instead of impurity
- Compare: Trees vs linear models — interpretability, non-linearity, no scaling required
- Pitfall: A fully-grown tree that has simply memorized the training set
- Interview: "Why don't decision trees need feature scaling?" ⭐

### Topic: Ensembles — Bagging & Random Forest (ensembles-bagging-random-forest, intermediate)
Why averaging many models reduces variance, and how random forest turns that into a practical algorithm.
- Concept: The wisdom-of-crowds intuition — why averaging independent models helps
- Concept: Bagging (bootstrap aggregating) — the mechanics
- Concept: Random forest — bagging plus feature randomness, and why that decorrelates the trees
- Diagram: A random forest aggregating predictions across trees
- Concept: Out-of-bag error as a free validation estimate
- Concept: Feature importance from a forest, and where it's misleading
- Pitfall: Feature-importance bias toward high-cardinality features
- Interview: "Why does random forest rarely overfit even with very deep trees?" ⭐

### Topic: Boosting, GBM & XGBoost (boosting-gbm-xgboost, advanced)
Sequential ensembling — boosting theory, gradient boosting, and the XGBoost/LightGBM defaults interviewers probe.
- Concept: Boosting intuition — each new model corrects the previous ensemble's errors
- Concept: AdaBoost — reweighting misclassified examples each round
- Concept: Gradient boosting — fitting residuals via gradient descent in function space
- Diagram: Boosting rounds progressively reducing residual error
- Concept: What XGBoost/LightGBM add in practice — built-in regularization, histogram binning, native missing-value handling
- Compare: Bagging vs boosting — the bias/variance story, and parallel vs sequential training
- Compare: Random forest vs gradient boosting — when each wins in practice
- Pitfall: Boosting overfitting with too many rounds or too high a learning rate — why early stopping matters
- Code: A minimal XGBoost fit using `early_stopping_rounds` and a validation set
- Interview: "Random forest vs XGBoost — which do you reach for, and why?" ⭐
- Interview: "How does gradient boosting actually use gradients?" ⭐

### Topic: SVM & Kernels (svm-kernels, advanced)
Maximum-margin classification and the kernel trick — a classic that still gets asked.
- Concept: The max-margin idea — why the widest separating boundary generalizes best
- Diagram: Support vectors and the margin
- Concept: Soft margin — the C parameter and tolerating some misclassification
- Concept: The kernel trick — an implicit high-dimensional mapping without ever computing it
- Concept: Common kernels — linear, RBF, and polynomial — and when to use each
- Compare: SVM vs logistic regression
- Pitfall: SVMs scaling poorly to very large datasets — why they're less common in industry now
- Interview: "Explain the kernel trick without the math" ⭐

### Topic: KNN & Naive Bayes (knn-naive-bayes, beginner)
Two simple, still-asked baselines — instance-based KNN and probabilistic Naive Bayes.
- Concept: K-Nearest Neighbors — lazy learning and distance metrics
- Concept: Choosing k — trading bias against variance via neighborhood size
- Pitfall: KNN needs feature scaling and degrades in high dimensions (curse of dimensionality)
- Concept: Naive Bayes — the conditional-independence assumption
- Concept: Why Naive Bayes still works well despite a technically "wrong" assumption
- Compare: KNN vs Naive Bayes — instance-based vs probabilistic, and when to reach for each
- Interview: "Why is it called 'naive,' and why does it still work?" ⭐

### Topic: Handling Imbalanced Data (handling-imbalanced-data, intermediate)
Training a genuinely good model when the positive class is rare — resampling, weighting, and thresholds.
- Concept: Why imbalance breaks naive training — the model collapses to predicting the majority class
- Concept: Resampling — oversampling (SMOTE), undersampling, and their trade-offs
- Concept: Class weighting inside the loss function
- Concept: Threshold moving vs retraining the model
- Compare: Resampling vs class weights vs an anomaly-detection framing for extreme imbalance
- Pitfall: Applying SMOTE before the train/test split — leakage again
- Interview: "1% positive-class fraud data — how do you approach training?" ⭐

---

## Group: Unsupervised Learning (unsupervised-learning)
*Tier: 🟡 Breadth · Scope: clustering, dimensionality reduction*

### Topic: Clustering — K-Means & Hierarchical (clustering-kmeans-hierarchical, beginner)
Grouping unlabeled data — K-means mechanics and hierarchical clustering as the two entry-point methods.
- Concept: What clustering solves — finding groups without labels
- Concept: K-means mechanics — assign, update, repeat
- Concept: Choosing k — the elbow method and silhouette score
- Diagram: K-means converging over several iterations
- Pitfall: K-means assumes roughly spherical, similarly-sized clusters
- Concept: Hierarchical clustering — agglomerative merging into a dendrogram
- Diagram: A dendrogram, and where to cut it
- Compare: K-means vs hierarchical clustering — scalability vs flexibility
- Interview: "How do you pick k with no ground-truth labels?" ⭐

### Topic: Density & Probabilistic Clustering (clustering-density-gmm, intermediate)
Clustering beyond K-means — density-based DBSCAN and probabilistic Gaussian Mixture Models.
- Concept: DBSCAN — density-based clusters and explicit noise points
- Concept: DBSCAN's parameters — eps and minPts, and how they change the result
- Compare: DBSCAN vs K-means — arbitrary shapes, no need to pick k upfront, native outlier handling
- Concept: Gaussian Mixture Models — soft, probabilistic cluster assignment
- Concept: Expectation-Maximization at a glance — how a GMM is actually fit
- Compare: Soft (GMM) vs hard (K-means) clustering — when a soft assignment matters
- Interview: "Your data has clusters of very different shapes and densities — what do you reach for?" ⭐

### Topic: Dimensionality Reduction — PCA (dimensionality-reduction-pca, intermediate)
PCA end to end — the most-asked unsupervised technique in ML interviews.
- Concept: The curse of dimensionality — why fewer, better dimensions help
- Concept: PCA intuition — finding the directions of maximum variance
- Diagram: Principal components drawn over a 2D scatter
- Concept: Eigenvectors and eigenvalues of the covariance matrix — the mechanism, kept intuitive
- Concept: Choosing the number of components — explained-variance ratio and the scree plot
- Pitfall: Running PCA without standardizing features first
- Concept: What you lose — the interpretability of the transformed features
- Interview: "Explain PCA to someone non-technical" ⭐
- Interview: "When would you deliberately not use PCA before modeling?" ⭐

### Topic: Dimensionality Reduction — t-SNE & UMAP (dimensionality-reduction-tsne-umap, advanced)
Modern nonlinear visualization techniques, and why they're easy to misread compared to PCA.
- Concept: Why linear PCA fails to capture nonlinear structure
- Concept: t-SNE — preserving local neighborhoods when projecting to low dimensions
- Pitfall: Over-interpreting t-SNE cluster sizes and inter-cluster distances — they aren't meaningful
- Concept: UMAP — a similar goal to t-SNE, faster, and better global-structure preservation
- Compare: PCA vs t-SNE vs UMAP — linear vs nonlinear, speed, and visualization vs preprocessing use cases
- Interview: "Why shouldn't you feed t-SNE output into a downstream classifier?" ⭐
- Interview: "1000 features down to 50 for a downstream model — PCA or UMAP?" ⭐

### Topic: Anomaly Detection (anomaly-detection, intermediate)
Finding rare, abnormal points without relying on labeled examples of them.
- Concept: Framing anomaly detection as density estimation — rare means low probability
- Concept: Simple statistical methods — z-score and IQR-based outlier flags
- Concept: Isolation forest — isolating anomalies via random partitioning
- Concept: Autoencoder-based anomaly detection via reconstruction error (cross-link deep-learning/autoencoders-generative-basics)
- Compare: Supervised fraud classification vs unsupervised anomaly detection — when labels are scarce
- Pitfall: Evaluating an anomaly detector with plain accuracy instead of precision/recall on the rare class
- Interview: "You have almost no labeled fraud examples — how do you detect anomalies at all?" ⭐

---

## Group: Deep Learning (deep-learning)
*Tier: 🔵 Rec · Scope: NNs, backprop, CNNs/RNNs, training*

### Topic: Neural Network Basics (neural-network-basics, beginner)
From a single perceptron to a multi-layer network, and why non-linear activations are what make it work.
- Concept: The perceptron — a weighted sum plus activation, functioning as a linear classifier
- Concept: Why we stack layers — the multi-layer perceptron and non-linear activation functions
- Concept: Common activations — sigmoid, tanh, ReLU — and why ReLU became the default
- Diagram: A feedforward network's architecture — input, hidden, and output layers
- Concept: Universal approximation, intuitively — why deep nets can fit almost any function
- Pitfall: Deep sigmoid/tanh networks and the vanishing-gradient problem they invite
- Interview: "Why did ReLU replace sigmoid as the default activation function?" ⭐

### Topic: Backpropagation & Training (backpropagation-training, intermediate)
The mechanism that actually trains a neural network — forward pass, backprop, and the fixes that make it stable.
- Concept: The forward pass — computing the loss from inputs to output
- Concept: Backpropagation — the chain rule propagating gradients backward through the network
- Diagram: A computational graph and its gradient flow
- Concept: Why backprop is efficient — reusing intermediate gradients instead of differentiating from scratch each time
- Concept: Weight initialization — Xavier/He initialization and why it matters
- Pitfall: Vanishing and exploding gradients in deep networks
- Concept: Batch normalization — stabilizing activations from layer to layer
- Code: Autograd — how a framework computes gradients automatically without you writing a single derivative
- Interview: "Derive backpropagation from scratch on a small network" ⭐
- Interview: "Your deep network's loss isn't moving — how do you debug it?" ⭐

### Topic: Optimizers & Training Dynamics (optimizers-training-dynamics, intermediate)
The optimizers and schedules that actually train deep nets, building on plain gradient descent.
- Concept: SGD with momentum — smoothing out noisy gradient steps
- Concept: Adam — adaptive per-parameter learning rates, and why it's the default
- Compare: SGD+momentum vs Adam — generalization vs convergence speed
- Concept: Learning-rate schedules — warmup, decay, and cosine annealing
- Concept: Batch size effects — gradient noise, generalization, and hardware throughput
- Pitfall: A fixed, too-high learning rate that plateaus training early
- Interview: "Why does Adam sometimes generalize worse than plain SGD?" ⭐

### Topic: Regularization in Deep Nets (regularization-deep-nets, intermediate)
The DL-specific regularization toolkit — dropout, augmentation, and early stopping.
- Concept: Dropout — randomly zeroing units to prevent co-adaptation
- Concept: Why dropout acts like an implicit ensemble
- Concept: Data augmentation as regularization, especially for vision
- Concept: Early stopping using the validation loss curve
- Concept: Weight decay vs L2 — subtly different once you're using an adaptive optimizer
- Pitfall: Leaving dropout active at inference time
- Interview: "Your model overfits badly — what deep-learning-specific levers do you pull?" ⭐

### Topic: CNN Architecture (cnn-architecture, intermediate)
Convolution mechanics and the classic architectures that make CNNs parameter-efficient on images.
- Concept: The convolution operation — kernels, stride, and padding
- Diagram: A convolution kernel sliding across an image
- Concept: Why convolution captures spatial locality and translation invariance via parameter sharing
- Concept: Pooling layers — downsampling, and why it helps
- Concept: The classic CNN stack and how the receptive field grows with depth
- Concept: Landmark architectures at a glance — LeNet → AlexNet → VGG → ResNet's skip connections
- Pitfall: Vanishing gradients in very deep CNNs without skip connections
- Code: A small CNN — a `Conv2d → ReLU → MaxPool` stack
- Interview: "Why do CNNs need far fewer parameters than a fully-connected net on the same image?" ⭐

### Topic: RNN, LSTM & Sequence Models (rnn-lstm-sequence-models, intermediate)
The pre-transformer sequence toolkit — RNN, LSTM, and GRU — and why attention eventually replaced them.
- Concept: RNNs — sharing weights across a sequence, with a hidden state as memory
- Diagram: An RNN unrolled through time
- Pitfall: Vanishing/exploding gradients over long sequences — why vanilla RNNs forget
- Concept: LSTM — forget/input/output gates as the fix for long-range memory
- Concept: GRU as a simpler alternative to LSTM
- Compare: RNN vs LSTM vs GRU — capacity vs compute cost
- Concept: Why attention and transformers eventually replaced RNNs for most sequence tasks (cross-link nlp/attention-transformer-architecture)
- Interview: "Why can't vanilla RNNs handle long sequences well?" ⭐

### Topic: Autoencoders & Generative Basics (autoencoders-generative-basics, advanced)
Learning compressed representations and the two classic generative model families before diffusion.
- Concept: Autoencoders — encoder/decoder learning a compressed representation
- Concept: Practical uses — denoising, dimensionality reduction, anomaly detection (cross-link unsupervised-learning/anomaly-detection)
- Concept: Variational autoencoders — a probabilistic latent space you can actually sample from
- Concept: GANs at a glance — generator vs discriminator in adversarial training
- Pitfall: GAN training instability and mode collapse
- Compare: VAEs vs GANs — sample quality vs training stability vs likelihood estimation
- Interview: "How does a VAE differ from a plain autoencoder?" ⭐

---

## Group: Natural Language Processing (nlp)
*Tier: 🔵 Rec · Scope: embeddings, transformers, tasks*

### Topic: Text Preprocessing & Representation (text-preprocessing-representation, beginner)
Turning raw text into model-ready input, from tokenization through classic vector representations.
- Concept: The NLP pipeline — tokenization, normalization, stopword handling
- Concept: Bag-of-Words and TF-IDF — representing text as vectors
- Pitfall: Bag-of-Words/TF-IDF losing word order and semantics
- Concept: N-grams — capturing a little local order
- Concept: Subword tokenization (BPE/WordPiece) and why it beats word-level tokenization
- Code: Building a TF-IDF matrix in a few lines and inspecting the top terms per document
- Interview: "Why did tokenization move from whole words to subwords?" ⭐

### Topic: Word Embeddings (word-embeddings, intermediate)
The semantic-vector breakthrough — word2vec and GloVe, and the limitation that motivated contextual models.
- Concept: The distributional hypothesis — a word is known by the company it keeps
- Concept: word2vec — CBOW vs skip-gram
- Diagram: Embeddings placing semantically similar words near each other in vector space
- Concept: The classic analogy example (king − man + woman ≈ queen) and what it actually reveals
- Concept: GloVe — global co-occurrence statistics vs word2vec's local context windows
- Pitfall: Static embeddings can't handle polysemy — one fixed vector for "bank" the river and "bank" the institution
- Compare: Static embeddings vs contextual embeddings — a preview of what transformers fix
- Interview: "What limitation of word2vec did transformers actually solve?" ⭐

### Topic: Attention & Transformer Architecture (attention-transformer-architecture, advanced)
The single most important architecture in modern AI — self-attention and the full Transformer block.
- Concept: The bottleneck problem attention solves — a fixed-size context vector in old seq2seq models
- Concept: The attention mechanism — query/key/value, intuitively
- Diagram: Self-attention computing a weighted context for one token
- Concept: Multi-head attention — why several attention "views" beat one
- Concept: Positional encoding — injecting order into a mechanism that has none by default
- Diagram: The full Transformer block — attention, feedforward, residual connections, and normalization
- Concept: Encoder-only vs decoder-only vs encoder-decoder — the three architecture families and their use cases
- Compare: Transformers vs RNNs — parallel training and long-range dependencies
- Pitfall: Quadratic attention cost with sequence length — why long context is expensive
- Code: Scaled dot-product attention in about ten lines of pseudocode
- Interview: "Explain self-attention from scratch" ⭐
- Interview: "Why do Transformers parallelize better than RNNs during training?" ⭐

### Topic: Contextual Models — the BERT Family (contextual-models-bert-family, advanced)
BERT-style pretraining — the encoder side of the Transformer story, and when it beats calling an LLM.
- Concept: Contextual embeddings — the same word gets a different vector depending on context
- Concept: BERT's pretraining objectives — masked language modeling and next-sentence prediction
- Concept: Fine-tuning BERT for downstream tasks — classification, NER, and QA heads
- Diagram: BERT's bidirectional context vs GPT's left-to-right context (cross-link llms/llm-architecture-scaling)
- Concept: Sentence-level embeddings via pooled BERT output, used for semantic search (cross-link llms/retrieval-augmented-generation)
- Compare: Encoder-only (BERT) vs decoder-only (GPT) — understanding tasks vs generation tasks
- Interview: "When would you fine-tune a BERT-style model instead of just calling an LLM API?" ⭐

### Topic: Core NLP Tasks (core-nlp-tasks, intermediate)
The NLP task landscape and the standard approach to each — the "how would you build X" interview questions.
- Concept: Text classification (sentiment, topic) — pipeline and metrics
- Concept: Named Entity Recognition — framed as sequence labeling
- Concept: Machine translation — the seq2seq framing and the BLEU score
- Concept: Question answering — extractive vs generative QA
- Concept: Text summarization — extractive vs abstractive
- Compare: Rule-based/classical ML vs fine-tuned transformer vs LLM-prompted — three ways to solve the same task
- Interview: "How would you build a support-ticket auto-tagger?" ⭐

### Topic: Language Modeling Fundamentals (language-modeling-fundamentals, intermediate)
What a language model actually predicts, from n-grams to neural LMs, and how it's evaluated.
- Concept: What a language model predicts — next-token probability — and why that's such a powerful primitive
- Concept: N-gram language models and the sparsity problem that limits them
- Concept: Neural language models — RNN-based, then Transformer-based
- Concept: Perplexity — how language models are evaluated
- Pitfall: Comparing perplexity across models with different tokenizers or vocabularies
- Concept: From language modeling to few-shot generalization — why scale changed everything (cross-link llms/llm-architecture-scaling)
- Interview: "Define a language model in one sentence you'd actually say in an interview" ⭐

---

## Group: Computer Vision (computer-vision)
*Tier: 🟡 Breadth · Scope: detection/segmentation basics*

### Topic: Image Classification Pipeline (image-classification-pipeline, beginner)
The end-to-end image classification pipeline, and why transfer learning is almost always the right start.
- Concept: The image classification pipeline — preprocessing, CNN backbone, softmax output
- Concept: Data augmentation for images — crop, flip, color jitter — and why it matters more here than elsewhere
- Concept: Transfer learning — fine-tuning an ImageNet-pretrained backbone
- Compare: Training from scratch vs transfer learning — the data/compute trade-off
- Concept: Common backbones at a glance (ResNet, EfficientNet) and how to choose one
- Pitfall: Fine-tuning with too high a learning rate destroys the pretrained features
- Interview: "You have 500 labeled images — how do you get a good classifier?" ⭐

### Topic: Object Detection (object-detection, advanced)
Locating and classifying multiple objects per image — two-stage vs one-stage detectors.
- Concept: Detection as classification plus localization — bounding boxes
- Concept: Anchor boxes — proposing candidate regions
- Concept: Two-stage detectors (the R-CNN family) — propose, then classify
- Concept: One-stage detectors (YOLO/SSD) — predicting boxes and classes in a single pass
- Compare: Two-stage vs one-stage detectors — accuracy vs speed
- Concept: Non-Max Suppression — cleaning up overlapping box predictions
- Concept: IoU (Intersection over Union) as the localization metric
- Concept: mAP — the standard detection evaluation metric
- Interview: "YOLO vs Faster R-CNN — which do you pick for a real-time app?" ⭐

### Topic: Image Segmentation (image-segmentation, advanced)
Per-pixel understanding of an image — semantic, instance, and panoptic segmentation.
- Concept: Segmentation as per-pixel classification
- Compare: Semantic vs instance vs panoptic segmentation — what each one distinguishes
- Concept: Encoder-decoder architectures for segmentation (U-Net) and its skip connections
- Diagram: U-Net's contracting and expanding paths
- Concept: Mask R-CNN — extending detection to per-instance masks
- Concept: Evaluating segmentation with pixel-wise IoU and the Dice coefficient
- Interview: "Semantic vs instance segmentation — give a real product example of each" ⭐

### Topic: Vision Beyond CNNs (vision-beyond-cnns, advanced)
Vision Transformers and the self-supervised/multimodal frontier beyond convolutional networks.
- Concept: Vision Transformer (ViT) — treating image patches as tokens
- Compare: CNN inductive bias vs ViT's data-hungry flexibility
- Pitfall: Fine-tuning a ViT on a small dataset from scratch underperforms a CNN
- Concept: Self-supervised pretraining for vision — the idea behind contrastive learning
- Concept: Multimodal models bridging vision and language via shared image-text embeddings (cross-link llms/diffusion-models-generative-ai)
- Interview: "Why do Vision Transformers need more data than CNNs to shine?" ⭐

---

## Group: LLMs & Generative AI (llms)
*Tier: 🔵 Rec · Scope: architecture, prompting, RAG, fine-tuning*

### Topic: LLM Architecture & Scaling (llm-architecture-scaling, advanced)
The decoder-only architecture behind GPT-style models, and how scale predictably changes capability.
- Concept: Decoder-only autoregressive architecture, GPT-style (cross-link nlp/attention-transformer-architecture for the attention mechanics)
- Concept: The pretraining objective — next-token prediction at massive scale
- Concept: Tokenization for LLMs (BPE) — why vocabulary design matters
- Concept: Scaling laws — how loss improves predictably with data, parameters, and compute
- Concept: Context window and KV caching — why longer context is expensive
- Concept: Emergent abilities — capabilities that only appear past a scale threshold
- Pitfall: Assuming bigger is always better for your specific task and cost budget
- Interview: "What actually happens when an LLM 'generates' the next word?" ⭐

### Topic: Decoding & Sampling Strategies (decoding-sampling-strategies, intermediate)
How text is actually sampled from a trained LLM, and why that choice matters as much as the model itself.
- Concept: Greedy decoding and its failure modes — repetition, blandness
- Concept: Temperature — controlling the randomness of sampling
- Concept: Top-k and top-p (nucleus) sampling
- Concept: Repetition, frequency, and presence penalties as practical knobs
- Concept: Beam search, and why it's used less for open-ended generation
- Compare: Choosing a decoding strategy by task — factual QA vs creative writing
- Interview: "Why doesn't temperature=0 guarantee the same output across two calls?" ⭐

### Topic: Prompting Techniques (prompting-techniques, intermediate)
Getting reliable behavior out of an LLM through prompt design alone, before touching weights.
- Concept: Zero-shot vs few-shot prompting
- Concept: Chain-of-thought prompting — why "think step by step" improves reasoning
- Concept: Structured-output prompting — JSON mode and function-calling schemas
- Concept: System prompts vs user prompts — the roles and their effect on behavior
- Concept: Prompt injection as a failure mode (cross-link appsec in Security area)
- Pitfall: Over-stuffing a prompt with instructions that quietly contradict each other
- Compare: Prompting vs fine-tuning — when prompting alone is genuinely enough
- Code: A function-calling / structured-output API request, end to end
- Interview: "Your prompt works in testing but fails in production — how do you debug it?" ⭐

### Topic: Retrieval-Augmented Generation (retrieval-augmented-generation, advanced)
Grounding LLM output in real, retrievable facts — the architecture behind most production "chat with your data" systems.
- Concept: Why RAG exists — grounding generation in facts the model was never trained on
- Diagram: The RAG pipeline — query, retrieve, augment the prompt, generate
- Concept: Embeddings and vector search as the retrieval mechanism
- Concept: Chunking strategy — why chunk size and overlap change answer quality
- Concept: Re-ranking retrieved chunks before generation
- Compare: RAG vs fine-tuning — grounding via retrieval vs baking knowledge into the weights
- Pitfall: Irrelevant retrieved chunks silently degrading answer quality
- Concept: Evaluating a RAG system — retrieval recall plus answer faithfulness
- Code: A minimal RAG loop — embed the query, retrieve top-k, build the prompt, call the model
- Interview: "Design a RAG system over a company's internal documents" ⭐
- Interview: "Your RAG chatbot still hallucinates despite retrieval — what's wrong?" ⭐

### Topic: Fine-Tuning & PEFT (fine-tuning-peft, advanced)
Adapting a pretrained model's weights — full fine-tuning vs parameter-efficient methods like LoRA.
- Concept: Full fine-tuning — updating every weight, its cost, and when it's worth it
- Concept: Instruction tuning — turning a base model into a helpful assistant
- Concept: LoRA — low-rank adapters instead of updating the full weight matrices
- Diagram: LoRA's adapter matrices sitting alongside the frozen base weights
- Concept: Other PEFT methods at a glance — adapters, prefix tuning
- Compare: RAG vs fine-tuning vs prompting — a decision framework for all three
- Pitfall: Fine-tuning on too little data causes catastrophic forgetting
- Interview: "When would you fine-tune instead of just prompting a bigger model?" ⭐

### Topic: RLHF & Alignment (rlhf-alignment, advanced)
Why a raw pretrained model isn't "aligned," and how human feedback reshapes it into an assistant.
- Concept: Why raw pretrained models aren't helpful/harmless by default
- Concept: The RLHF pipeline — a reward model from human preferences, then policy optimization (cross-link reinforcement-learning/policy-gradient-methods)
- Concept: DPO (Direct Preference Optimization) as a simpler alternative to full RLHF
- Compare: RLHF vs DPO — a reward model and RL loop vs a single direct optimization step
- Concept: Alignment failure modes — reward hacking and sycophancy
- Interview: "In plain terms, what does RLHF actually change about a model?" ⭐

### Topic: LLM Limitations & Hallucination (llm-limitations-hallucination, intermediate)
Why LLMs confidently state falsehoods, and the practical mitigations used in production.
- Concept: Hallucination — why a next-token predictor states false things confidently
- Concept: Knowledge cutoff and staleness
- Concept: Reasoning limitations — arithmetic and multi-step logic, and why they slip
- Pitfall: Chain-of-thought text can be fluent yet unfaithful to what actually drove the answer
- Concept: Bias inherited from training data
- Concept: Mitigations in practice — RAG, tool use, and verification passes (cross-link applied-ai/evaluating-llm-systems)
- Interview: "How do you reduce hallucination in a production LLM feature?" ⭐

### Topic: Diffusion Models & Generative AI (diffusion-models-generative-ai, advanced)
The generative technique behind modern text-to-image systems — the other half of "Generative AI."
- Concept: Generative AI beyond text — the image/audio/video generation landscape at a glance
- Concept: The diffusion process — gradually adding noise, then learning to reverse it
- Diagram: Forward (noising) vs reverse (denoising) diffusion
- Concept: Sampling a diffusion model — iterative denoising from pure noise to an image
- Concept: Conditioning generation on text for text-to-image models (cross-link nlp/word-embeddings and llms/llm-architecture-scaling for the text encoder)
- Compare: Diffusion models vs GANs (cross-link deep-learning/autoencoders-generative-basics) — sample quality and diversity vs training stability vs speed
- Concept: Latent diffusion — running the process in a compressed latent space for efficiency
- Interview: "At a high level, how does a text-to-image model like Stable Diffusion work?" ⭐

---

## Group: Applied AI / AI Engineering (applied-ai)
*Tier: 🔵 Rec · Scope: building AI apps, agents, evals*

### Topic: LLM App Architecture (llm-app-architecture, intermediate)
The practical stack for shipping an LLM-powered feature, beyond a single API call.
- Concept: The typical LLM app stack — model API, orchestration layer, vector DB, application logic
- Concept: Chains/pipelines — composing multiple LLM calls into one workflow
- Concept: Structured output and function calling as the integration seam with the rest of the app
- Concept: Streaming responses — why, and how it changes perceived latency
- Concept: Caching LLM responses — semantic cache vs exact-match cache
- Pitfall: Chaining too many LLM calls compounds both latency and error rate
- Interview: "Design the architecture for an AI customer-support assistant" ⭐

### Topic: AI Agents (ai-agents, advanced)
LLMs that plan, call tools, and act autonomously — the agent loop and its failure modes.
- Concept: What makes something an "agent" — an LLM that plans, acts via tools, observes, and repeats
- Diagram: The agent loop — think, act, observe
- Concept: Tool/function calling — how an LLM invokes an external capability
- Concept: The ReAct pattern — interleaving reasoning and acting
- Concept: Planning strategies — single-shot plans vs iterative replanning
- Concept: Memory in agents — short-term context vs long-term retrieval
- Concept: Multi-agent systems — when specialized agents beat one generalist
- Pitfall: Unbounded agent loops — runaway tool-calling and runaway cost
- Compare: A simple prompt-chain vs a full autonomous agent — when the added complexity is worth it
- Code: A tool-calling loop — the model requests a tool, you execute it, you feed the result back
- Interview: "Design an agent that books a flight within a user's constraints" ⭐
- Interview: "Your agent gets stuck in a tool-calling loop — how do you prevent that?" ⭐

### Topic: Evaluating LLM Systems (evaluating-llm-systems, advanced)
Measuring whether a generative system is actually good — the hardest and most-asked "AI engineering" skill.
- Concept: Why evaluating generative output is harder than classification — there's no single ground truth
- Concept: Reference-based metrics (BLEU/ROUGE) and why they fall short for open-ended text
- Concept: LLM-as-judge — using a model to score another model's output
- Pitfall: LLM-judge bias — favoring longer or more confident-sounding answers
- Concept: Building a golden test set from real user queries and real failures
- Concept: Online evals — A/B testing, thumbs up/down, and implicit signals
- Compare: Offline eval suites vs online production monitoring — what each one catches
- Interview: "How do you know your new prompt is actually better than the old one?" ⭐

### Topic: Guardrails & Production Safety (guardrails-safety-production, intermediate)
Keeping an LLM feature safe and auditable once real users can type anything into it.
- Concept: Input guardrails — detecting prompt injection and jailbreak attempts
- Concept: Output guardrails — content filtering, PII redaction, schema validation
- Concept: Human-in-the-loop patterns for high-stakes actions
- Concept: Rate limiting and abuse prevention for AI APIs (cross-link resilience in System Design area)
- Concept: Logging and audit trails — reconstructing "why did the agent do that"
- Pitfall: Relying on the system prompt alone as a security boundary
- Interview: "A user tries to jailbreak your support bot into leaking its system prompt — how do you defend against it?" ⭐

### Topic: Cost & Latency Optimization (cost-latency-optimization, intermediate)
The real-world engineering trade-offs that separate a demo from a production AI feature.
- Concept: The token-cost model — why prompt design is also a cost decision
- Concept: Model routing — a cheap model for easy cases, an expensive one for hard cases
- Concept: Caching and batching to cut redundant calls
- Concept: Quantization and distillation at a glance — smaller models for cheaper serving (cross-link mlops/model-serving-patterns)
- Concept: Streaming and partial responses to cut perceived latency even when total cost is unchanged
- Compare: Latency-sensitive (chat) vs throughput-sensitive (batch) workloads — different optimizations for each
- Interview: "Your AI feature costs 10x the projection in production — what do you check first?" ⭐

---

## Group: MLOps (mlops)
*Tier: 🟡 Breadth · Scope: serving, monitoring, feature stores*

### Topic: Model Serving Patterns (model-serving-patterns, beginner)
Getting a trained model into production — the serving patterns and safe-rollout mechanics.
- Concept: Batch inference vs online (real-time) inference — genuinely different infrastructure
- Concept: Serving a model via a REST/gRPC endpoint — the basic pattern
- Concept: Containerizing models for reproducible deployment
- Concept: Shadow deployment and canary releases for models (cross-link cicd in Engineering Craft area)
- Concept: A/B testing a new model version safely
- Compare: Online serving vs batch scoring — matching the pattern to the product need
- Interview: "Design the serving path for a real-time fraud-scoring model" ⭐

### Topic: Model Monitoring & Drift (model-monitoring-drift, intermediate)
Catching a model quietly degrading in production, often before you even have new labels.
- Concept: Why models degrade silently in production — the world changes, the code doesn't
- Concept: Data drift vs concept drift — input-distribution shift vs input-output relationship shift
- Concept: Monitoring input feature distributions over time
- Concept: Monitoring prediction distributions and downstream business metrics
- Concept: Triggering retraining — scheduled vs drift-triggered
- Pitfall: Monitoring only accuracy, which needs labels that arrive late or never
- Interview: "You can't measure live accuracy in real time — how do you monitor the model anyway?" ⭐

### Topic: Feature Stores (feature-stores, intermediate)
The infrastructure piece that keeps training and serving features consistent.
- Concept: The problem feature stores solve — training/serving skew
- Diagram: An offline store (training) and online store (low-latency serving) fed from the same feature definitions
- Concept: Point-in-time correctness — avoiding future leakage when joining features to historical labels
- Concept: Feature versioning and reuse across teams and models
- Pitfall: Computing the same feature differently in the training pipeline vs the serving path
- Compare: A lightweight feature table vs a full feature-store platform — when the overhead is worth it
- Interview: "What is training-serving skew, and how do feature stores prevent it?" ⭐

### Topic: ML Pipelines & Versioning (ml-pipelines-versioning, intermediate)
Making a model's training run reproducible and safely automatable end to end.
- Concept: The ML pipeline as a DAG — ingest, features, train, validate, deploy
- Concept: Experiment tracking — logging parameters, metrics, and artifacts for every run
- Concept: Model registry — versioning and promoting models across environments
- Concept: Data versioning — why code, data, and config all need pinning to reproduce a model
- Concept: Automated retraining pipelines and their triggers
- Code: Logging a training run's params/metrics/artifacts with an experiment tracker in a few lines
- Interview: "How do you make a model's training run fully reproducible?" ⭐

---

## Group: Recommender Systems (recommender-systems)
*Tier: ⚪ Niche · Scope: collaborative/content filtering*

### Topic: Recommender Fundamentals (recommender-fundamentals, beginner)
Framing the recommendation problem and the cold-start challenge every approach has to deal with.
- Concept: The recommendation problem — predicting preference/engagement for a user-item pair
- Concept: Implicit vs explicit feedback — clicks/watch-time vs star ratings
- Concept: The cold-start problem — new users and new items
- Compare: Content-based vs collaborative filtering — what signal each one actually uses
- Pitfall: Assuming more data always fixes cold start — it doesn't fix a brand-new user with zero history
- Interview: "Implicit vs explicit feedback — which is more common in practice, and why?" ⭐

### Topic: Content-Based Filtering (content-based-filtering, beginner)
Recommending from item features and a user's own history, without needing other users' data.
- Concept: Representing items as feature vectors — genre, tags, text embeddings
- Concept: Recommending via similarity to a user's previously-liked items
- Concept: TF-IDF/embedding similarity as the content similarity function (cross-link nlp/word-embeddings)
- Pitfall: Content-based filtering over-narrows — the filter bubble, no serendipity
- Compare: Content-based vs collaborative filtering — solves new-item cold start but not new-user cold start
- Interview: "Why does pure content-based filtering lead to a filter bubble?" ⭐

### Topic: Collaborative Filtering & Matrix Factorization (collaborative-filtering-matrix-factorization, intermediate)
Learning from the crowd — the classic, still most-asked collaborative filtering technique.
- Concept: The user-item interaction matrix — the core data structure
- Concept: User-based vs item-based collaborative filtering — the neighborhood methods
- Concept: Matrix factorization — learning latent user and item vectors
- Diagram: Decomposing the interaction matrix into user and item factor matrices
- Concept: Implicit-feedback matrix factorization — weighting observed vs unobserved interactions
- Pitfall: The sparsity problem — most user-item pairs have no interaction at all
- Interview: "Explain matrix factorization for recommendations to a non-ML interviewer" ⭐

### Topic: Deep Learning Recommenders (deep-learning-recommenders, advanced)
Modern neural recommenders that scale collaborative filtering to huge catalogs.
- Concept: Neural collaborative filtering — replacing the dot product with a learned function
- Concept: Two-tower models — separately embedding users and items for scalable retrieval
- Concept: Sequence-aware recommenders — modeling a user's session/history (cross-link deep-learning/rnn-lstm-sequence-models)
- Compare: Two-tower retrieval vs matrix factorization — scaling to huge item catalogs
- Pitfall: Collaborative signals alone still don't solve cold start — hybrid approaches are needed
- Interview: "Why do two-tower models scale to hundreds of millions of items?" ⭐

### Topic: Ranking & Hybrid Recommenders (ranking-hybrid-recommenders, advanced)
The practical multi-stage pipeline most production recommenders actually run.
- Concept: The candidate-generation-then-ranking two-stage funnel
- Concept: Hybrid recommenders — combining content-based and collaborative signals
- Concept: Learning-to-rank for the final stage (cross-link ml-fundamentals/evaluation-metrics-regression-ranking for NDCG/MAP)
- Concept: Diversity and novelty — why pure relevance ranking hurts long-term engagement
- Concept: Evaluating recommenders offline (NDCG, precision@k) vs online (CTR, watch-time, A/B tests)
- Pitfall: Optimizing purely for click-through rate creates a clickbait feedback loop
- Interview: "Design the recommendation system for a video app's homepage" ⭐

---

## Group: Reinforcement Learning (reinforcement-learning)
*Tier: ⚪ Niche · Scope: MDPs, Q-learning, policy methods*

### Topic: RL Problem Formulation (rl-problem-formulation, beginner)
The vocabulary and formal structure every RL algorithm is built on.
- Concept: The RL loop — agent, environment, state, action, reward
- Concept: Markov Decision Processes — states, actions, transition probabilities, rewards
- Concept: The Markov property — why "the state" must capture everything that's relevant
- Concept: Policy, value function, and return (discounted future reward) — the core vocabulary
- Concept: Episodic vs continuing tasks — when there is, or isn't, a natural end
- Concept: Exploration vs exploitation — the fundamental RL dilemma
- Interview: "Explain the exploration-exploitation trade-off with a real example" ⭐

### Topic: Value-Based Methods (value-based-methods, intermediate)
Learning which actions are good — Q-learning and its deep-learning extension, DQN.
- Concept: Value functions — how good a state (V) or a state-action pair (Q) is
- Concept: The Bellman equation — expressing value recursively
- Concept: Q-learning — learning optimal Q-values off-policy from experience
- Concept: Epsilon-greedy — balancing exploration during learning
- Concept: Deep Q-Networks (DQN) — approximating Q with a neural net for large state spaces
- Pitfall: Instability from combining bootstrapping, function approximation, and off-policy data — and how experience replay/target networks fix it
- Interview: "How does DQN stabilize training compared to vanilla Q-learning?" ⭐

### Topic: Policy Gradient Methods (policy-gradient-methods, advanced)
Learning a policy directly instead of deriving it from value estimates, up through the industry-standard PPO.
- Concept: Why learn a policy directly instead of deriving it from Q-values
- Concept: The policy gradient idea — nudging action probabilities by their outcome
- Concept: REINFORCE — the basic policy gradient algorithm
- Concept: Actor-critic methods — reducing variance with a learned value baseline
- Concept: PPO (Proximal Policy Optimization) — clipping updates for stability, the industry-standard method (cross-link llms/rlhf-alignment)
- Compare: Value-based vs policy-based methods — discrete vs continuous action spaces, and stability
- Interview: "Why is PPO the go-to algorithm for RLHF?" ⭐

### Topic: RL Applications & Challenges (rl-applications-challenges, intermediate)
Why RL is hard to actually deploy, and where it genuinely earns its complexity in industry.
- Concept: Reward shaping — designing rewards that induce the behavior you actually intended
- Pitfall: Reward hacking — the agent finds an unintended shortcut to maximize reward
- Concept: Sample inefficiency — why RL needs far more interactions than supervised learning
- Concept: Simulation-to-real transfer — training in a simulator, deploying in the real world
- Compare: Model-based vs model-free RL — planning with a learned world model vs learning purely from experience
- Concept: Where RL is actually used in industry today — recommendations, ad bidding, RLHF, robotics/games
- Interview: "Why is RL rarely the first choice for a typical product ML problem?" ⭐

---

## Group: ML System Design (ml-system-design)
*Tier: 🔵 Rec · Scope: design a recommender/feed/fraud system*

### Topic: ML System Design Framework (ml-system-design-framework, intermediate)
The repeatable method for answering any ML system design question, before touching any specific case study.
- Concept: How an ML system design interview differs from a pure HLD interview — data and model, not just infrastructure
- Concept: The framework — clarify requirements, frame as an ML problem, data, features, model, evaluation, serving, monitoring
- Concept: Clarifying questions that actually matter — scale, latency budget, label availability, online vs batch
- Concept: Stating assumptions and trade-offs out loud — what interviewers are really scoring
- Concept: The offline/online metric split — proxy metrics vs the real business goal
- Pitfall: Diving straight into model architecture before clarifying the business objective and constraints
- Interview: "Walk me through how you'd structure any ML system design answer" ⭐

### Topic: Design a Feed Ranking System (design-a-feed-ranking-system, advanced)
The canonical "design a feed" case study, integrating ranking, freshness, and diversity into one answer.
- Concept: Framing the feed as a ranking problem — score and order candidate posts
- Diagram: The multi-stage pipeline — candidate generation, ranking, then re-ranking/business rules
- Concept: Feature sources — user, content, and interaction features feeding the ranker
- Concept: Choosing the training label — engagement proxies (click/like/watch-time) and their pitfalls
- Concept: Layering freshness and diversity constraints onto pure relevance ranking (cross-link recommender-systems/ranking-hybrid-recommenders)
- Concept: Serving at scale — precomputing candidates, caching, and the latency budget per stage
- Pitfall: Optimizing purely for engagement breeds outrage-bait and addictive feedback loops
- Interview: "Design the news feed ranking system for a social app" ⭐

### Topic: Design a Fraud Detection System (design-a-fraud-detection-system, advanced)
The canonical fraud case study, built on extreme class imbalance and delayed ground truth.
- Concept: Framing fraud detection as extreme-imbalance classification (cross-link supervised-learning/handling-imbalanced-data)
- Concept: Feature engineering for fraud — velocity features, graph/network features, device fingerprinting
- Concept: The real-time vs batch scoring split — blocking a transaction vs flagging it for review
- Concept: Label latency — fraud is often confirmed weeks later, which complicates training
- Concept: The precision/recall trade-off stated in business terms — false declines vs missed-fraud cost
- Concept: Adversarial adaptation — fraudsters change behavior in direct response to your model
- Interview: "Design a real-time fraud detection system for card transactions" ⭐

### Topic: Design a Search Ranking System (design-a-search-ranking-system, advanced)
A query-driven ranking case study, distinct from a feed's passive ranking.
- Concept: Framing search as retrieval plus ranking, not one single model
- Concept: Query understanding — spell correction, intent classification, query expansion
- Concept: Retrieval — inverted index/BM25 vs embedding-based semantic search (cross-link llms/retrieval-augmented-generation)
- Concept: Learning-to-rank for the final result ordering
- Concept: Evaluating search quality — NDCG, human relevance judgments, click models
- Pitfall: Optimizing relevance purely offline without correcting for position bias in click data
- Interview: "Design the search ranking system for an e-commerce site" ⭐

### Topic: Design a Recommendation System End-to-End (design-a-recommendation-system-e2e, advanced)
The canonical "design a recommender" case study, integrating the Recommender Systems group end to end.
- Concept: End-to-end framing — this integrates the Recommender Systems group's algorithms into one interview answer
- Concept: Choosing a candidate-generation strategy at scale (cross-link recommender-systems/deep-learning-recommenders)
- Concept: The ranking stage — what features and labels feed it
- Concept: Cold-start handling in a full system — new users and new items
- Concept: Online experimentation — rolling out a new recommender safely with A/B tests and guardrail metrics
- Pitfall: Launching a new recommender without a holdout/guardrail group to catch regressions
- Interview: "Design a product recommendation system for an e-commerce homepage" ⭐

### Topic: ML Infra Trade-offs at Scale (ml-infra-tradeoffs-scale, intermediate)
The cross-cutting infrastructure trade-offs interviewers probe across every ML system design question.
- Concept: Online vs offline/batch inference, revisited at the full-system level
- Concept: Latency budgets across a multi-stage pipeline — retrieval and ranking under one shared SLA
- Concept: Scaling training data and compute — when to distribute training (cross-link mlops/ml-pipelines-versioning)
- Concept: Build vs buy — a hosted model API vs training your own
- Concept: Handling scale spikes and stale models gracefully — falling back to a simpler heuristic
- Concept: Multi-region considerations for serving models close to users (cross-link consistency-replication in System Design area)
- Interview: "Your ranking model's p99 latency blows the budget under peak load — what do you do?" ⭐

---

## Overlaps & gaps flagged for review

- **Transformer architecture lives in `nlp`, not `llms`.** Per the map's own scope split ("transformers" under `nlp`, "architecture" under `llms`), the deep dive on attention/self-attention/positional encoding sits in `nlp/attention-transformer-architecture`; `llms/llm-architecture-scaling` cross-links back rather than re-deriving it. Flag if reviewers expected transformer internals inside the LLM group instead.
- **Recommenders are deliberately split two ways.** `recommender-systems` teaches the algorithms (content-based, collaborative filtering, two-tower, ranking); `ml-system-design/design-a-recommendation-system-e2e` teaches the interview case study that integrates them. Same pattern for fraud (`supervised-learning/handling-imbalanced-data` + `unsupervised-learning/anomaly-detection` → `ml-system-design/design-a-fraud-detection-system`) and search/feed ranking. No content is duplicated, only cross-linked.
- **Gap closed:** the map's scope line for `llms` didn't mention image/diffusion generation, but the group is named "LLMs **& Generative AI**" — added `diffusion-models-generative-ai` so that half of the group's name is actually covered (Stable-Diffusion-style text-to-image). Flag if this is out of scope for a first pass.
- **No dedicated multimodal-LLM topic.** Touched only briefly as a cross-link in `computer-vision/vision-beyond-cnns`. If multimodal (image+text) generation is a priority, it likely deserves its own topic in `llms`.
- **RLHF mechanics live in `reinforcement-learning` (`policy-gradient-methods`, i.e. PPO), not duplicated in `llms/rlhf-alignment`,** which cross-links back and focuses on the alignment framing instead.
- **No overlap** with Area 16 (`probability-stats`, `linear-algebra`) or Area 5 (`gpus-accelerators`) — ML Fundamentals and Deep Learning apply math/hardware concepts in ML context but don't re-teach the underlying math or hardware.
