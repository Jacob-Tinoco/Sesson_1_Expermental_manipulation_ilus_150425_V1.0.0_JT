# 🖋️ Illustrator Experimental Manipulation – Session 1

> **Versión:** V1.0.0 JT  
> **Fecha de creación:** 15-04-2025

---

## 📘 Descripción General

Este repositorio contiene un conjunto de scripts en Python y plantillas de ExtendScript para automatizar procesos de manipulación y extracción de agrupaciones en archivos de Adobe Illustrator. Está diseñado para:

- Identificar y transformar grupos de objetos (logos, patrones de color, etc.).
- Exportar activos o preparar datos intermedios para análisis.
- Mantener versiones claras y reproducibles del flujo de trabajo experimental.

---

## 📚 Tabla de Contenidos

1. [Estructura del Proyecto](#-estructura-del-proyecto)  
2. [Descripción de Scripts Clave](#-descripción-de-scripts-clave)  
3. [Cómo Ejecutar](#-cómo-ejecutar)  
4. [Dataset / Insumos](#-dataset--insumos)  
5. [Tecnologías Usadas](#-tecnologías-usadas)  
6. [Notas Finales](#-notas-finales)  
7. [Autor](#-autor)

---

## 📁 Estructura del Proyecto

```bash
SESSION_1_EXPERIMENTAL_MANIPULATION_ILUS_150425_V1.0.0_JT/
├── 📂 Backup/                          # Copias de archivos originales de Illustrator
├── 📂 BLANKS/                          # Plantillas en blanco para pruebas
├── 📂 LAST_SCRIPTS_REFERENCE/         # Scripts de referencia anteriores
├── 📂 LOGOS/                          # Recursos de logos e imágenes
├── 📂 reemplazo_e_identificacion_de_colores/  # Paletas y patrones de color
├── 📂 reportes/                       # Ejemplos de reports generados
├── 📄 Analisis_exploratorio_notas.txt # Notas de análisis preliminar
├── 🔹 INFO_LOGOS_GRUPO.py             # Script de extracción de grupos de logos
├── 🔹 INFO_LOGOS_POSICION01.py        # Script para posicionamiento de logos (v1)
├── 🔹 INGO_GROUPS_extract_transform_mac00.py  # Versión inicial de extracción/transformación
├── 🔹 INGO_GROUPS_extract_transform_mac01.py  # Versión mejorada con control de IDs
├── 🔹 INGO_GROUPS_extract_transform_mac02.py  # Versión final con generación de log
├── 🔹 replace_parent_groups_mac07.py  # Script de reasignación de grupos padre
└── 📄 README.md                       # Documentación del proyecto (este archivo)
````

---

## 📜 Descripción de Scripts Clave

### 🔹 INFO\_LOGOS\_GRUPO.py

* 📌 **Función:** Extrae metadatos de grupos de logos dentro de un documento de Illustrator.
* 🗓️ **Última Modificación:** 15-04-2025
* ✅ **Estado:** 🟢 Producción

### 🔹 INFO\_LOGOS\_POSICION01.py

* 📌 **Función:** Calcula y reporta la posición de cada logo en el lienzo.
* 🗓️ **Última Modificación:** 15-04-2025
* ✅ **Estado:** 🟢 Producción

### 🔹 INGO\_GROUPS\_extract\_transform\_mac0\[0–2].py

* 📌 **Función General:**

  1. Detectar grupos por nombre/ID.
  2. Aplicar transformaciones (escala, rotación (aun en pruebas apra los angulos), recolor).
  3. Exportar o registrar resultados en un log.
* 📑 **Versiones:**

  * **mac00:** Versión base, detección y exportación.
  * **mac01:** Añade validaciones de ID y control de errores.
  * **mac02:** Genera reportes detallados y limpia archivos temporales.

### 🔹 replace\_parent\_groups\_mac07.py

* 📌 **Función:** Reemplaza referencias de grupos padre en documentos, útil para reorganización masiva.
* 🗓️ **Última Modificación:** 15-04-2025
* ✅ **Estado:** 🟢 Producción

---

## 🚀 Cómo Ejecutar

1. **Descargar el script**

2. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```
3. **Preparar entorno**

   * Tener Adobe Illustrator (2021+) instalado y permisos de automatización habilitados en macOS.
   * Colocar archivos `.ai` en la carpeta `Backup/` o `BLANKS/`.
4. **Ejecutar un script**

   ```bash
   python INGO_GROUPS_extract_transform_mac02.py --input path/to/file.ai --output ./reportes
   ```
5. **Revisar resultados**

   * Los assets transformados y logs se guardan en `reportes/`.
   * Consulte `Analisis_exploratorio_notas.txt` para observaciones manuales.

---

## 🧪 Dataset / Insumos

* **Archivos de Illustrator:** Formato `.ai`, con capas y grupos previamente nombrados.
* **Paletas de color:** JSON o `.ase` en `reemplazo_e_identificacion_de_colores/`.
* **Recursos de prueba:** Cualquier documento de prueba en `BLANKS/`.

---

## 📦 Tecnologías Usadas

* **Python 3.10+**
* **ExtendScript (JavaScript para Illustrator)**
* **PyWin32 / comtypes** (solo si se usa en Windows)
* **macOS Automation** (`osascript`)
* **Librerías Python:** `argparse`, `logging`, `tempfile`

---

## 📝 Notas Finales

* ⚠️ Asegúrate de versionar cada script con el siguiente esquema:
  `NOMBRE_ddMMyy_Vx.x.x_JT.py`.
* 💡 Documenta los cambios en cada versión en el CHANGELOG dentro de `LAST_SCRIPTS_REFERENCE/`.
* 🔒 No incluir archivos de diseño confidenciales al compartir en público.

---

## ✍️ Autor

**Jacob Tinoco**
📆 Última actualización: 15-04-2025
📧 [jtinoco@maximaapparel.com](mailto:jtinoco@maximaapparel.com)


