<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentación del Proyecto de Vibraciones Mecánicas</title>
</head>
<body>
    <h1>Documentación del Proyecto de Vibraciones Mecánicas</h1>
    <h2>Universidad Tecnológica de Panamá</h2>
    <p>
        <strong>Facultad de Ingeniería Mecánica</strong><br>
        <em>Trabajo de Análisis de Vibraciones según la norma ISO 10816</em>
    </p>
    <p>
        Este proyecto analiza los datos de vibración de motores eléctricos y genera una clasificación basada en la norma ISO 10816. Además, produce una gráfica de severidad de vibración en formato log-log para evaluar el desempeño de los motores.
    </p>
    <h2>Estructura del Directorio</h2>
    <ul>
        <li><strong><code>mechanic.py</code></strong>: 
            Este archivo procesa los datos de los motores para calcular su clasificación y genera un archivo CSV con los resultados.</li>
        <li><strong><code>graph.py</code></strong>: 
            Este archivo genera una gráfica log-log de severidad de vibración y la guarda como una imagen PNG.</li>
        <li><strong><code>condiciones_motores.csv</code></strong>: Archivo generado que contiene los datos procesados y clasificados.</li>
        <li><strong><code>grafica_severidad_vibracion.png</code></strong>: Imagen generada que muestra la gráfica de severidad de vibración.</li>
        <li><strong><code>venv/</code></strong>: Entorno virtual de Python para manejar las dependencias del proyecto.</li>
    </ul>
    <h2>Requisitos Previos</h2>
    <ol>
        <li><strong>Python 3.x</strong>: Asegúrate de tener Python instalado.</li>
        <li><strong>Bibliotecas necesarias</strong>: Instálalas con:
            <pre><code>pip install pandas matplotlib</code></pre>
        </li>
        <li><strong>Entorno interactivo</strong>: Para visualizar la gráfica directamente, usa un entorno gráfico como Jupyter Notebook o una máquina con GUI.</li>
    </ol>
    <h2>Uso</h2>
    <h3>1. Ejecutar el procesamiento de datos</h3>
    <p>Ejecuta <code>mechanic.py</code> para calcular las condiciones de los motores y generar el archivo CSV:</p>
    <pre><code>python3 mechanic.py</code></pre>
    <p>Esto generará el archivo <code>condiciones_motores.csv</code>.</p>
    <h3>2. Generar la gráfica</h3>
    <p>Ejecuta <code>graph.py</code> para crear la gráfica log-log:</p>
    <pre><code>python3 graph.py</code></pre>
    <p>Esto generará el archivo <code>grafica_severidad_vibracion.png</code>.</p>
    <h3>3. Abrir los archivos generados</h3>
    <ul>
        <li><code>condiciones_motores.csv</code>: Ábrelo en Excel o cualquier editor de texto.</li>
        <li><code>grafica_severidad_vibracion.png</code>: Ábrelo con cualquier visor de imágenes.</li>
    </ul>
    <h2>Notas Importantes</h2>
    <ul>
        <li><strong>Advertencia sobre entornos no interactivos</strong>: 
            Si el proyecto se ejecuta en un entorno sin soporte gráfico, la gráfica no se mostrará en pantalla y solo se guardará como archivo PNG.</li>
        <li><strong>Generación de archivos</strong>: 
            Cada ejecución sobrescribirá los archivos <code>condiciones_motores.csv</code> y <code>grafica_severidad_vibracion.png</code>.</li>
    </ul>
    <h2>Contexto Académico</h2>
    <p>
        Este proyecto es parte de una asignación de la <strong>Universidad Tecnológica de Panamá</strong> en la Facultad de Ingeniería Mecánica. Su objetivo es demostrar el análisis y la clasificación de vibraciones mecánicas en motores eléctricos utilizando herramientas computacionales y conceptos avanzados de ingeniería mecánica.
    </p>
</body>
</html>
