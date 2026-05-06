"""
run_tests.py — Runner de pruebas para TREZ.

Ejecuta cada archivo .trez en tests/features/ y compara su salida
contra el archivo .expected correspondiente (línea a línea).

Uso:
    python3 tests/run_tests.py
    python3 tests/run_tests.py --update   # regenera los .expected

Salida:
    PASS  test_basic          (8 líneas)
    FAIL  test_math           línea 3: '3.14' != '3.141592653589793'
    ...
    Resultado: 10/10 pasaron
"""

import sys
import os
import subprocess

SRC_DIR      = os.path.join(os.path.dirname(__file__), '..', 'src')
FEATURES_DIR = os.path.join(os.path.dirname(__file__), 'features')
UPDATE_MODE  = '--update' in sys.argv


def run_trez(trez_file):
    """Ejecuta un archivo .trez y retorna (stdout, stderr, returncode)."""
    result = subprocess.run(
        [sys.executable, 'main.py', trez_file],
        cwd=SRC_DIR,
        capture_output=True,
        text=True,
        timeout=60,
    )
    return result.stdout.rstrip('\n'), result.stderr.rstrip('\n'), result.returncode


def compare(name, actual_lines, expected_lines):
    """Compara línea a línea. Retorna lista de diferencias."""
    diffs = []
    max_lines = max(len(actual_lines), len(expected_lines))
    for i in range(max_lines):
        act = actual_lines[i] if i < len(actual_lines) else '<ausente>'
        exp = expected_lines[i] if i < len(expected_lines) else '<ausente>'
        if act.strip() != exp.strip():
            diffs.append(f"  línea {i+1}: obtenido {repr(act)} != esperado {repr(exp)}")
    return diffs


def main():
    trez_files = sorted(
        f for f in os.listdir(FEATURES_DIR)
        if f.endswith('.trez')
    )

    passed = 0
    failed = 0
    errors = 0

    print(f"\nTREZ Test Runner — {len(trez_files)} archivos\n{'─'*50}")

    for trez_name in trez_files:
        trez_path     = os.path.join(FEATURES_DIR, trez_name)
        expected_path = trez_path.replace('.trez', '.expected')
        label         = trez_name.replace('.trez', '')

        try:
            actual_out, stderr_out, retcode = run_trez(trez_path)
        except subprocess.TimeoutExpired:
            print(f"TIMEOUT  {label}")
            errors += 1
            continue

        actual_lines = actual_out.splitlines()

        if UPDATE_MODE:
            with open(expected_path, 'w') as f:
                f.write(actual_out + '\n' if actual_out else '')
            print(f"UPDATED  {label}")
            continue

        if not os.path.exists(expected_path):
            print(f"MISSING  {label}  (sin archivo .expected — ejecuta con --update)")
            errors += 1
            continue

        with open(expected_path) as f:
            expected_lines = f.read().rstrip('\n').splitlines()

        if retcode != 0 and stderr_out:
            print(f"ERROR    {label}\n  {stderr_out.splitlines()[-1]}")
            errors += 1
            continue

        diffs = compare(label, actual_lines, expected_lines)
        if not diffs:
            print(f"PASS     {label:<35} ({len(actual_lines)} líneas)")
            passed += 1
        else:
            print(f"FAIL     {label}")
            for d in diffs[:5]:
                print(d)
            if len(diffs) > 5:
                print(f"  ... y {len(diffs) - 5} diferencias más")
            failed += 1

    total = passed + failed + errors
    print(f"\n{'─'*50}")
    print(f"Resultado: {passed}/{total} pasaron", end='')
    if failed:
        print(f"  |  {failed} fallaron", end='')
    if errors:
        print(f"  |  {errors} errores", end='')
    print('\n')
    sys.exit(0 if failed == 0 and errors == 0 else 1)


if __name__ == '__main__':
    main()
