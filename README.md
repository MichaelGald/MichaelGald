<div align="center">

# Michael Galdámez

### Desarrollador Full-Stack

Construyo software robusto y escalable: APIs con **.NET**, aplicaciones web con **React / Next.js** y apps móviles con **React Native**, con un enfoque en arquitectura limpia y ciberseguridad.

<br/>

![C#](https://img.shields.io/badge/C%23-.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

San Pedro Sula, Honduras &nbsp;·&nbsp; Ingeniería en Sistemas, UNAH-CUROC

</div>

---

## Sobre mí

Soy estudiante de Ingeniería en Sistemas en la **UNAH-CUROC** y desarrollador Full-Stack apasionado por la arquitectura de software, las aplicaciones web/móviles escalables y la ciberseguridad.

Me interesa todo el ciclo de un producto: modelar el dominio, diseñar la API, construir la interfaz y desplegarla de forma segura. Trabajo con transacciones atómicas, control de acceso granular y arquitecturas pensadas para crecer.

- **Actualmente:** `[qué estás construyendo ahora, ej. SIGREF]`
- **Aprendiendo:** `[ej. arquitectura limpia / CQRS, Kubernetes, pentesting avanzado]`
- **Abierto a:** proyectos freelance, colaboraciones y oportunidades como desarrollador Full-Stack.
- **Pregúntame sobre:** .NET, React, modelado de bases de datos y laboratorios de ciberseguridad.

---

## Stack tecnológico

| Área | Tecnologías |
|---|---|
| **Backend** | ![C#](https://skillicons.dev/icons?i=cs) ![.NET](https://skillicons.dev/icons?i=dotnet) ![Node.js](https://skillicons.dev/icons?i=nodejs) ![Express](https://skillicons.dev/icons?i=express) <br/> Web APIs REST · OpenAPI · Entity Framework Core · Hangfire · Keycloak (OIDC/JWT/RBAC) · HL7 FHIR · OpenTelemetry |
| **Frontend** | ![TypeScript](https://skillicons.dev/icons?i=ts) ![JavaScript](https://skillicons.dev/icons?i=js) ![React](https://skillicons.dev/icons?i=react) ![Next.js](https://skillicons.dev/icons?i=nextjs) ![HTML](https://skillicons.dev/icons?i=html) ![CSS](https://skillicons.dev/icons?i=css) <br/> Vite · TanStack Query · Zustand · Formik/Yup · Vitest |
| **UI / Estilos** | ![Tailwind](https://skillicons.dev/icons?i=tailwind) ![Figma](https://skillicons.dev/icons?i=figma) <br/> Ant Design · shadcn/ui · React Native Reusables · Canva |
| **Móvil** | ![React Native](https://skillicons.dev/icons?i=react) React Native |
| **Bases de datos** | ![PostgreSQL](https://skillicons.dev/icons?i=postgres) ![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white) ![MongoDB](https://skillicons.dev/icons?i=mongodb) <br/> Modelado relacional · consultas complejas · optimización |
| **DevOps & Sistemas** | ![Docker](https://skillicons.dev/icons?i=docker) ![Git](https://skillicons.dev/icons?i=git) ![Arch](https://skillicons.dev/icons?i=arch) ![Linux](https://skillicons.dev/icons?i=linux) <br/> Docker Compose · Nginx · Tailscale VPN · CachyOS / Arch Linux |
| **Seguridad** | Pentesting en entornos controlados · Hydra · análisis de malware y ransomware · mitigación |
| **Hardware & IoT** | ![Arduino](https://skillicons.dev/icons?i=arduino) Arduino UNO · sensores ultrasónicos · L298N / L293D · Bluetooth |
| **Modelado & Redes** | AutoCAD (2D/3D) · Cisco Packet Tracer |

---

## Proyectos destacados

### SIGREF · Gestión administrativa para organizaciones de salud
> Plataforma que centraliza pacientes, servicios, caja, ingresos, facturación, reportes y auditoría, reduciendo tareas manuales y dando trazabilidad a cada operación.

![.NET](https://img.shields.io/badge/.NET_9-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![React](https://img.shields.io/badge/React_19-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Keycloak](https://img.shields.io/badge/Keycloak-4D4D4D?style=flat-square&logo=keycloak&logoColor=white)
![HL7 FHIR](https://img.shields.io/badge/HL7_FHIR-R4-E44D26?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

- **Módulos operativos:** pacientes y profesionales, catálogos de servicios, sesiones de caja, facturación e ingresos, dashboards y reportes.
- **Auditoría y trazabilidad** de eventos y cambios, con almacenamiento documental en MongoDB.
- **Seguridad:** autenticación con Keycloak (OpenID Connect / JWT) y autorización basada en roles (RBAC).
- **Interoperabilidad clínica** con **HL7 FHIR R4** para información de referencia.
- **Procesamiento en segundo plano:** tareas y generación de reportes con un worker dedicado (Hangfire).
- **Contratos tipados de punta a punta:** API documentada con OpenAPI y cliente TypeScript generado con Orval.
- **Observabilidad y despliegue:** OpenTelemetry y entornos reproducibles con Docker Compose y Nginx.
- **Proyecto en equipo** de 8 desarrolladores. **Mi rol:** `[ej. backend / frontend / auditoría / FHIR...]`
- **Software propietario:** el código no es público.

---

### Laboratorio de simulación de Pentesting
> Entorno controlado para practicar ciberseguridad ofensiva y defensiva.

- Red de máquinas virtuales interconectadas mediante **Tailscale VPN**.
- Simulación de vectores de ataque, incluyendo fuerza bruta con **Hydra** sobre OpenSSH.
- Análisis forense y estrategias de mitigación, con estudio de ransomware (caso **Conti**).
- *Todo el trabajo se realiza en entornos propios y con fines educativos.*

---

## Estadísticas de GitHub

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=TU_USUARIO_GITHUB&show_icons=true&theme=tokyonight&hide_border=true" alt="Estadísticas de GitHub" />
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=TU_USUARIO_GITHUB&layout=compact&theme=tokyonight&hide_border=true" alt="Lenguajes más usados" />

</div>

---

## Objetivos

- Profundizar en arquitectura de software (DDD, Clean Architecture) y sistemas distribuidos.
- Fortalecer mis habilidades en ciberseguridad aplicada al desarrollo seguro.
- Seguir construyendo productos que resuelvan problemas reales para negocios en Honduras y la región.

---

## Contacto

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MichaelGald)

*¿Tienes un proyecto en mente? Hablemos.* 

</div>
