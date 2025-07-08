# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Detección de plagas agrícolas a partir de imágenes

## Objetivo del Proyecto

El objetivo principal del presente proyecto es desarrollar un sistema robusto y eficiente capaz de identificar y clasificar diversas plagas agrícolas a partir de imágenes naturales. Estas imágenes, capturadas en entornos reales, se categorizarán meticulosamente en 12 clases distintas, cada una representando una plaga específica o un tipo de insecto de interés agronómico. Para una comprensión detallada de estas categorías y las características inherentes a cada imagen, puede consultar la información completa en el diccionario de datos anexo.

## Alcance del Proyecto

### Incluye:

- El proyecto se sustenta en un conjunto de datos de imágenes naturales centrado específicamente en diversas especies de insectos, estructurado en 12 categorías distintas que representan una clasificación de plagas agrícolas. Este dataset, obtenido de Kaggle, consiste en 5494 imágenes en formatos JPG y PNG.
- Al finalizar este proyecto, se espera haber desarrollado un modelo de aprendizaje profundo capaz de clasificar las imágenes de plagas agrícolas dentro de sus 12 clases definidas. Los resultados incluyen la obtención de un modelo entrenado y optimizado, junto con un informe detallado de métricas de rendimiento como la exactitud, precisión, recall y F1-score, demostrando la capacidad del sistema para realizar inferencias correctas sobre nuevas imágenes y un análisis de su desempeño por clase.
- El éxito del proyecto se determinará por varios criterios clave, incluyendo que el modelo alcance una precisión global superior a un umbral predefinido (por ejemplo, 85-90%) en el conjunto de prueba, y que demuestre un rendimiento consistente y robusto para la mayoría de las clases, medido a través de métricas como el F1-score.

### Excluye:

- El proyecto se enfoca exclusivamente en la detección de las plagas especificadas en el diccionario de datos, excluyendo explícitamente cualquier otra especie no documentada. Asimismo, el alcance no contempla el análisis de anomalías; por lo tanto, se asume que el sistema recibirá imágenes que contengan únicamente los insectos de interés definidos.

## Metodología

La metodología del proyecto seguirá un enfoque iterativo y basado en CripsDM. Inicialmente, se realizará un Análisis Exploratorio de Datos (EDA) exhaustivo sobre el conjunto de imágenes de abejas, incluyendo la caracterización de la distribución de clases y la homogeneización de las dimensiones de las imágenes. Posteriormente, se procederá al preprocesamiento y aumentación de datos para preparar las imágenes para el entrenamiento. La fase de modelado implicará la selección y el entrenamiento de una red neuronal convolucional (CNN), posiblemente utilizando técnicas de Transfer Learning para aprovechar modelos pre-entrenados. Seguidamente, el modelo será evaluado rigurosamente utilizando métricas de clasificación estándar sobre un conjunto de prueba independiente, para validar su precisión y capacidad de generalización antes de presentar las conclusiones y los posibles pasos futuros. Finalmente, el modelo será desplegado por medio de un servicio web. 

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 23 de junio al 28 de junio del 2025|
| Preprocesamiento, análisis exploratorio | 2 semanas | del 30 de junio al 12 de julio del 2025|
| Modelamiento y extracción de características | 1 semanas | del 07 de julio al 12 de julio del 2025|
| Despliegue | 1 semanas | del 14 de julio al 19 de julio del 2025 |
| Evaluación y entrega final | 3 semanas | del 07 de julio al 25 de julio del 2025|
 
## Equipo del Proyecto

- Líder: Juan Sebastian Malagón Torres
- Ingeniero de datos: Sebastián Daniel Moreno
- Cientifico de datos: Juan Sebastian Malagón Torres
- Ingeniero en ML: Sebastián Daniel Moreno

## Presupuesto

| Categoría de Gasto | Descripción | Costo Estimado (USD) | Notas / Consideraciones |
| :----------------- | :---------- | :------------------- | :---------------------- |
| **I. Personal** | | | |
| Científico de Datos Senior | Diseño del modelo, preprocesamiento avanzado, optimización. | $8,000 | 2 meses a tiempo parcial |
| Ingeniero de ML Junior | Implementación de código, experimentos, EDA. | $5,000 | 2.5 meses a tiempo completo |
| **II. Infraestructura y Software** | | | |
| Plataforma Cloud (GPU) | AWS/GCP/Azure para entrenamiento de modelos (instancias GPU). | $1,500 | Costos de cómputo por ~200 horas de GPU |
| Almacenamiento Cloud | S3/GCS para dataset de imágenes y checkpoints del modelo. | $50 | 500 GB por 2 meses |
| Licencias de Software | Herramientas específicas o IDEs (si aplica, asumimos open-source). | $0 | Se utilizarán herramientas y librerías open-source (Python, TensorFlow/PyTorch, scikit-learn). |
| **IV. Misceláneos** | | | |
| Investigación y Desarrollo | Tiempo para pruebas de concepto, lectura de artículos, etc. | $700 | Horas dedicadas a exploración y resolución de problemas. |
| Gestión de Proyecto | Coordinación, reuniones, documentación. | $300 | Pequeño porcentaje del tiempo del equipo. |
| Contingencias | Fondo para imprevistos (aprox. 10% del total). | $1,555 | Buffer para gastos inesperados. |
| **TOTAL ESTIMADO DEL PROYECTO** | | **$17,105** | |


## Stakeholders

- Los stakeholders clave en este proyecto serán biólogos y agrónomos interesados en la identificación automática de plagas en los cultivos
- Los expertos en Agronomía/Biología actúan como validadores del conocimiento de dominio, asesorando sobre la clasificación de plagas y la interpretación de resultados, y se les consulta para asegurar la relevancia práctica del modelo. 
- Las expectativas  giran en torno a la entrega de un modelo funcional y preciso que clasifique automáticamente las 12 plagas de interes. 

## Aprobaciones

- Juan Sebastian Malagón Torres