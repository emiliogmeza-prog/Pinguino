# Entrega en GitHub

Carpeta a subir:

```text
programacion/
```

Repositorio usado:

```text
Pinguino
```

No es necesario subir carpetas generadas por Python como `__pycache__`, `build`
o `dist`. Por eso se incluye `.gitignore`.

Si se sube desde la pagina de GitHub:

1. Crear un repositorio nuevo.
2. Entrar al repositorio.
3. Usar `Add file` y luego `Upload files`.
4. Arrastrar el contenido de la carpeta `programacion`.
5. Confirmar con un mensaje como `Agregar proyecto Kagastian 5000`.

Si se sube con Git instalado:

```bash
git init
git add .
git commit -m "Agregar proyecto Kagastian 5000"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```
