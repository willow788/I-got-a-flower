<div align="center">

# 🌸 I Got a Flower 🌸

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="MIT License">
<img src="https://img.shields.io/badge/Made%20with-Turtle%20Graphics-924CB4?style=for-the-badge" alt="Turtle Graphics">

### *A mesmerizing mathematical flower that blooms on your screen* 🌺✨

[Demo](#-demo) • [How It Works](#-how-it-works) • [Getting Started](#-getting-started) • [The Math](#-the-math-behind-the-beauty)

</div>

---

## 🎨 What is This?

Ever wondered what happens when math meets art? **I Got a Flower** creates a stunning purple flower using nothing but Python's turtle graphics and polar coordinates. Watch as mathematical equations come to life, drawing petals in a hypnotic animation!

## ✨ Demo

> *The flower draws itself using 2000 points calculated from polar equations*

The program creates a beautiful 7-petaled flower in vibrant purple (`#924CB4`) against a black canvas. Each line radiates from the center, creating an elegant mathematical rose pattern.

## 🚀 Getting Started

### Prerequisites

- Python 3.x (comes with turtle graphics built-in!)
- That's it! No external dependencies needed 🎉

### Installation & Run

```bash
# Clone this repository
git clone https://github.com/willow788/I-got-a-flower.git

# Navigate to the directory
cd I-got-a-flower

# Run the program
python flower.py
```

Sit back and watch your flower bloom! 🌷

## 🔬 The Math Behind the Beauty

This isn't just pretty pixels—it's **mathematics in motion**! 

### The Polar Equation

```python
r(θ) = 300 × sin(7θ)
```

Where:
- **r** = radius (distance from center)
- **θ** (theta) = angle
- **k = 7** = number of petals

### From Polar to Cartesian

The program converts polar coordinates to Cartesian (x, y) coordinates:

```python
x = r × cos(θ)
y = r × sin(θ)
```

*Yes, this is the same circular motion physics from Class 11—but now it's actually beautiful!* 😄

## 🎯 Features

- ⚡ **Fast Animation** - Set to maximum speed for instant gratification
- 🎨 **Customizable Colors** - Change the flower color by modifying the hex code
- 🔢 **Adjustable Petals** - Modify the `k` parameter to create flowers with different petal counts
- 🖤 **Elegant Contrast** - Black background makes the purple petals pop

## 🎨 Customization Ideas

Want to make it your own? Try these tweaks:

```python
# Change the color
color("#FF69B4")  # Hot pink flower

# More petals
def r(theta, k=11):  # 11-petaled flower

# Different size
return 500 * math.sin(k * theta)  # Bigger flower

# Change background
bgcolor("midnight blue")  # Night garden vibes
```

## 📚 What You'll Learn

- 🐢 Turtle graphics in Python
- 📐 Polar coordinate systems
- 🔄 Converting between polar and Cartesian coordinates
- 🎬 Creating animated drawings with code
- ✏️ Mathematical art and parametric equations

## 🤝 Contributing

Found a way to make the flower even more beautiful?  Contributions are welcome! 

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFlower`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFlower`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💭 Acknowledgments

- Inspired by the beauty of mathematical art
- Built with Python's beloved turtle graphics module
- A tribute to everyone who survived Class 11 physics 🎓

---

<div align="center">

**Made with 💜 and a lot of math**

*If you like this project, give it a ⭐! *

</div>
