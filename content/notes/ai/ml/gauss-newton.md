---
title: "Gauss-Newton Optimization"
date: 2024-12-19
draft: false
tags: ["optimization", "machine learning", "deep learning", "LLM", "second-order methods", "Gauss-Newton", "K-FAC", "Shampoo"]
categories: ["Machine Learning", "Optimization"]
description: "Gauss-Newton and second-order methods for deep learning"
math: true
---

# Gauss-Newton Optimization for Deep Neural Networks and LLM Training

This document provides a brief technical overview of modern optimization techniques for large-scale deep learning. It starts with classical optimization foundations, moves through advanced **second-order methods**, and ends with practical **curvature approximations** that make these techniques feasible for billion-parameter models.

**What you'll learn:**
- How classical optimization methods scale (or don't) to modern deep learning
- The mathematical foundation of second-order optimization
- Practical approximations like **K-FAC**, **Shampoo**, and **Rank-1 methods**
- When and why to use each optimization approach

<details>
<summary><strong>📋 Table of Contents</strong></summary>

1. [Classical Optimization Foundations](#1-classical-optimization-foundations)
   - [Problem Setup](#11-problem-setup)
   - [Gradient Descent](#12-gradient-descent)
   - [Newton's Method](#13-newtons-method)
2. [Gauss–Newton and Generalized Gauss–Newton](#2-gaussnewton-and-generalized-gaussnewton)
   - [Setup: Network Outputs and Loss](#21-setup-network-outputs-and-loss)
   - [Hessian Structure](#22-hessian-structure)
   - [Gauss–Newton (GN) Approximation](#23-gaussnewton-gn-approximation)
   - [Generalized Gauss–Newton (GGN)](#24-generalized-gaussnewton-ggn)
   - [Why Use GGN?](#25-why-use-ggn)
3. [Practical Challenge: Computing J and G](#3-practical-challenge-computing-j-and-g)
4. [Approximating GGN in Practice](#4-approximating-ggn-in-practice)
   - [Gradient Descent (First-Order Baseline)](#41-gradient-descent-first-order-baseline)
   - [Adam](#42-adam)
   - [K-FAC: Kronecker-Factored Approximate Curvature](#43-k-fac-kronecker-factored-approximate-curvature)
   - [Shampoo Optimizer](#44-shampoo-optimizer)
   - [Rank-1 Curvature Approximation](#45-rank-1-curvature-approximation)
5. [Summary of GGN Approximations](#5-summary-of-ggn-approximations)
6. [Intuitive Analogy: Mountain Navigation](#6-intuitive-analogy-mountain-navigation)
7. [Practical Guidance for Optimizer Selection](#7-practical-guidance-for-optimizer-selection)
8. [Key Takeaways](#8-key-takeaways)

</details>

---

## **1. Classical Optimization Foundations**

### **1.1 Problem Setup**

The foundation of all optimization in deep learning is the **empirical risk minimization** problem. We consider the general problem of minimizing an objective function:
$$
L(\theta) = \mathbb{E}_{(x,y)\sim \mathcal{D}}[\ell(f(x; \theta), y)]
$$

**Notation:**
- $\theta \in \mathbb{R}^n$: model parameters (weights and biases)
- $f(x; \theta)$: the neural network model that maps inputs to outputs
- $\ell(\cdot, y)$: per-sample loss function (e.g., cross-entropy, MSE)
- $\mathcal{D}$: the data distribution from which we sample training examples

This formulation captures the essence of supervised learning: we want to find parameters that minimize the expected loss over our data distribution.

The optimization goal is to find:
$$
\theta^* = \arg\min_\theta L(\theta)
$$

---

### **1.2 Gradient Descent**

**Gradient descent** is the foundational first-order optimization method that powers most of deep learning. The core idea is simple: move in the direction opposite to the gradient to reduce the loss.
$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta L(\theta_t)
$$
**Parameters:**
- $\eta$: learning rate (step size)
- $\nabla_\theta L(\theta)$: gradient of the loss with respect to parameters

**Advantages:**
- **Computationally efficient**: $O(n)$ cost per iteration
- **Memory efficient**: only requires storing gradients
- **Scales well**: works for models with millions or billions of parameters
- **Simple to implement**: straightforward backpropagation

**Limitations:**
- **Ignores curvature**: treats all parameter directions equally
- **Sensitive to conditioning**: slow convergence when the loss landscape is ill-conditioned
- **Requires careful tuning**: learning rate significantly affects convergence

---

### **1.3 Newton's Method**

The limitations of gradient descent motivate the use of **second-order methods** that incorporate curvature information. **Newton's method** uses the Hessian matrix to adapt step sizes for each parameter direction.
$$
H(\theta) = \nabla^2_\theta L(\theta)
$$

The **Newton update**:
$$
\theta_{t+1} = \theta_t - H(\theta_t)^{-1} \nabla_\theta L(\theta_t)
$$

**Advantages:**
- **Adaptive step sizes**: automatically adjusts learning rate for each parameter direction
- **Quadratic convergence**: converges in fewer iterations, especially near optima
- **Theoretically optimal**: provides the best local step direction

**Critical Limitations for Deep Learning:**
- **Computational intractability**: 
  - Hessian size: $n \times n$ → trillions of entries for LLMs (e.g., 175B parameters)
  - Matrix inversion cost: $O(n^3)$ → computationally prohibitive
- **Memory requirements**: storing the full Hessian requires $O(n^2)$ memory
- **Numerical instability**: Hessian may be singular or indefinite

This motivates the need for **practical approximations** that capture the benefits of second-order information while remaining computationally feasible.

---

## **2. Gauss–Newton and Generalized Gauss–Newton**

The **Gauss–Newton (GN)** method provides a practical alternative to full Newton's method by exploiting the structure of specific loss functions. This approach leads to the **Generalized Gauss–Newton (GGN)** method, which forms the foundation for modern second-order optimization in deep learning.

---

### **2.1 Setup: Network Outputs and Loss**

To understand the Gauss–Newton approach, we need to examine how neural networks process data:

**Key Components:**
- $z = f(x; \theta)$: network output (e.g., logits, embeddings)
- $\ell(z, y)$: per-example loss function
- $L(\theta)$: total empirical loss

The total loss over a batch of $N$ examples:
$$
L(\theta) = \frac{1}{N} \sum_{i=1}^N \ell(z_i, y_i)
$$

---

### **2.2 Hessian Structure**

The key insight of Gauss–Newton methods comes from analyzing the structure of the Hessian matrix. When we differentiate the loss with respect to parameters, the exact Hessian has a specific decomposition:
$$
H = J^T H_\ell J + \sum_{i} \left[\sum_k r_{i,k} \nabla^2_\theta z_{i,k}\right]
$$

**Term Analysis:**
- $J = \frac{\partial z}{\partial \theta}$: **Jacobian matrix** of network outputs with respect to parameters
- $H_\ell = \nabla^2_z \ell(z, y)$: **Hessian of the loss** with respect to network outputs
- $r_i = z_i - y_i$: **residuals** (prediction errors)

**Physical Interpretation:**
- **First term** ($J^T H_\ell J$): captures how sensitive the loss is to parameter changes through the network outputs
- **Second term**: depends on the second derivatives of the network architecture itself

**Key Insight:** The second term is computationally expensive and often noisy for deep networks. The Gauss–Newton approximation **drops this term**, focusing only on the first term which captures the essential curvature information.

---

### **2.3 Gauss–Newton (GN) Approximation**

The classical Gauss–Newton method applies specifically to **least squares regression**. For this loss function:
$$
\ell(z, y) = \frac{1}{2}\|z - y\|^2
$$
we have $H_\ell = I$ (the identity matrix).

**Gauss–Newton Approximation:** By dropping the expensive second term, the Hessian simplifies to:
$$
G = J^T J
$$

This is the **Gauss–Newton matrix** — a positive semi-definite approximation of the full Hessian $H$. This approximation is:
- **Always positive semi-definite** (unlike the full Hessian)
- **Much cheaper to compute** (no second derivatives of the network)
- **Theoretically justified** for least squares problems

---

### **2.4 Generalized Gauss–Newton (GGN)**

Most modern deep learning applications use **non-quadratic losses** like cross-entropy, not least squares. The **Generalized Gauss–Newton (GGN)** method extends the classical approach by preserving the loss curvature information:
$$
\boxed{G = J^T H_\ell J}
$$

**Component Roles:**
- $J$: encodes **model sensitivity** (how outputs change with parameters)
- $H_\ell$: encodes **loss curvature** (how the loss changes with outputs)

This decomposition allows us to understand optimization from two perspectives: the network's sensitivity to parameter changes and the loss function's curvature properties.

---

### **2.5 Why Use GGN?**

The GGN approximation offers several key advantages over the full Hessian for deep learning applications:

| Property              | Full Hessian $H$          | GGN $G$ |
|-----------------------|-----------------------------|-----------|
| **Positive semi-definite** |  No (can be indefinite)     |  Yes (stable updates) |
| **Computational complexity** | Very high                    | Lower (no second derivatives of network) |
| **Practical feasibility** | Hard to compute              |  Practical with approximations |
| **Theoretical foundation** | General but unstable         | Well-founded for many losses |

**Key Benefits:**
- **Numerical stability**: GGN ignores unstable negative curvature that can cause optimization to diverge
- **Theoretical connection**: For cross-entropy loss, GGN is equivalent to the **Fisher Information Matrix**, providing a principled foundation
- **Practical efficiency**: Avoids computing expensive second derivatives of the network architecture

---

## **3. Practical Challenge: Computing $J$ and $G$**

While GGN provides a theoretically sound approximation, we face a **massive computational challenge** when applying it to modern deep learning:

**Scale Problem:**
- $n = $  # parameters: billions of parameters (e.g., 175B for GPT-3)
- $J$ shape: $(m \times n)$ → impossible to store explicitly
- $G$ shape: $(n \times n)$ → trillions of entries

**Solution:** Use **Jacobian-vector products (JVPs)** instead of materializing full matrices.

**JVP Operations:**
| Operation | Interpretation | Efficient Computation |
|------------|----------------|-----------------------|
| $Jv$     | Effect of parameter perturbation on outputs | Forward-mode autodiff |
| $J^T v$  | Effect of output perturbation on parameters | Reverse-mode autodiff (backprop) |

**Key Insight:** We never explicitly materialize $J$ or $G$, only products like $Gv = J^T(H_\ell(Jv))$. This allows us to compute GGN-vector products efficiently using standard autodiff tools.

---

## **4. Approximating GGN in Practice**

Even with efficient JVPs, the GGN matrix $G$ is still too large to store or invert directly. We need **structured approximations** that capture the essential curvature information while remaining computationally tractable.

**Approach:** Instead of computing $G^{-1}$ exactly, we design approximations that can be efficiently applied to gradients.

---

### **4.1 Gradient Descent (First-Order Baseline)**

As our baseline, consider standard first-order gradient descent:
$$
\Delta \theta = -\eta \nabla_\theta L
$$

**Characteristics:**
- **Cost**: $O(n)$ per iteration
- **Memory**: $O(n)$ (just gradients)
- **Limitation**: Ignores curvature completely, leading to inefficient updates in ill-conditioned optimization landscapes

This motivates the need for curvature-aware methods that can adapt step sizes based on the local geometry.

---

### **4.2 Adam**

**Adam** approximates curvature **diagonally** by tracking first and second moments of gradients:

$$
\theta_{t+1} = \theta_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

This provides adaptive learning rates per parameter while maintaining $O(n)$ computational cost.

---

### **4.3 K-FAC: Kronecker-Factored Approximate Curvature**

**K-FAC** (Kronecker-Factored Approximate Curvature) represents a major breakthrough in making second-order optimization practical for deep networks. It provides a structured **layer-wise approximation** to the GGN matrix.

**Setup:** Consider a fully connected layer with forward pass:
$$
z = W a + b
$$
**Key Components:**
- $a$: input activations to the layer
- $\delta = \partial L / \partial z$: backpropagated error signals
- $W$: weight matrix

**Gradient Computation:**
$$
\nabla_W L = \delta a^T
$$

**Vectorized Form:**
$$
\mathrm{vec}(\nabla_W L) = a \otimes \delta
$$

**K-FAC Key Insight:** The GGN matrix for this layer can be approximated as a Kronecker product:
$$
G = \mathbb{E}[a a^T] \otimes \mathbb{E}[\delta \delta^T] = A \otimes S
$$

**Covariance Matrices:**
- $A = \mathbb{E}[a a^T]$: **activation covariance** (input statistics)
- $S = \mathbb{E}[\delta \delta^T]$: **gradient covariance** (output error statistics)

This factorization dramatically reduces the computational complexity while preserving the essential curvature structure.

---

#### **K-FAC Update Rule**

Using the Kronecker product property $(A \otimes S)^{-1} = A^{-1} \otimes S^{-1}$, the K-FAC update becomes:

$$
\boxed{\Delta W = -\eta S^{-1} (\nabla_W L) A^{-1}}
$$

**Geometric Interpretation:**
- **Left multiplication** by $S^{-1}$: whitens the output gradients (normalizes error signal variance)
- **Right multiplication** by $A^{-1}$: whitens the input activations (normalizes input signal variance)

**Connection to Natural Gradients:** This update approximates a **natural gradient update** for each layer, which respects the geometry of the parameter space and provides more effective optimization directions.

---

#### **Computational Complexity Analysis**

The power of K-FAC lies in its dramatic complexity reduction:

| Method   | Memory per Layer | Update Cost | Curvature Quality |
|----------|------------------|-------------|-------------------|
| **Full GGN** | $O((d_{in} d_{out})^2)$ | $O((d_{in} d_{out})^3)$ | Exact |
| **Adam**     | $O(d_{in} d_{out})$ | $O(d_{in} d_{out})$ | Diagonal only |
| **K-FAC**    | $O(d_{in}^2 + d_{out}^2)$ | $O(d_{in}^3 + d_{out}^3)$ | Block-structured |

**Key Benefits:**
- **Orders of magnitude cheaper** than full GGN while maintaining rich curvature structure
- **Much richer than Adam** by capturing cross-parameter interactions within each layer
- **Practical for large models** where full GGN is computationally prohibitive

---

### **4.4 Shampoo Optimizer**

**Shampoo** represents the next evolution beyond K-FAC, generalizing the Kronecker factorization to **multi-dimensional tensors**. While K-FAC factors the curvature into just two dimensions (input and output), Shampoo can handle arbitrary tensor shapes.

**Setup:** For a weight tensor $W$ with shape $(d_1, d_2, ..., d_k)$, Shampoo maintains one factor per dimension:
$$
G \approx G_1 \otimes G_2 \otimes \dots \otimes G_k
$$

---

#### **Shampoo Update Algorithm**

The Shampoo update follows a systematic procedure:

1. **Estimate per-dimension covariances**: Compute $G_i$ for each tensor dimension
2. **Apply damping**: $\tilde{G}_i = G_i + \lambda I$ (regularization for numerical stability)
3. **Compute inverse square roots**: $\tilde{G}_i^{-1/2}$ (efficient matrix operations)
4. **Apply preconditioning**: 
   $$
   \Delta W = -\eta \left(\bigotimes_{i=1}^k \tilde{G}_i^{-1/2}\right) \nabla_W L
   $$

**Key Insight:** The Kronecker product of inverse square roots provides an efficient way to apply the full preconditioning without materializing the complete matrix.

---

#### **Shampoo vs K-FAC Trade-offs**

| Feature           | K-FAC       | Shampoo |
|-------------------|-------------|---------|
| **Dimensions modeled** | 2 (input/output) | All tensor dimensions |
| **Curvature fidelity** | Moderate    | High |
| **Memory cost**       | Lower       | Higher |
| **Computational cost** | Lower       | Higher |
| **Applicability**     | FC layers   | All tensor operations |

**Production Usage:** Shampoo is used at Google for training very large models (e.g., PaLM), where higher fidelity curvature information helps reduce total training steps and improve final performance.

---

### **4.5 Rank-1 Curvature Approximation**

For **extremely large models** (e.g., >1T parameters), even K-FAC or Shampoo may be computationally prohibitive. **Rank-1 methods** provide an ultra-lightweight alternative.

**Core Idea:** Approximate the full curvature matrix with a single outer product:
$$
G_t \approx v_t v_t^T
$$
Where $v_t$ is typically the current gradient or a random projection.

**Moving Average Update:**  to preserve stability
$$
\hat{G}_t = \beta \hat{G}_{t-1} + (1-\beta) v_t v_t^T
$$

**Characteristics:**
- **Memory cost**: $O(n)$ (same as Adam)
- **Compute cost**: $O(n)$ (extremely cheap)
- **Scalability**: Works for models of any size
- **Curvature quality**: Extremely coarse approximation

**Use Cases:** Primarily used in **fine-tuning scenarios** where computational efficiency is paramount, such as:
- **LoRA adapter training**
- **Parameter-efficient fine-tuning**
- **Resource-constrained environments**

---

## **5. Summary of GGN Approximations**

Here's a comprehensive comparison of the optimization methods we've discussed:

| Method    | Curvature Approximation | Cost | Accuracy | LLM Use Case |
|-----------|--------------------------|------|----------|--------------|
| **Adam**     | Diagonal (per-parameter) | Low  | Low      | General training  |
| **Rank-1**    | Single vector outer product | Low  | Very low | Fine-tuning  |
| **K-FAC**     | 2D Kronecker factors | Medium | Medium | Fine-tuning, RL |
| **Shampoo**   | Multi-dim factorization | High | High | Research-scale |

---

## **6. Intuitive Analogy: Mountain Navigation**

Imagine you're navigating through a complex mountain landscape to reach the lowest valley (optimal solution):

| Optimizer | Navigation Tool | Description |
|------------|-----------------|-------------|
| **AdamW**      | **Compass only** | Knows direction but ignores terrain steepness and obstacles |
| **Rank-1**     | **Single slope measurement** | Minimal terrain info, very cheap to use |
| **K-FAC**      | **2D topographic map per region** | Detailed local maps, simplified but highly useful |
| **Shampoo**    | **Full 3D topographic map** | Complete terrain information, computationally expensive |
| **Full Newton** | **GPS with full terrain data** | Perfect information but impossible to compute in real-time |

This analogy helps understand the **curvature fidelity vs. computational cost** trade-off inherent in optimization method selection.

---

## **7. Practical Guidance for Optimizer Selection**

When choosing an optimization method for your specific use case, consider the following recommendations:

| Scenario                   | Recommended Optimizer | Rationale |
|----------------------------|-----------------------|-----------|
| **General training**            | Adam | Proven stability, computational efficiency, widely used |
| **Fine-tuning adapters (LoRA)** | Rank-1 or Adam | Ultra-efficient for parameter-efficient methods |
| **Reinforcement learning**      | K-FAC | Natural gradients help with policy optimization |
| **Advanced research**           | Shampoo or hybrid approaches | Maximum curvature fidelity for cutting-edge work |
| **Resource-constrained**        | Adam or Rank-1 | Prioritize computational efficiency |
| **Convergence-critical**        | Shampoo or K-FAC | Higher curvature fidelity for difficult optimization landscapes |

---

## **8. Key Takeaways**


1. **The GGN Framework**: The Generalized Gauss–Newton method provides a stable, positive semi-definite curvature approximation that's theoretically sound and practically feasible for deep networks.

2. **Adam's Role**: Adam remains widely used due to its proven stability, computational efficiency, and robust performance across diverse architectures.

3. **K-FAC Innovation**: By factoring curvature into input and output covariances, K-FAC achieves near-natural gradient updates at dramatically reduced computational cost, making second-order methods practical for deep learning.

4. **Shampoo Advancement**: Shampoo generalizes K-FAC to handle arbitrary tensor dimensions, providing higher curvature fidelity at increased computational cost, suitable for research-scale applications.

5. **Rank-1 Efficiency**: For extremely large models, rank-1 methods provide ultra-cheap curvature approximations that maintain some second-order benefits while scaling to trillion-parameter models.

6. **Fundamental Trade-off**: The choice of optimization method fundamentally depends on balancing **curvature fidelity** against **computational scalability**, with no single method optimal for all scenarios.

**The Future**: As models continue to grow in size and complexity, the development of efficient second-order methods will become increasingly critical for achieving optimal training performance.

---
