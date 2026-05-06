import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from errors import TrezRuntimeError


def _plt():
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        return plt
    except ImportError:
        raise TrezRuntimeError("Plotdoz: matplotlib no instalado. Ejecuta: pip install matplotlib")


def learning_curve(train_losses, val_losses=None, title="Learning Curve",
                   xlabel="Epoch", ylabel="Loss", output_file="learning_curve.png"):
    """Curva de aprendizaje: train loss y opcionalmente val loss por época."""
    plt = _plt()
    epochs = list(range(1, len(train_losses) + 1))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(epochs, [float(v) for v in train_losses], label="Train", color="steelblue", linewidth=2)
    if val_losses:
        ax.plot(epochs, [float(v) for v in val_losses], label="Val", color="tomato",
                linewidth=2, linestyle="--")
        ax.legend()
    ax.set_title(str(title))
    ax.set_xlabel(str(xlabel))
    ax.set_ylabel(str(ylabel))
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(str(output_file))
    plt.close(fig)
    print(f"[Plotdoz] learning_curve guardado en: {output_file}")
    return str(output_file)


def histogram(values, title="Histograma", xlabel="Valor", ylabel="Frecuencia",
              bins=20, output_file="histograma.png"):
    """Histograma de una lista de valores numéricos."""
    plt = _plt()
    numeric = []
    for v in values:
        try:
            numeric.append(float(v))
        except (TypeError, ValueError):
            pass
    if not numeric:
        raise TrezRuntimeError("Plotdoz.histogram(): no hay valores numéricos para graficar.")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(numeric, bins=int(bins), color="steelblue", edgecolor="black")
    ax.set_title(str(title))
    ax.set_xlabel(str(xlabel))
    ax.set_ylabel(str(ylabel))
    plt.tight_layout()
    plt.savefig(str(output_file))
    plt.close(fig)
    print(f"[Plotdoz] histogram guardado en: {output_file}")
    return str(output_file)


def bar_chart(labels, values, title="Barras", xlabel="X", ylabel="Y",
              output_file="barras.png"):
    """Gráfico de barras."""
    plt = _plt()
    if len(labels) != len(values):
        raise TrezRuntimeError("Plotdoz.bar_chart(): labels y values deben tener el mismo tamaño.")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar([str(l) for l in labels], [float(v) for v in values],
           color="steelblue", edgecolor="black")
    ax.set_title(str(title))
    ax.set_xlabel(str(xlabel))
    ax.set_ylabel(str(ylabel))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(str(output_file))
    plt.close(fig)
    print(f"[Plotdoz] bar_chart guardado en: {output_file}")
    return str(output_file)


def scatter(x_vals, y_vals, title="Scatter", xlabel="X", ylabel="Y",
            color="steelblue", output_file="scatter.png"):
    """Scatter plot."""
    plt = _plt()
    if len(x_vals) != len(y_vals):
        raise TrezRuntimeError("Plotdoz.scatter(): x_vals y y_vals deben tener el mismo tamaño.")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter([float(v) for v in x_vals], [float(v) for v in y_vals],
               alpha=0.5, color=str(color), edgecolors="none", s=20)
    ax.set_title(str(title))
    ax.set_xlabel(str(xlabel))
    ax.set_ylabel(str(ylabel))
    plt.tight_layout()
    plt.savefig(str(output_file))
    plt.close(fig)
    print(f"[Plotdoz] scatter guardado en: {output_file}")
    return str(output_file)


def line_chart(x_vals, y_vals, title="Linea", xlabel="X", ylabel="Y",
               output_file="linea.png"):
    """Gráfico de línea."""
    plt = _plt()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([float(v) for v in x_vals], [float(v) for v in y_vals],
            color="steelblue", linewidth=1.5)
    ax.set_title(str(title))
    ax.set_xlabel(str(xlabel))
    ax.set_ylabel(str(ylabel))
    plt.tight_layout()
    plt.savefig(str(output_file))
    plt.close(fig)
    print(f"[Plotdoz] line_chart guardado en: {output_file}")
    return str(output_file)
