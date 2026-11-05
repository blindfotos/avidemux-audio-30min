from pathlib import Path
root = Path("avidemux")
changes = [
    (root / "avidemux/qt4/ADM_userInterfaces/ADM_gui/gui2.ui", "<number>-99999</number>", "<number>-1800000</number>"),
    (root / "avidemux/qt4/ADM_userInterfaces/ADM_gui/gui2.ui", "<number>99999</number>", "<number>1800000</number>"),
    (root / "avidemux_plugins/ADM_scriptEngines/qtScript/src/AudioOutput.cpp", 'validateNumber("timeShift", timeShift, -99999, 99999)', 'validateNumber("timeShift", timeShift, -1800000, 1800000)'),
]
for file, old, new in changes:
    if not file.exists():
        raise SystemExit(f"No existe: {file}")
    content = file.read_text(encoding="utf-8")
    count = content.count(old)
    if count != 1:
        raise SystemExit(f"Se esperaban 1 coincidencia de {old!r} en {file}; hay {count}")
    file.write_text(content.replace(old, new), encoding="utf-8")
    print(f"Modificado: {file}: {old} -> {new}")
print("Parche aplicado. Aún falta compilar y probar.")
