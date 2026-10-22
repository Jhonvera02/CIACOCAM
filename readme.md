# CIACOCAM

**Sistema de Control Integral y Administración de Cámaras de Seguridad**

CIACOCAM es un módulo para **Odoo** orientado a la gestión y seguimiento de una infraestructura de videovigilancia. Permite organizar la información de ubicaciones, cámaras y equipos DVR/NVR, además de registrar inspecciones, incidencias, mantenimientos e historial de eventos.

## Funcionalidades

- Gestión de ubicaciones.
- Registro y administración de cámaras de seguridad.
- Gestión de equipos DVR/NVR.
- Checklists para inspecciones periódicas.
- Registro y seguimiento de incidencias.
- Gestión de mantenimientos preventivos y correctivos.
- Consulta del historial de eventos.
- Vistas de navegación y panel de control.
- Grupos de seguridad y permisos de acceso.

## Tecnologías

- **Odoo 19**
- **Python** para los modelos del módulo.
- **XML** para vistas, menús, datos y configuración de seguridad.
- **CSV** para permisos de acceso.
- **PostgreSQL 16** como base de datos.
- **Docker Compose** para facilitar el entorno de ejecución.

## Estructura del módulo

```text
CIACOCAM/
├── __init__.py
├── __manifest__.py
├── docker-compose.yml
├── data/
│   └── data.xml
├── models/
│   ├── __init__.py
│   ├── camara.py
│   ├── checklist.py
│   ├── dvr.py
│   ├── historial.py
│   ├── incidencia.py
│   ├── inspeccion.py
│   ├── mantenimiento.py
│   └── ubicacion.py
├── security/
│   ├── ir.model.access.csv
│   └── security_groups.xml
├── static/
│   └── description/
│       └── icon.png
└── views/
    ├── camara_views.xml
    ├── checklist_views.xml
    ├── dashboard.xml
    ├── dvr_views.xml
    ├── historial_views.xml
    ├── incidencia_views.xml
    ├── inspeccion_views.xml
    ├── mantenimiento_views.xml
    ├── menu.xml
    └── ubicacion_views.xml
```

## Requisitos

- Docker instalado.
- Docker Compose disponible.
- Acceso a los puertos `8069` (interfaz web de Odoo) y `5432` (PostgreSQL), si se mantienen los puertos definidos en el archivo Compose.

## Instalación y ejecución con Docker Compose

1. Clona el repositorio:

   ```bash
   git clone URL_DE_TU_REPOSITORIO
   ```

2. Entra en la carpeta del proyecto:

   ```bash
   cd CIACOCAM
   ```

3. Revisa el archivo `docker-compose.yml` antes de iniciar los servicios. Para un entorno real, cambia las credenciales de ejemplo y evita exponer PostgreSQL a redes no confiables.

4. Inicia Odoo y PostgreSQL:

   ```bash
   docker compose up -d
   ```

5. Abre Odoo en el navegador:

   [http://localhost:8069](http://localhost:8069)

6. Crea o selecciona una base de datos desde Odoo. En la lista de aplicaciones, actualiza la lista de aplicaciones si es necesario y busca el módulo **CIACOCAM** para instalarlo.

### Importante sobre la configuración

El `docker-compose.yml` incluido usa valores de ejemplo para PostgreSQL. Son adecuados únicamente para pruebas locales y **no deben utilizarse sin cambios en producción**. Configura contraseñas seguras, restringe la exposición de puertos y realiza copias de seguridad de la base de datos y de los datos de Odoo.

El servicio monta la carpeta del proyecto como un directorio de addons adicionales. Si la estructura de tu repositorio cambia, revisa la ruta montada y el parámetro `--addons-path`.

## Licencia

El manifiesto del módulo declara la licencia **LGPL-3**. Consulta las condiciones de esa licencia antes de redistribuir o modificar el proyecto.

## Autoría

- **Autor declarado en el manifiesto:** SIGI

## Estado del proyecto

Módulo Odoo instalable según su manifiesto. Antes de usarlo en un entorno productivo, verifica la instalación en una instancia de prueba y valida los permisos, los flujos de trabajo y las copias de seguridad.
